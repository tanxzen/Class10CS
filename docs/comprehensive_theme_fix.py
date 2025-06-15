#!/usr/bin/env python3
"""
Comprehensive fix for all theme color issues including flowcharts
"""

import os
import re
from pathlib import Path

def get_comprehensive_theme_css():
    """Returns comprehensive CSS with proper theme colors"""
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
        
        /* Light theme variables - PROPER DARK TEXT */
        --bg-primary: #f1f5f9;
        --bg-secondary: #ffffff;
        --text-primary: #1e293b;
        --text-secondary: #475569;
        --text-muted: #64748b;
        --border-color: #e2e8f0;
        --shadow: rgba(0, 0, 0, 0.1);
        --card-bg: #ffffff;
        --sidebar-bg: #ffffff;
        --algorithm-bg: #2c3e50;
        --algorithm-text: #ffffff;
        --flowchart-bg: #f1f5f9;
        --flowchart-text: #1e293b;
        --flowchart-border: #334155;
        --alert-bg: #eff6ff;
        --hint-bg: #fff3cd;
        --hint-border: #ffeaa7;
        --hint-text: #92400e;
        --short-answer-bg: #e8f5e8;
        --warning-bg: #fef08a;
        --code-text: #1e293b;
        --heading-color: #1e293b;
        --link-color: #2563eb;
        --link-hover: #1d4ed8;
      }

      [data-theme="dark"] {
        /* Dark theme variables - PROPER LIGHT TEXT */
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
        --algorithm-text: #f8fafc;
        --flowchart-bg: #334155;
        --flowchart-text: #f8fafc;
        --flowchart-border: #64748b;
        --alert-bg: #1e3a8a;
        --hint-bg: #7c2d12;
        --hint-border: #ea580c;
        --hint-text: #fed7aa;
        --short-answer-bg: #166534;
        --warning-bg: #7c2d12;
        --code-text: #f8fafc;
        --heading-color: #f8fafc;
        --link-color: #60a5fa;
        --link-hover: #93c5fd;
      }"""

def get_comprehensive_typography_css():
    """Returns comprehensive typography CSS including flowcharts"""
    return """
      /* COMPREHENSIVE TYPOGRAPHY FIX INCLUDING FLOWCHARTS */
      
      /* Base body styling */
      body {
        color: var(--text-primary) !important;
        background-color: var(--bg-primary) !important;
        transition: all 0.3s ease !important;
      }

      /* ALL HEADINGS */
      h1, h2, h3, h4, h5, h6 {
        color: var(--heading-color) !important;
        font-weight: 600 !important;
      }

      /* ALL TEXT ELEMENTS */
      p, li, td, th, span, div, label, strong, b, em, i {
        color: var(--text-primary) !important;
      }

      /* ALGORITHM CARDS - SPECIAL HANDLING */
      .algorithm-card {
        background: var(--algorithm-bg) !important;
        color: var(--algorithm-text) !important;
      }

      .algorithm-card *,
      .algorithm-card h1,
      .algorithm-card h2,
      .algorithm-card h3,
      .algorithm-card h4,
      .algorithm-card h5,
      .algorithm-card h6,
      .algorithm-card p,
      .algorithm-card li,
      .algorithm-card span,
      .algorithm-card div,
      .algorithm-card strong,
      .algorithm-card b,
      .algorithm-card em,
      .algorithm-card i {
        color: var(--algorithm-text) !important;
      }

      /* CODE BLOCKS - CRITICAL FIX */
      code, pre {
        font-family: 'Courier New', 'Monaco', 'Menlo', monospace !important;
        padding: 4px 8px !important;
        border-radius: 4px !important;
      }

      /* Algorithm code blocks */
      .algorithm-card code,
      .algorithm-card pre {
        color: var(--algorithm-text) !important;
        background-color: var(--algorithm-bg) !important;
      }

      /* Regular code blocks */
      code:not(.algorithm-card code),
      pre:not(.algorithm-card pre) {
        color: var(--code-text) !important;
        background-color: var(--bg-secondary) !important;
        border: 1px solid var(--border-color) !important;
      }

      /* FLOWCHART ELEMENTS - COMPREHENSIVE FIX */
      .flowchart,
      .flowchart-container {
        background-color: var(--flowchart-bg) !important;
        color: var(--flowchart-text) !important;
      }

      .flowchart-start,
      .flowchart-end {
        color: var(--flowchart-text) !important;
        border: 2px solid var(--flowchart-border) !important;
        background-color: var(--card-bg) !important;
        border-radius: 50% !important;
        width: 40px !important;
        height: 40px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-weight: bold !important;
      }

      .flowchart-step,
      .flowchart-box {
        color: var(--flowchart-text) !important;
        border: 2px solid var(--flowchart-border) !important;
        background-color: var(--card-bg) !important;
        border-radius: 8px !important;
        padding: 12px 16px !important;
        text-align: center !important;
        font-weight: 500 !important;
      }

      .flowchart-decision {
        color: var(--flowchart-text) !important;
        border: 2px solid var(--flowchart-border) !important;
        background-color: var(--card-bg) !important;
        transform: rotate(45deg) !important;
        width: 120px !important;
        height: 120px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-weight: 500 !important;
      }

      .flowchart-decision > div {
        transform: rotate(-45deg) !important;
        text-align: center !important;
        color: var(--flowchart-text) !important;
      }

      .flowchart-branch {
        color: var(--flowchart-text) !important;
        font-weight: 600 !important;
        font-size: 14px !important;
      }

      /* Flowchart arrows and lines */
      .flowchart-arrow,
      .flowchart-line {
        border-color: var(--flowchart-border) !important;
        background-color: var(--flowchart-border) !important;
      }

      /* LINKS */
      a {
        color: var(--link-color) !important;
        text-decoration: none !important;
      }

      a:hover {
        color: var(--link-hover) !important;
        text-decoration: underline !important;
      }

      /* SIDEBAR */
      .sidebar {
        background-color: var(--sidebar-bg) !important;
        color: var(--text-primary) !important;
        border-right: 1px solid var(--border-color) !important;
      }

      .sidebar * {
        color: var(--text-secondary) !important;
      }

      .sidebar a {
        color: var(--text-secondary) !important;
      }

      .sidebar a:hover,
      .sidebar a.active {
        color: var(--text-primary) !important;
        background-color: var(--bg-primary) !important;
      }

      /* CARDS AND CONTAINERS */
      .card, .container, .main-content {
        background-color: var(--card-bg) !important;
        color: var(--text-primary) !important;
        border-color: var(--border-color) !important;
      }

      /* HINTS AND ALERTS */
      .hint {
        background-color: var(--hint-bg) !important;
        border-color: var(--hint-border) !important;
        color: var(--hint-text) !important;
      }

      .alert {
        background-color: var(--alert-bg) !important;
        color: var(--text-primary) !important;
      }

      /* SHORT ANSWERS */
      .short-answer {
        background-color: var(--short-answer-bg) !important;
        color: var(--text-primary) !important;
      }

      /* TABLES */
      table {
        color: var(--text-primary) !important;
        border-color: var(--border-color) !important;
      }

      th {
        background-color: var(--bg-secondary) !important;
        color: var(--text-primary) !important;
        font-weight: 600 !important;
      }

      td {
        border-color: var(--border-color) !important;
        color: var(--text-primary) !important;
      }

      /* FORM ELEMENTS */
      input, textarea, select, button {
        background-color: var(--bg-secondary) !important;
        color: var(--text-primary) !important;
        border-color: var(--border-color) !important;
      }

      /* NAVIGATION */
      .nav-link {
        color: var(--text-secondary) !important;
      }

      .nav-link:hover,
      .nav-link.active {
        color: var(--text-primary) !important;
      }

      /* OVERRIDE ANY REMAINING ISSUES */
      [style*="color: black"],
      [style*="color: #000"],
      [style*="color: #000000"] {
        color: var(--text-primary) !important;
      }

      [style*="color: white"],
      [style*="color: #fff"],
      [style*="color: #ffffff"] {
        color: var(--text-primary) !important;
      }

      /* SMOOTH TRANSITIONS */
      * {
        transition: color 0.3s ease, background-color 0.3s ease, border-color 0.3s ease !important;
      }"""

def process_html_file(file_path):
    """Process a single HTML file with comprehensive theme fix"""
    print(f"Applying comprehensive theme fix to {file_path}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get the comprehensive CSS
    theme_css = get_comprehensive_theme_css()
    typography_css = get_comprehensive_typography_css()
    
    # Replace the entire CSS theme section
    # Find the pattern from :root to the end of [data-theme="dark"]
    pattern = r':root\s*{.*?\[data-theme="dark"\]\s*{[^}]*}'
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, theme_css, content, flags=re.DOTALL)
    
    # Remove any existing typography fixes and add the new comprehensive one
    # Remove existing typography sections
    typography_patterns = [
        r'/\* Enhanced typography.*?/\* Ensure all text is readable.*?\*/',
        r'/\* Fix algorithm code blocks.*?/\* Ensure algorithm cards have proper text colors.*?\*/',
        r'/\* COMPREHENSIVE TYPOGRAPHY FIX.*?/\* SMOOTH TRANSITIONS.*?\*/'
    ]
    
    for pattern in typography_patterns:
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # Add the comprehensive typography CSS before closing </style>
    if '</style>' in content:
        content = content.replace('</style>', typography_css + '\n    </style>')
    
    # Write the updated content back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✅ Applied comprehensive fix to {file_path}")

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
    
    print("\nApplying comprehensive theme fixes...")
    for file_path in html_files:
        try:
            process_html_file(file_path)
        except Exception as e:
            print(f"  ❌ Error processing {file_path}: {e}")
    
    print(f"\n✅ Completed comprehensive theme fix for {len(html_files)} HTML files!")
    print("\nFixes applied:")
    print("  🌞 LIGHT THEME:")
    print("    - Dark text (#1e293b) on light backgrounds")
    print("    - Algorithm code: WHITE text on DARK BLUE background")
    print("    - Regular code: DARK text on light background")
    print("    - Flowcharts: DARK text on light elements")
    print("    - All headings and text properly dark")
    print("  🌙 DARK THEME:")
    print("    - Light text (#f8fafc) on dark backgrounds")
    print("    - Algorithm code: WHITE text on VERY DARK background")
    print("    - Regular code: LIGHT text on dark background")
    print("    - Flowcharts: LIGHT text on dark elements")
    print("    - All headings and text properly light")
    print("  📊 FLOWCHARTS:")
    print("    - Proper contrast for start/end circles")
    print("    - Clear text in process boxes")
    print("    - Readable decision diamonds")
    print("    - Visible branch labels")
    print("  ⚡ COMPREHENSIVE:")
    print("    - Fixed ALL text elements with !important declarations")
    print("    - Proper contrast ratios for accessibility")
    print("    - Smooth transitions between themes")
    print("    - Override any conflicting inline styles")

if __name__ == "__main__":
    main()