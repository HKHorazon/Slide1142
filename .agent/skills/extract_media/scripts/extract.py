import argparse
import os
import zipfile
import shutil
from pathlib import Path

def extract_from_pptx(pptx_path, out_base_dir):
    """
    Extracts media from a single PPTX file.
    """
    try:
        # Verify file is a valid zip (PPTX is a zip)
        if not zipfile.is_zipfile(pptx_path):
            print(f"[SKIP] {os.path.basename(pptx_path)}: Not a valid PPTX (Zip) file.")
            return

        import re
        
        file_stem = Path(pptx_path).stem.strip()
        
        # Try to find L + number pattern
        match = re.search(r'L(\d+)', file_stem, re.IGNORECASE)
        if match:
            # Found chapter number, convert to int (removes leading zeros)
            chapter_num = int(match.group(1))
            target_folder_name = f"Ch{chapter_num}"
        else:
            # Fallback to original name if pattern not found
            target_folder_name = file_stem

        target_dir = os.path.join(out_base_dir, target_folder_name)
        
        # Ensure target dir exists
        os.makedirs(target_dir, exist_ok=True)

        with zipfile.ZipFile(pptx_path, 'r') as z:
            # Find all media files
            media_files = [f for f in z.namelist() if f.startswith('ppt/media/')]
            
            if not media_files:
                print(f"[INFO] {os.path.basename(pptx_path)}: No media found.")
                return

            print(f"[EXTRACT] {os.path.basename(pptx_path)} -> {len(media_files)} files")
            
            for media in media_files:
                source = z.open(media)
                filename = os.path.basename(media)
                target_path = os.path.join(target_dir, filename)
                
                with open(target_path, "wb") as target:
                    shutil.copyfileobj(source, target)

    except Exception as e:
        print(f"[ERROR] Failed to process {pptx_path}: {e}")

def process_path(path, out_dir):
    """
    Process a path (file or directory).
    """
    path_obj = Path(path)
    
    if path_obj.is_file():
        if path_obj.suffix.lower() == '.pptx':
            extract_from_pptx(str(path_obj), out_dir)
        elif path_obj.suffix.lower() == '.md':
             print(f"[INFO] Markdown file detected ({path_obj.name}). Image extraction from MD content is not yet supported. Please provide the source PPTX.")
        else:
             print(f"[SKIP] {path_obj.name}: Not a supported file type.")
             
    elif path_obj.is_dir():
        print(f"[DIR] Scanning directory: {path}")
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.lower().endswith('.pptx') and not file.startswith('~$'):
                    full_path = os.path.join(root, file)
                    extract_from_pptx(full_path, out_dir)
    else:
        print(f"[WARN] Path not found: {path}")

def main():
    parser = argparse.ArgumentParser(description="Extract media from PPTX files.")
    parser.add_argument('sources', nargs='+', help='Input files or directories')
    parser.add_argument('-o', '--out', required=True, help='Output base directory')
    
    args = parser.parse_args()
    
    out_dir = args.out
    if not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
        
    print(f"--- Starting Extraction to {out_dir} ---")
    
    for source in args.sources:
        process_path(source, out_dir)
        
    print("--- Done ---")

if __name__ == "__main__":
    main()
