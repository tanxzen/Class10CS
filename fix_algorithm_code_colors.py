#!/usr/bin/env python3
"""
Script to fix algorithm code block colors for better readability
"""

import os
import re
from pathlib import Path

def get_algorithm_code_fix_css():
    """Returns CSS to fix algorithm code block colors"""
    return """
      /* Fix algorithm code blocks for better readability */
      .algorithm-card code,
      .algorithm-card pre {
        color: var(--algorithm-text) !important;
        background-color: var(--algorithm-bg) !important;
      }

      /* Light theme algorithm code */
      :root .algorithm-card code,
      :root .algorithm-card pre {
        color: #ecf0f1 !important;
        background-color: #2c3e50 !important;
      }

      /* Dark theme algorithm code */
      [data-theme="dark"] .algorithm-card code,
      [data-theme="dark"] .algorithm-card pre {
        color: #f1f5f9 !important;
        background-color: #0f172a !important;
      }

      /* General code blocks outside algorithm cards */
      code {
        color: var(--code-text) !important;
        background-color: var(--bg-secondary) !important;
        padding: 2px 6px;
        border-radius: 4px;
        font-family: 'Courier New', monospace;
      }

      pre {
        color: var(--code-text) !important;
        background-color: var(--bg-secondary) !important;
        padding: 12px;
        border-radius: 6px;
        overflow-x: auto;
        font-family: 'Courier New', monospace;
      }

      /* Ensure algorithm cards have proper text colors */
      .algorithm-card {
        background: var(--algorithm-bg) !important;
        color: var(--algorithm-text) !important;
      }

      .algorithm-card * {
        color: var(--algorithm-text) !important;
      }

      .algorithm-card h3,
      .algorithm-card h4,
      .algorithm-card p,
      .algorithm-card li,
      .algorithm-card span,
      .algorithm-card div,
      .algorithm-card strong,
      .algorithm-card b {
        color: var(--algorithm-text) !important;
      }"""

def process_html_file(file_path):
    """Process a single HTML file to fix algorithm code colors"""
    print(f"Fixing algorithm code colors in {file_path}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get the CSS fix
    css_fix = get_algorithm_code_fix_css()
    
    # Add the CSS fix before the closing </style> tag
    if '</style>' in content and 'Fix algorithm code blocks for better readability' not in content:
        content = content.replace('</style>', css_fix + '\n    </style>')
    elif 'Fix algorithm code blocks for better readability' in content:
        # Replace existing fix with updated version
        pattern = r'/\* Fix algorithm code blocks for better readability \*/.*?/\* Ensure algorithm cards have proper text colors \*/[^}]*}'
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, css_fix.strip(), content, flags=re.DOTALL)
    
    # Write the updated content back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✅ Fixed {file_path}")

def main():
    """Main function to process all HTML files"""
    docs_dir = Path('./docs')
    html_files = list(docs_dir.glob('*.html'))
    
    # Also check for HTML files in root
    root_html_files = list(Path('.').glob('*.html'))
    html_files.extend(root_html_files)
    
    print(f"Found {len(html_files)} HTML files to fix:")
    for file_path in html_files:
        print(f"  - {file_path}")
    
    print("\nFixing algorithm code block colors...")
    for file_path in html_files:
        try:
            process_html_file(file_path)
        except Exception as e:
            print(f"  ❌ Error processing {file_path}: {e}")
    
    print(f"\n✅ Completed fixing {len(html_files)} HTML files!")
    print("\nAlgorithm code block fixes:")
    print("  - Light theme: White text (#ecf0f1) on dark blue background (#2c3e50)")
    print("  - Dark theme: Bright white text (#f1f5f9) on very dark background (#0f172a)")
    print("  - Added proper contrast for all algorithm card elements")
    print("  - Fixed general code blocks outside algorithm cards")
    print("  - Enhanced readability with proper font families")

if __name__ == "__main__":
    main()