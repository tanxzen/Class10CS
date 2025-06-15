#!/usr/bin/env python3
"""
Script to add dark/light theme switcher to all HTML files in the docs directory
"""

import os
import re
from pathlib import Path

def get_theme_css():
    """Returns the CSS for theme variables and switcher"""
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
        --short-answer-bg: #e8f5e8;
        --warning-bg: #fef08a;
      }

      [data-theme="dark"] {
        --bg-primary: #0f172a;
        --bg-secondary: #1e293b;
        --text-primary: #f1f5f9;
        --text-secondary: #94a3b8;
        --border-color: #334155;
        --shadow: rgba(0, 0, 0, 0.3);
        --card-bg: #1e293b;
        --sidebar-bg: #1e293b;
        --algorithm-bg: #0f172a;
        --algorithm-text: #e2e8f0;
        --flowchart-bg: #334155;
        --alert-bg: #1e3a8a;
        --hint-bg: #451a03;
        --hint-border: #92400e;
        --short-answer-bg: #14532d;
        --warning-bg: #451a03;
      }

      /* Theme switcher styles */
      .theme-switcher {
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 1000;
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 25px;
        padding: 8px;
        box-shadow: 0 2px 10px var(--shadow);
        display: flex;
        align-items: center;
        gap: 8px;
        transition: all 0.3s ease;
      }

      .theme-toggle {
        background: none;
        border: none;
        cursor: pointer;
        padding: 8px 12px;
        border-radius: 20px;
        display: flex;
        align-items: center;
        gap: 6px;
        font-size: 14px;
        font-weight: 500;
        transition: all 0.3s ease;
        color: var(--text-secondary);
      }

      .theme-toggle:hover {
        background: var(--bg-primary);
        color: var(--text-primary);
      }

      .theme-toggle.active {
        background: var(--primary);
        color: white;
      }

      .theme-toggle i {
        font-size: 16px;
      }"""

def get_theme_js():
    """Returns the JavaScript for theme switching functionality"""
    return """      // Theme switching functionality
      const themeToggle = {
        init() {
          this.createSwitcher();
          this.loadTheme();
          this.bindEvents();
        },

        createSwitcher() {
          const switcher = document.createElement('div');
          switcher.className = 'theme-switcher';
          switcher.innerHTML = `
            <button class="theme-toggle" data-theme="light">
              <i class="fas fa-sun"></i>
              <span>Light</span>
            </button>
            <button class="theme-toggle" data-theme="dark">
              <i class="fas fa-moon"></i>
              <span>Dark</span>
            </button>
          `;
          document.body.appendChild(switcher);
        },

        loadTheme() {
          const savedTheme = localStorage.getItem('theme') || 'light';
          this.setTheme(savedTheme);
        },

        setTheme(theme) {
          document.documentElement.setAttribute('data-theme', theme);
          localStorage.setItem('theme', theme);
          
          // Update active button
          document.querySelectorAll('.theme-toggle').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.theme === theme);
          });
        },

        bindEvents() {
          document.addEventListener('click', (e) => {
            if (e.target.closest('.theme-toggle')) {
              const theme = e.target.closest('.theme-toggle').dataset.theme;
              this.setTheme(theme);
            }
          });
        }
      };

      // Initialize theme switcher when DOM is loaded
      document.addEventListener('DOMContentLoaded', () => {
        themeToggle.init();
      });"""

def update_css_variables(content):
    """Update CSS to use theme variables"""
    # Replace common background colors
    content = re.sub(r'background-color:\s*#f1f5f9;', 'background-color: var(--bg-primary);', content)
    content = re.sub(r'background-color:\s*white;', 'background-color: var(--card-bg);', content)
    content = re.sub(r'background-color:\s*#ffffff;', 'background-color: var(--card-bg);', content)
    
    # Replace text colors
    content = re.sub(r'color:\s*var\(--dark\);', 'color: var(--text-primary);', content)
    content = re.sub(r'color:\s*#1e293b;', 'color: var(--text-primary);', content)
    
    # Replace border colors
    content = re.sub(r'border.*?#e2e8f0', lambda m: m.group(0).replace('#e2e8f0', 'var(--border-color)'), content)
    content = re.sub(r'border-bottom:\s*1px solid #e2e8f0;', 'border-bottom: 1px solid var(--border-color);', content)
    
    # Replace box shadows
    content = re.sub(r'box-shadow:\s*[^;]*rgba\(0,\s*0,\s*0,\s*0\.1\)[^;]*;', 'box-shadow: 0 4px 6px -1px var(--shadow);', content)
    
    # Add transition to body
    if 'body {' in content and 'transition:' not in content:
        content = re.sub(r'(body\s*{[^}]*)', r'\1\n        transition: background-color 0.3s ease, color 0.3s ease;', content)
    
    return content

def process_html_file(file_path):
    """Process a single HTML file to add theme switcher"""
    print(f"Processing {file_path}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if theme switcher already exists
    if 'theme-switcher' in content:
        print(f"  Theme switcher already exists in {file_path}, skipping...")
        return
    
    # Replace the :root CSS variables section
    root_pattern = r':root\s*{[^}]*}'
    theme_css = get_theme_css()
    
    if re.search(root_pattern, content):
        content = re.sub(root_pattern, theme_css, content, flags=re.DOTALL)
    else:
        # If no :root found, add it after the first style tag
        style_pattern = r'(<style[^>]*>)'
        if re.search(style_pattern, content):
            content = re.sub(style_pattern, r'\1\n' + theme_css + '\n', content)
    
    # Update CSS to use theme variables
    content = update_css_variables(content)
    
    # Add theme JavaScript before closing </body> tag
    theme_js = get_theme_js()
    if '</body>' in content:
        content = content.replace('</body>', f'    <script>\n{theme_js}\n    </script>\n  </body>')
    
    # Write the updated content back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✅ Updated {file_path}")

def main():
    """Main function to process all HTML files"""
    docs_dir = Path('./docs')
    html_files = list(docs_dir.glob('*.html'))
    
    # Also check for HTML files in root
    root_html_files = list(Path('.').glob('*.html'))
    html_files.extend(root_html_files)
    
    print(f"Found {len(html_files)} HTML files to process:")
    for file_path in html_files:
        print(f"  - {file_path}")
    
    print("\nProcessing files...")
    for file_path in html_files:
        try:
            process_html_file(file_path)
        except Exception as e:
            print(f"  ❌ Error processing {file_path}: {e}")
    
    print(f"\n✅ Completed processing {len(html_files)} HTML files!")
    print("\nFeatures added:")
    print("  - Light/Dark theme switcher in top-right corner")
    print("  - Persistent theme selection (saved in localStorage)")
    print("  - Smooth transitions between themes")
    print("  - Updated CSS variables for consistent theming")

if __name__ == "__main__":
    main()