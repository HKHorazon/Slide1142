import argparse
import os
import subprocess
import sys

# Configuration
INPUT_ROOT_DIR = 'MD'
OUTPUT_ROOT_DIR = 'PDF'
DEFAULT_THEME = 'HoraStyle.css'

def get_output_path(md_file_path):
    """Calculates the output PDF path based on the input MD path."""
    # Normalize paths
    md_file_path = os.path.normpath(md_file_path)
    
    # Check if file is inside the INPUT_ROOT_DIR to maintain structure
    if INPUT_ROOT_DIR in md_file_path:
        try:
             # Try to get path relative to MD root to mirror structure in PDF
            rel_path = os.path.relpath(md_file_path, INPUT_ROOT_DIR)
        except ValueError:
            rel_path = os.path.basename(md_file_path)
    else:
        # If outside MD dir, just use the basename
        rel_path = os.path.basename(md_file_path)

    # Construct output path
    # e.g. PDF/Chapter1/Slide.pdf
    base_name = os.path.splitext(rel_path)[0]
    output_path = os.path.join(OUTPUT_ROOT_DIR, base_name + '.pdf')
    return output_path

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export Marp slides to PDF.")
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-f", "--file", help="Export a specific Markdown file")
    group.add_argument("-d", "--dir", help="Export all Markdown files in a specific directory")
    group.add_argument("-a", "--all", action="store_true", help="Export all files in 'MD' directory (Default)")

    args = parser.parse_args()

    if args.file:
        export_file(args.file)
    elif args.dir:
        export_folder(args.dir)
    else:
        # Default behavior checks if default dir exists
        if os.path.exists(INPUT_ROOT_DIR):
            export_all()
        else:
            print(f"Error: Default input directory '{INPUT_ROOT_DIR}' not found.")