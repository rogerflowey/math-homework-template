#!/usr/bin/env python3
"""Download a notes.sjtu page and emit its Markdown body."""
from __future__ import annotations

import argparse
import pathlib
import sys
from typing import Optional

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from html import unescape


def read_html_source(url: str, html_file: Optional[pathlib.Path] = None) -> str:
    if html_file is not None:
        return html_file.read_text(encoding="utf-8")

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    response.encoding = response.apparent_encoding or "utf-8"
    return response.text


def _collapse_newlines(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.replace("\r", "").splitlines()).strip("\n") + "\n"


def extract_markdown(html: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    doc = soup.find(id="doc")
    if doc is None:
        doc = soup.body if soup.body is not None else soup

    for tag in doc.find_all(["script", "style", "noscript"]):
        tag.decompose()

    if doc.find(True) is None:
        raw_text = doc.get_text()
        return _collapse_newlines(unescape(raw_text))

    markdown = md(str(doc), heading_style="ATX", strip=["span"])
    return _collapse_newlines(markdown)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch a notes.sjtu page and print its Markdown contents."
    )
    parser.add_argument(
        "url",
        help="notes.sjtu page URL (e.g. https://notes.sjtu.edu.cn/s/abcdefg)",
    )
    parser.add_argument(
        "--html-file",
        type=pathlib.Path,
        help="Optional local HTML file to use instead of downloading",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=pathlib.Path,
        help="Optional output file to write the Markdown to (defaults to stdout)",
    )
    return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)

    try:
        html = read_html_source(args.url, args.html_file)
        markdown = extract_markdown(html)
    except requests.HTTPError as exc:
        print(f"HTTP error: {exc}", file=sys.stderr)
        return 1
    except requests.RequestException as exc:
        print(f"Network error: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:  # pylint: disable=broad-except
        print(f"Failed to extract markdown: {exc}", file=sys.stderr)
        return 1

    if args.output:
        args.output.write_text(markdown, encoding="utf-8")
    else:
        sys.stdout.write(markdown)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
