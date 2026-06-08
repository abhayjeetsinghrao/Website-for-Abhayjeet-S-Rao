#!/usr/bin/env python3
"""
verify_insight.py — Pre-publish AI verification gate for insight articles.

Parses an insight HTML file, extracts the case citation and key legal
holdings, then uses Claude with live web search to confirm:
  1. The case is a real, published decision
  2. The case number / neutral citation is accurate
  3. Key legal holdings match the actual judgment
  4. All statutory provisions cited exist

VERDICT: PASS → commit and publish
         FLAG  → minor corrections needed before publishing
         FAIL  → material errors; do not publish

Usage:
    python3 scripts/verify_insight.py insights/<slug>.html

Requirements:
    pip install anthropic
    ANTHROPIC_API_KEY set in environment
"""

import re
import sys
import json
import os


# ── HTML parsing (no external dependencies) ──────────────────────────────────

def _strip_tags(html):
    text = re.sub(r'<[^>]+>', ' ', html)
    text = re.sub(r'&mdash;', '—', text)
    text = re.sub(r'&ndash;', '–', text)
    text = re.sub(r'&rsquo;', "'", text)
    text = re.sub(r'&ldquo;', '"', text)
    text = re.sub(r'&rdquo;', '"', text)
    text = re.sub(r'&amp;', '&', text)
    text = re.sub(r'&#[0-9]+;', '', text)
    text = re.sub(r'&[a-zA-Z]+;', '', text)
    return re.sub(r'\s+', ' ', text).strip()


def _extract_class(html, class_name, tag='div'):
    """Return inner text of the first element with the given class."""
    pattern = rf'<{tag}[^>]*\bclass="{re.escape(class_name)}"[^>]*>(.*?)</{tag}>'
    m = re.search(pattern, html, re.DOTALL)
    return _strip_tags(m.group(1)) if m else ''


def parse_insight(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    title     = _extract_class(html, 'art-title', 'h1')
    citation  = _extract_class(html, 'art-citation')
    art_tag   = _extract_class(html, 'art-tag', 'span')
    date_str  = _extract_class(html, 'art-date')
    provisions = re.findall(r'class="art-prov">(.*?)</span>', html)
    provisions = [_strip_tags(p) for p in provisions]

    # Body text — first 2 000 chars is enough for holdings verification
    body_m = re.search(
        r'<div class="art-text">(.*?)</div>\s*<div class="art-footer-nav">',
        html, re.DOTALL
    )
    body = _strip_tags(body_m.group(1))[:2000] if body_m else ''

    return {
        'file': filepath,
        'title': title,
        'citation': citation,
        'tag': art_tag,
        'date': date_str,
        'provisions': provisions,
        'body': body,
    }


# ── Verification via Claude + web search ────────────────────────────────────

SYSTEM_PROMPT = """You are a strict legal fact-checker for a professional law website.
Your sole job is to verify that an insight article is factually accurate before it
is published. Be rigorous: errors in legal citations destroy the site's credibility
and its SEO authority. Return only a JSON object — no prose, no markdown."""

def build_user_prompt(data):
    return f"""Verify this legal insight article using web search:

TITLE     : {data['title']}
CITATION  : {data['citation']}
AREA      : {data['tag']}
DATE FILED: {data['date']}
PROVISIONS: {', '.join(data['provisions'])}

ARTICLE BODY (excerpt):
{data['body']}

Search for the case or legal event, then return ONLY this JSON:
{{
  "verdict": "PASS" | "FLAG" | "FAIL",
  "case_real": true | false,
  "citation_correct": true | false,
  "holdings_accurate": true | false,
  "issues": ["specific factual errors found, if any"],
  "corrections": ["exact corrections to apply, if any"],
  "verified_citation": "the authoritative citation as you found it online"
}}

Verdict rules:
- PASS : case is real, citation correct, holdings accurate
- FLAG : case is real but citation has a minor error or holdings need small correction
- FAIL : case does not exist, citation is materially wrong, or holdings are fabricated"""


def run_verification(data):
    try:
        import anthropic
    except ImportError:
        print("ERROR: anthropic not installed.\n  Run: pip install anthropic")
        sys.exit(2)

    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set.")
        sys.exit(2)

    client = anthropic.Anthropic(api_key=api_key)

    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1500,
        system=SYSTEM_PROMPT,
        tools=[{
            "type": "web_search_20250305",
            "name": "web_search",
        }],
        tool_choice={"type": "auto"},
        messages=[{"role": "user", "content": build_user_prompt(data)}],
    )

    # Extract the final text block (after any tool calls)
    for block in reversed(response.content):
        if hasattr(block, 'type') and block.type == 'text':
            text = block.text.strip()
            json_m = re.search(r'\{[\s\S]*\}', text)
            if json_m:
                try:
                    return json.loads(json_m.group())
                except json.JSONDecodeError:
                    pass

    return {
        "verdict": "ERROR",
        "case_real": None,
        "citation_correct": None,
        "holdings_accurate": None,
        "issues": ["Verification agent returned an unparseable response."],
        "corrections": [],
        "verified_citation": "",
    }


# ── CLI output ───────────────────────────────────────────────────────────────

def fmt_bool(v):
    if v is True:  return "YES"
    if v is False: return "NO"
    return "?"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print(f"ERROR: File not found: {filepath}")
        sys.exit(1)

    sep = "=" * 62
    print(f"\n{sep}")
    print(f"  INSIGHT VERIFICATION")
    print(f"  {filepath}")
    print(sep)

    data = parse_insight(filepath)
    print(f"  Title     : {data['title'][:70]}")
    print(f"  Citation  : {data['citation'][:80]}")
    print(f"  Provisions: {', '.join(data['provisions'])}")
    print(f"\n  Running AI verification with live web search …\n")

    result = run_verification(data)

    verdict = result.get('verdict', 'UNKNOWN')
    print(f"  VERDICT           :  {verdict}")
    print(f"  Case real         :  {fmt_bool(result.get('case_real'))}")
    print(f"  Citation correct  :  {fmt_bool(result.get('citation_correct'))}")
    print(f"  Holdings accurate :  {fmt_bool(result.get('holdings_accurate'))}")

    if result.get('verified_citation'):
        print(f"\n  Authoritative citation:")
        print(f"    {result['verified_citation']}")

    issues = result.get('issues') or []
    if issues:
        print(f"\n  ISSUES:")
        for i in issues:
            print(f"    ✗  {i}")

    corrections = result.get('corrections') or []
    if corrections:
        print(f"\n  CORRECTIONS NEEDED:")
        for c in corrections:
            print(f"    →  {c}")

    print(f"\n{'─' * 62}")
    if verdict == 'PASS':
        print("  ✓  CLEARED — article may be committed and published.")
        print(sep)
        sys.exit(0)
    elif verdict == 'FLAG':
        print("  ⚠  FLAGGED — apply corrections, then re-run before publishing.")
        print(sep)
        sys.exit(1)
    else:
        print("  ✗  NOT CLEARED — do not publish. Fix all issues first.")
        print(sep)
        sys.exit(1)


if __name__ == '__main__':
    main()
