#!/usr/bin/env python3
"""Build a GitHub Pages site using Python standard library only."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / 'site' / 'template.html'
OUTPUT = ROOT / 'index.html'

def generate():
    text = TEMPLATE.read_text(encoding='utf-8')
    for kind in ('chapters', 'templates', 'plan'):
        content = json.loads((ROOT / 'data' / f'{kind}.json').read_text(encoding='utf-8'))
        # Prevent accidentally forming a closing script tag in embedded JSON.
        encoded = json.dumps(content, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
        text = text.replace(f'__{kind.upper()}_JSON__', encoded)
    return text

def main():
    output = generate()
    if '--check' in sys.argv:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding='utf-8') != output:
            print('index.html is stale: run python3 scripts/build.py', file=sys.stderr)
            sys.exit(1)
        print('index.html is up to date')
        return
    OUTPUT.write_text(output, encoding='utf-8')
    print('Generated', OUTPUT)

if __name__ == '__main__':
    main()
