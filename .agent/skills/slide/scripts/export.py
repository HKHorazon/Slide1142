import argparse
import os
import subprocess
import sys
import re

# Configuration
INPUT_ROOT_DIR = 'MD'
OUTPUT_ROOT_DIR = 'PDF'
DISPLAY_DIR = 'display'
DEFAULT_THEME = 'HoraStyle.css'

def get_output_path(md_file_path):
    """Calculates the output PDF path based on the input MD path."""
    md_file_path = os.path.normpath(md_file_path)
    
    if INPUT_ROOT_DIR in md_file_path:
        try:
            rel_path = os.path.relpath(md_file_path, INPUT_ROOT_DIR)
        except ValueError:
            rel_path = os.path.basename(md_file_path)
    else:
        rel_path = os.path.basename(md_file_path)

    base_name = os.path.splitext(rel_path)[0]
    output_path = os.path.join(OUTPUT_ROOT_DIR, base_name + '.pdf')
    return output_path

def get_slide_title(md_file_path):
    """Extracts the first H1 title from the Markdown file."""
    try:
        with open(md_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                stripped = line.strip()
                if stripped.startswith('# '):
                    return stripped[2:].strip()
    except Exception as e:
        print(f"Warning: Could not read title from {md_file_path}: {e}")
    return None

def format_display_name(category, filename, title):
    """Formats the display name: {Course}_Ch{Num}_{Title}"""
    name_without_ext = os.path.splitext(filename)[0]
    
    # Try to extract chapter number from filename (e.g. Mobile_01 -> 01)
    # Looking for pattern: anything_DIGITS
    match = re.search(r'_(\w+)$', name_without_ext)
    if match:
        chapter_part = match.group(1)
    else:
        chapter_part = name_without_ext

    # If we have a title, use the full format
    if title:
        # Avoid duplicating the chapter info if it's already in the title roughly
        # But per user request: {Course}_Ch{Chapter}_{ChapterName}
        # Let's stick to the requested format strictly.
        
        # Clean category name (remove spaces or special chars if needed, but keeping as is for now)
        display = f"{category}_Ch{chapter_part}_{title}"
    else:
        # Fallback if no title found
        display = name_without_ext
        
    return display

def export_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return

    output_path = get_output_path(file_path)
    output_dir = os.path.dirname(output_path)
    
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    print(f"[Exporting] {file_path} -> {output_path}")

    command = [
        'marp', file_path,
        '--pdf',
        '--allow-local-files',
        '--theme-set', DEFAULT_THEME,
        '-o', output_path
    ]

    try:
        subprocess.run(command, check=True)
        print(f"[Done] Success!")
    except subprocess.CalledProcessError as e:
        print(f"[Error] Failed to export {file_path}: {e}")

def export_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"Error: Folder not found: {folder_path}")
        return
        
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                export_file(full_path)

def export_all():
    print(f"Exporting all files from {INPUT_ROOT_DIR}...")
    export_folder(INPUT_ROOT_DIR)

