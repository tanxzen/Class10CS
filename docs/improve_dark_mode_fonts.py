#!/usr/bin/env python3
"""
Script to improve font colors and readability in dark mode for all HTML files
"""

import os
import re
from pathlib import Path

def get_improved_theme_css():
    """Returns the improved CSS with better dark mode font colors"""
    return """      :root {
        --primary: #2563eb;
        --primary-dark: #1e40af;
        --secondary: #f59e0b;
        --dark: #1e293b;
        --light: #f8fafc;
        --gray: #94a3b8;
        --success: #10b981;
        --warning: #f59e0b;
        --danger: #ef4444;
        --code-bg: #1e293b;
        --sidebar-width: 280px;
        --warning-border: #facc15;
        --warning-text: #854d0e;
        
        /* Light theme variables */
        --bg-primary: #f1f5f9;
        --bg-secondary: #ffffff;
        --text-primary: #1e293b;
        --text-secondary: #64748b;
        --text-muted: #94a3b8;
        --border-color: #e2e8f0;
        --shadow: rgba(0, 0, 0, 0.1);
        --card-bg: #ffffff;
        --sidebar-bg: #ffffff;
        --algorithm-bg: #2c3e50;
        --algorithm-text: #ecf0f1;
        --flowchart-bg: #f1f5f9;
        --alert-bg: #eff6ff;
        --hint-bg: #fff3cd;
        --hint-border: #ffeaa7;
        --hint-text: #856404;
        --short-answer-bg: #e8f5e8;
        --warning-bg: #fef08a;
        --code-text: #1e293b;
        --heading-color: #1e293b;
        --link-color: #2563eb;
        --link-hover: #1d4ed8;
      }

      [data-theme="dark"] {
        --bg-primary: #0f172a;
        --bg-secondary: #1e293b;
        --text-primary: #f8fafc;
        --text-secondary: #cbd5e1;
        --text-muted: #94a3b8;
        --border-color: #334155;
        --shadow: rgba(0, 0, 0, 0.3);
        --card-bg: #1e293b;
        --sidebar-bg: #1e293b;
        --algorithm-bg: #0f172a;
        --algorithm-text: #f1f5f9;
        --flowchart-bg: #334155;
        --alert-bg: #1e3a8a;
        --hint-bg: #7c2d12;
        --hint-border: #ea580c;
        --hint-text: #fed7aa;
        --short-answer-bg: #166534;
        --warning-bg: #7c2d12;
        --code-text: #e2e8f0;
        --heading-color: #f1f5f9;
        --link-color: #60a5fa;
        --link-hover: #93c5fd;
      }"""

def get_additional_dark_mode_css():
    """Returns additional CSS rules for better dark mode readability"""
    return """
      /* Enhanced typography for dark mode */
      body {
        color: var(--text-primary);
      }

      h1, h2, h3, h4, h5, h6 {
        color: var(--heading-color) !important;
      }

      p, li, td, th {
        color: var(--text-primary) !important;
      }

      .algorithm-card h3,
      .algorithm-card h4 {
        color: var(--algorithm-text) !important;
      }

      /* Code blocks */
      code, pre {
        color: var(--code-text) !important;
        background-color: var(--algorithm-bg) !important;
      }

      /* Links */
      a {
        color: var(--link-color) !important;
      }

      a:hover {
        color: var(--link-hover) !important;
      }

      /* Sidebar links */
      .sidebar a {
        color: var(--text-secondary) !important;
      }

      .sidebar a:hover,
      .sidebar a.active {
        color: var(--text-primary) !important;
      }

      /* Flowchart text */
      .flowchart-start,
      .flowchart-end,
      .flowchart-step,
      .flowchart-box,
      .flowchart-decision {
        color: var(--text-primary) !important;
      }

      /* Algorithm cards */
      .algorithm-card {
        background: var(--algorithm-bg) !important;
        color: var(--algorithm-text) !important;
      }

      /* Hints and alerts */
      .hint {
        background-color: var(--hint-bg) !important;
        border-color: var(--hint-border) !important;
        color: var(--hint-text) !important;
      }

      .alert {
        color: var(--text-primary) !important;
      }

      /* Short answer sections */
      .short-answer {
        background-color: var(--short-answer-bg) !important;
        color: var(--text-primary) !important;
      }

      /* Strong/bold text */
      strong, b {
        color: var(--text-primary) !important;
        font-weight: 600;
      }

      /* Table styling */
      table {
        color: var(--text-primary) !important;
      }

      th {
        background-color: var(--bg-secondary) !important;
        color: var(--text-primary) !important;
      }

      td {
        border-color: var(--border-color) !important;
      }

      /* Navigation */
      .nav-link {
        color: var(--text-secondary) !important;
      }

      .nav-link:hover,
      .nav-link.active {
        color: var(--text-primary) !important;
      }

      /* Buttons */
      .btn {
        color: var(--text-primary) !important;
      }

      /* Form elements */
      input, textarea, select {
        background-color: var(--bg-secondary) !important;
        color: var(--text-primary) !important;
        border-color: var(--border-color) !important;
      }

      /* Ensure all text is readable */
      * {
        transition: color 0.3s ease, background-color 0.3s ease, border-color 0.3s ease;
      }"""

def process_html_file(file_path):
    """Process a single HTML file to improve dark mode fonts"""
    print(f"Improving dark mode fonts in {file_path}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the existing theme CSS with improved version
    improved_css = get_improved_theme_css()
    additional_css = get_additional_dark_mode_css()
    
    # Find and replace the :root and [data-theme="dark"] sections
    pattern = r':root\s*{[^}]*}.*?\[data-theme="dark"\]\s*{[^}]*}'
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, improved_css, content, flags=re.DOTALL)
    
    # Add additional CSS rules before the closing </style> tag
    if '</style>' in content and 'Enhanced typography for dark mode' not in content:
        content = content.replace('</style>', additional_css + '\n    </style>')
    
    # Write the updated content back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✅ Improved {file_path}")

def main():
    """Main function to process all HTML files"""
    docs_dir = Path('./docs')
    html_files = list(docs_dir.glob('*.html'))
    
    # Also check for HTML files in root
    root_html_files = list(Path('.').glob('*.html'))
    html_files.extend(root_html_files)
    
    print(f"Found {len(html_files)} HTML files to improve:")
    for file_path in html_files:
        print(f"  - {file_path}")
    
    print("\nImproving dark mode font readability...")
    for file_path in html_files:
        try:
            process_html_file(file_path)
        except Exception as e:
            print(f"  ❌ Error processing {file_path}: {e}")
    
    print(f"\n✅ Completed improving {len(html_files)} HTML files!")
    print("\nImprovements made:")
    print("  - Enhanced text contrast in dark mode")
    print("  - Brighter primary text color (#f8fafc)")
    print("  - Improved secondary text color (#cbd5e1)")
    print("  - Better heading visibility")
    print("  - Enhanced link colors (#60a5fa)")
    print("  - Improved code block readability")
    print("  - Better hint and alert text colors")
    print("  - Enhanced flowchart text visibility")
    print("  - Stronger contrast for all UI elements")

if __name__ == "__main__":
    main()