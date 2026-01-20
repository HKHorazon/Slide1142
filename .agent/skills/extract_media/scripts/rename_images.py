import os
import re
import argparse
from pathlib import Path

# Mapping for Subject Names
SUBJECT_MAPPING = {
    "CSharp程式": "CSharp",
    "AI2": "AI2",
    "Web": "Web",
    "Mobile": "Mobile",
    "General": "General",
    "Project_112音樂遊戲": "Project_112"
}

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)]

def rename_images_in_dir(root_dir):
    """
    Renames images in root_dir/Subject/ChX/ to Subject_ChXX_YY.ext
    """
    root_path = Path(root_dir)
    if not root_path.exists():
        print(f"Directory not found: {root_dir}")
        return

    # Iterate over Subject Directories (e.g., CSharp程式, AI2)
    for subject_dir in root_path.iterdir():
        if not subject_dir.is_dir():
            continue
            
        subject_name_raw = subject_dir.name
        # Apply mapping or use raw name (sanitized)
        subject_prefix = SUBJECT_MAPPING.get(subject_name_raw, subject_name_raw)
        
        print(f"Processing Subject: {subject_name_raw} -> Prefix: {subject_prefix}")

        # Iterate over Chapter Directories (e.g., Ch1, Ch0)
        for chapter_dir in subject_dir.iterdir():
            if not chapter_dir.is_dir():
                continue
            
            # Match ChX pattern
            match = re.match(r'^Ch(\d+)$', chapter_dir.name, re.IGNORECASE)
            if not match:
                # Iterate recursive subdirs? Or skip? 
                # According to plan, we only process ChX folders.
                # But let's check if there are images directly or non-conforming folders.
                # For safety, let's only process ChX folders as per request.
                continue
            
            chapter_num = int(match.group(1))
            
            # Get all images in this folder
            images = []
            file_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp', '.emf', '.wmf'}
            
            for file in chapter_dir.iterdir():
                if file.is_file() and file.suffix.lower() in file_extensions:
                    images.append(file)
            
            # Sort images to maintain order (image1, image2...)
            images.sort(key=lambda x: natural_sort_key(x.name))
            
            # Rename loop
            for idx, img_path in enumerate(images, 1):
                extension = img_path.suffix.lower()
                # Format: Subject_ChXX_YY.ext
                new_filename = f"{subject_prefix}_Ch{chapter_num:02d}_{idx:02d}{extension}"
                new_path = chapter_dir / new_filename
                
                if img_path.name == new_filename:
                    continue # Already renamed
                    
                try:
                    # Rename
                    img_path.rename(new_path)
                    # print(f"  [RENAME] {chapter_dir.name}/{img_path.name} -> {new_filename}")
                except Exception as e:
                    print(f"  [ERROR] Failed to rename {img_path}: {e}")
            
            print(f"  Finished {chapter_dir.name}: Renamed {len(images)} images.")

def main():
    parser = argparse.ArgumentParser(description="Rename extracted images to standard format.")
    parser.add_argument('root_dir', help='Root IMAGE directory')
    
    args = parser.parse_args()
    rename_images_in_dir(args.root_dir)

if __name__ == "__main__":
    main()