def generate_index_html():
    """Generates an index.html in the DISPLAY_DIR listing all PDFs."""
    print(f"Generating index.html in {DISPLAY_DIR}...")
    
    if not os.path.exists(OUTPUT_ROOT_DIR):
        print(f"Warning: PDF directory {OUTPUT_ROOT_DIR} does not exist.")
        return

    os.makedirs(DISPLAY_DIR, exist_ok=True)
    
    # Data structure: { "Category": [ ("FormattedName", "RelativeLink"), ... ] }
    pdf_files = {}

    for root, dirs, files in os.walk(OUTPUT_ROOT_DIR):
        for file in files:
            if file.endswith('.pdf'):
                full_path = os.path.join(root, file)
                
                # Calculate paths
                display_abs = os.path.abspath(DISPLAY_DIR)
                pdf_abs = os.path.abspath(full_path)
                try:
                    rel_link = os.path.relpath(pdf_abs, display_abs)
                    rel_link = rel_link.replace(os.sep, '/')
                except ValueError:
                    rel_link = pdf_abs
                
                # Determine Category
                rel_root = os.path.relpath(root, OUTPUT_ROOT_DIR)
                if rel_root == '.':
                    category = "Uncategorized"
                else:
                    category = rel_root
                
                # Find corresponding MD file to get title
                # Mapping mechanism: PDF/Cat/File.pdf -> MD/Cat/File.md
                # This assumes structure is mirrored exactly.
                rel_from_pdf_root = os.path.relpath(full_path, OUTPUT_ROOT_DIR)
                base_name_no_ext = os.path.splitext(rel_from_pdf_root)[0]
                md_guess_path = os.path.join(INPUT_ROOT_DIR, base_name_no_ext + '.md')
                
                if os.path.exists(md_guess_path):
                    title = get_slide_title(md_guess_path)
                else:
                    title = None
                    
                formatted_name = format_display_name(category, file, title)

                if category not in pdf_files:
                    pdf_files[category] = []
                
                pdf_files[category].append((formatted_name, rel_link))

    # Generate HTML content
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course Slides Index</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f0f2f5; padding: 40px; color: #1e1b4b; margin: 0; }}
        .container {{ max-width: 900px; margin: 0 auto; }}
        h1 {{ text-align: center; color: #581c87; margin-bottom: 40px; font-weight: 700; }}
        
        .category {{ background: white; margin-bottom: 20px; border-radius: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); overflow: hidden; }}
        
        details > summary {{
            padding: 20px 25px;
            cursor: pointer;
            background-color: #fff;
            list-style: none; /* Hide default triangle */
            position: relative;
            transition: background-color 0.2s;
        }}
        
        details > summary:hover {{
            background-color: #f8fafc;
        }}

        details > summary::-webkit-details-marker {{
            display: none;
        }}

        details > summary h2 {{ 
            border-bottom: none; 
            margin: 0; 
            font-size: 1.3em; 
            color: #1e1b4b; 
            display: inline-block;
        }}

        /* Custom arrow */
        details > summary::after {{
            content: '+';
            position: absolute;
            right: 25px;
            font-size: 1.5em;
            color: #581c87;
            font-weight: bold;
        }}

        details[open] > summary::after {{
            content: '-';
        }}
        
        details[open] > summary {{
            border-bottom: 1px solid #e2e8f0;
        }}

        .file-list {{ list-style: none; padding: 15px 25px; margin: 0; background-color: #fff; }}
        .file-item {{ margin: 8px 0; }}
        .file-link {{ display: block; padding: 10px 15px; text-decoration: none; color: #334155; border-radius: 6px; transition: all 0.2s; }}
        .file-link:hover {{ background: #eff6ff; color: #581c87; padding-left: 20px; }}
        
        .footer {{ text-align: center; margin-top: 50px; color: #64748b; font-size: 0.9em; }}
        
        @media (max-width: 600px) {{
            body {{ padding: 20px; }}
            h1 {{ font-size: 1.8em; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📚 Course Slides Index</h1>
"""

    sorted_categories = sorted(pdf_files.keys())
    
    for category in sorted_categories:
        html_content += f'        <div class="category">\n            <details>\n                <summary><h2>{category}</h2></summary>\n                <ul class="file-list">\n'
        for name, link in sorted(pdf_files[category]):
            html_content += f'                    <li class="file-item"><a class="file-link" href="{link}" target="_blank">{name}</a></li>\n'
        html_content += '                </ul>\n            </details>\n        </div>\n'

    html_content += """        <div class="footer">
            <p>Generated by Antigravity Slide Skill</p>
        </div>
    </div>
</body>
</html>"""

    index_path = os.path.join(DISPLAY_DIR, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"[Index] details written to {index_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export Marp slides to PDF.")
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-f", "--file", help="Export a specific Markdown file")
    group.add_argument("-d", "--dir", help="Export all Markdown files in a specific directory")
    group.add_argument("-a", "--all", action="store_true", help="Export all files in 'MD' directory (Default)")
    # New flag to only regenerate index
    group.add_argument("-i", "--index", action="store_true", help="Only regenerate the index HTML")

    args = parser.parse_args()

    if args.index:
        generate_index_html()
    else:
        if args.file:
            export_file(args.file)
        elif args.dir:
            export_folder(args.dir)
        else:
            if os.path.exists(INPUT_ROOT_DIR):
                export_all()
            else:
                print(f"Error: Default input directory '{INPUT_ROOT_DIR}' not found.")
        
        # Always generate index after processing slides
        generate_index_html()