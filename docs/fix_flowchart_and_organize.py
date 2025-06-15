#!/usr/bin/env python3
"""
Fix flowchart text visibility in light theme and organize files
"""

import os
import re
import shutil
from pathlib import Path

def get_flowchart_fix_css():
    """Returns CSS to fix flowchart text visibility in light theme"""
    return """
      /* FLOWCHART TEXT VISIBILITY FIX */
      
      /* Light theme flowchart text - MUST BE DARK */
      :root .flowchart-start,
      :root .flowchart-end,
      :root .flowchart-step,
      :root .flowchart-box,
      :root .flowchart-decision,
      :root .flowchart-branch {
        color: #1e293b !important;
      }

      :root .flowchart-decision > div {
        color: #1e293b !important;
      }

      /* Dark theme flowchart text - MUST BE LIGHT */
      [data-theme="dark"] .flowchart-start,
      [data-theme="dark"] .flowchart-end,
      [data-theme="dark"] .flowchart-step,
      [data-theme="dark"] .flowchart-box,
      [data-theme="dark"] .flowchart-decision,
      [data-theme="dark"] .flowchart-branch {
        color: #f8fafc !important;
      }

      [data-theme="dark"] .flowchart-decision > div {
        color: #f8fafc !important;
      }

      /* Ensure flowchart backgrounds are theme-appropriate */
      :root .flowchart-start,
      :root .flowchart-end,
      :root .flowchart-step,
      :root .flowchart-box,
      :root .flowchart-decision {
        background-color: #ffffff !important;
        border-color: #334155 !important;
      }

      [data-theme="dark"] .flowchart-start,
      [data-theme="dark"] .flowchart-end,
      [data-theme="dark"] .flowchart-step,
      [data-theme="dark"] .flowchart-box,
      [data-theme="dark"] .flowchart-decision {
        background-color: #1e293b !important;
        border-color: #64748b !important;
      }"""

def fix_flowchart_in_file(file_path):
    """Fix flowchart text visibility in a single HTML file"""
    print(f"Fixing flowchart text in {file_path}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get the flowchart fix CSS
    flowchart_fix = get_flowchart_fix_css()
    
    # Add the flowchart fix before the closing </style> tag
    if '</style>' in content and 'FLOWCHART TEXT VISIBILITY FIX' not in content:
        content = content.replace('</style>', flowchart_fix + '\n    </style>')
    elif 'FLOWCHART TEXT VISIBILITY FIX' in content:
        # Replace existing fix with updated version
        pattern = r'/\* FLOWCHART TEXT VISIBILITY FIX \*/.*?border-color: #64748b !important;\s*}'
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, flowchart_fix.strip(), content, flags=re.DOTALL)
    
    # Write the updated content back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✅ Fixed flowchart text in {file_path}")

def move_files_to_docs():
    """Move all files to docs folder except README.md"""
    print("\nMoving files to docs folder...")
    
    # Files to move (exclude README.md and docs folder itself)
    files_to_move = []
    for item in Path('.').iterdir():
        if item.is_file() and item.name != 'README.md' and not item.name.startswith('.'):
            files_to_move.append(item)
    
    print(f"Files to move to docs/:")
    for file_path in files_to_move:
        print(f"  - {file_path}")
    
    # Move each file
    for file_path in files_to_move:
        dest_path = Path('docs') / file_path.name
        try:
            shutil.move(str(file_path), str(dest_path))
            print(f"  ✅ Moved {file_path} to {dest_path}")
        except Exception as e:
            print(f"  ❌ Error moving {file_path}: {e}")

def main():
    """Main function"""
    print("🔧 FIXING FLOWCHART TEXT VISIBILITY AND ORGANIZING FILES")
    print("=" * 60)
    
    # First, fix flowchart text in all HTML files
    docs_dir = Path('./docs')
    html_files = list(docs_dir.glob('*.html'))
    
    # Also check for HTML files in root
    root_html_files = list(Path('.').glob('*.html'))
    html_files.extend(root_html_files)
    
    print(f"Found {len(html_files)} HTML files to fix:")
    for file_path in html_files:
        print(f"  - {file_path}")
    
    print("\n🎨 Fixing flowchart text visibility...")
    for file_path in html_files:
        try:
            fix_flowchart_in_file(file_path)
        except Exception as e:
            print(f"  ❌ Error processing {file_path}: {e}")
    
    # Then move files to docs folder
    print("\n📁 Organizing files...")
    move_files_to_docs()
    
    print(f"\n✅ COMPLETED ALL FIXES!")
    print("\n🎨 Flowchart fixes applied:")
    print("  - Light theme: DARK text (#1e293b) on WHITE backgrounds")
    print("  - Dark theme: LIGHT text (#f8fafc) on DARK backgrounds")
    print("  - Proper border colors for both themes")
    print("  - Enhanced visibility for all flowchart elements")
    
    print("\n📁 File organization:")
    print("  - All files moved to docs/ folder")
    print("  - README.md kept in root directory")
    print("  - Clean project structure maintained")

if __name__ == "__main__":
    main()