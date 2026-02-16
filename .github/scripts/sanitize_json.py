#!/usr/bin/env python3
"""Sanitize CLIO's moderation-results.json to fix common JSON issues."""

import json
import re
import sys

def sanitize_json(filepath):
    """Fix invalid unicode escapes and control characters in JSON file."""
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # Fix invalid unicode escapes by replacing them with safe alternatives
    # Pattern matches \u followed by non-hex characters
    content = re.sub(r'\\u(?![0-9a-fA-F]{4})', r'\\\\u', content)
    
    # Strip actual problematic control characters (keep newlines, tabs)
    content = ''.join(c if ord(c) >= 32 or c in '\n\r\t' else ' ' for c in content)
    
    try:
        data = json.loads(content)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=True)
        print('JSON sanitized successfully')
        return True
    except json.JSONDecodeError as e:
        print(f'JSON still invalid after sanitization: {e}', file=sys.stderr)
        return False

if __name__ == '__main__':
    filepath = sys.argv[1] if len(sys.argv) > 1 else '/tmp/clio-workspace/moderation-results.json'
    success = sanitize_json(filepath)
    sys.exit(0 if success else 1)
