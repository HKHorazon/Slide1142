import os
import argparse
import glob
import re
import json

# Configuration
INPUT_ROOT_DIR = 'MD'
TEMPLATE_PATH = os.path.join('.agent', 'skills', 'slide', 'reference', 'course_map_template.md')

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
    return "TBD"

def get_course_name_from_settings(settings_path):
    """Reads ChapterName from settings.json."""
    if os.path.exists(settings_path):
        try:
            with open(settings_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get("ChapterName", "Course Name")
        except:
            pass
    return "Course Name"

def generate_map(course_dir):
    full_course_path = os.path.join(INPUT_ROOT_DIR, course_dir)
    if not os.path.exists(full_course_path):
        print(f"Error: Directory {full_course_path} does not exist.")
        return

    print(f"Generating Course Map for: {course_dir}")

    # 1. Get Course Name & MapLock
    settings_path = os.path.join(full_course_path, 'settings.json')
    
    settings_data = {}
    if os.path.exists(settings_path):
        try:
            with open(settings_path, 'r', encoding='utf-8') as f:
                settings_data = json.load(f)
        except:
            pass
            
    if settings_data.get("MapLock", False):
        print(f"Skipping {course_dir}: MapLock is enabled.")
        return

    course_name = settings_data.get("ChapterName", "Course Name")

    # 2. Scan Markdown files
    md_files = glob.glob(os.path.join(full_course_path, '*.md'))
    md_files = sorted(md_files)
    
    # Filter files
    valid_files = []
    for f in md_files:
        filename = os.path.basename(f)
        # Skip settings, map itself, and maybe intro/00 if needed (but currently we map them to weeks)
        if filename.lower() == 'settings.json': continue
        if '_map.md' in filename.lower(): continue
        
        valid_files.append(f)

    # 3. Extract Titles
    titles = []
    for f in valid_files:
        title = get_slide_title(f)
        titles.append(title)
        
    print(f"Found {len(titles)} chapters.")

    # 4. Map to Weeks
    # Mapping logic: 
    # Valid files are sequential. 
    # We simply take the first N files and fill the slots.
    # W2-W8 (7 slots), W10-W16 (7 slots) -> Total 14 slots available.
    
    placeholders = {}
    
    # Fill W2-W8
    for i in range(7):
        week_num = i + 2
        key = f"{{WEEK_{week_num:02d}}}"
        if i < len(titles):
            placeholders[key] = titles[i]
        else:
            placeholders[key] = "(自行安排進度)"
            
    # Fill W10-W16
    for i in range(7):
        week_num = i + 10
        idx = i + 7 # Start after the first 7
        key = f"{{WEEK_{week_num}}}"
        if idx < len(titles):
            placeholders[key] = titles[idx]
        else:
            placeholders[key] = "(自行安排進度)"

    # 5. Read Template
    if not os.path.exists(TEMPLATE_PATH):
        print(f"Error: Template not found at {TEMPLATE_PATH}")
        return

    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # 6. Replace Placeholders
    content = content.replace("{COURSE_NAME}", course_name)
    content = content.replace("{SEMESTER}", "114-2") # Hardcoded or passed arg

    for key, value in placeholders.items():
        content = content.replace(key, value)
        
    # 7. Write Output
    # Output file: {CourseDir}_00_Map.md
    # Try to match the prefix of files in that dir (e.g. Mobile_00_Map.md)
    # Heuristic: Take the first file's prefix before underscore
    output_filename = "Course_00_Map.md"
    if valid_files:
        first_base = os.path.basename(valid_files[0])
        if '_' in first_base:
            prefix = first_base.split('_')[0]
            output_filename = f"{prefix}_00_Map.md"
            
    output_path = os.path.join(full_course_path, output_filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Successfully generated: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Course Map Markdown.")
    parser.add_argument("-d", "--dir", required=True, help="Target Course Directory relative to MD/")
    args = parser.parse_args()

    generate_map(args.dir)
