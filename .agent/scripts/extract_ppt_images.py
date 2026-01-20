import os
import zipfile
import shutil
from pathlib import Path
import argparse

def extract_images_from_pptx(pptx_path, output_dir):
    """
    Extracts images from a pptx file (which is a zip archive)
    into the output directory.
    """
    try:
        if not zipfile.is_zipfile(pptx_path):
            print(f"Skipping {pptx_path}: Not a valid zip file")
            return

        with zipfile.ZipFile(pptx_path, 'r') as z:
            # Filter for media files in ppt/media/
            media_files = [f for f in z.namelist() if f.startswith('ppt/media/')]
            
            if not media_files:
                print(f"No media found in {pptx_path}")
                return

            # Create output directory for this pptx
            pptx_name = Path(pptx_path).stem
            target_folder = os.path.join(output_dir, pptx_name)
            os.makedirs(target_folder, exist_ok=True)

            print(f"Extracting {len(media_files)} images from {pptx_name}...")
            
            for file in media_files:
                # Extract file
                source = z.open(file)
                filename = os.path.basename(file)
                target_path = os.path.join(target_folder, filename)
                
                with open(target_path, "wb") as target:
                    shutil.copyfileobj(source, target)
                    
    except Exception as e:
        print(f"Error processing {pptx_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Extract images from PPTX files.")
    parser.add_argument("source_dir", help="Directory containing .pptx files")
    parser.add_argument("dest_dir", help="Directory to save extracted images")
    args = parser.parse_args()

    source_dir = args.source_dir
    dest_dir = args.dest_dir

    # Ensure destination directory exists
    if not os.path.exists(dest_dir):
        print(f"Creating destination directory: {dest_dir}")
        os.makedirs(dest_dir)

    # Walk through source directory
    if not os.path.exists(source_dir):
        print(f"Source directory not found: {source_dir}")
        return

    files_processed = 0
    for filename in os.listdir(source_dir):
        if filename.lower().endswith(('.pptx', '.ppt')): 
            if filename.lower().endswith('.ppt'):
                print(f"Skipping {filename}: .ppt format not supported by this script (OLE format).")
                continue
                
            file_path = os.path.join(source_dir, filename)
            extract_images_from_pptx(file_path, dest_dir)
            files_processed += 1

    print(f"Done. Processed {files_processed} files.")

if __name__ == "__main__":
    main()
