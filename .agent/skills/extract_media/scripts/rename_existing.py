import os
import re
import argparse
from pathlib import Path

def rename_folders(target_dir):
    """
    Renames subdirectories in target_dir from '...Lxx...' to 'ChX'.
    """
    if not os.path.exists(target_dir):
        print(f"Directory not found: {target_dir}")
        return

    print(f"Scanning {target_dir}...")
    
    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)
        
        if os.path.isdir(item_path):
            # Regex to find L + number
            match = re.search(r'L(\d+)', item, re.IGNORECASE)
            
            if match:
                chapter_num = int(match.group(1))
                new_name = f"Ch{chapter_num}"
                new_path = os.path.join(target_dir, new_name)
                
                if item != new_name:
                    try:
                        # Handle collision if target exists (merge or skip?)
                        # For now, if target exists, we just move contents or warn?
                        # Simple rename first.
                        if os.path.exists(new_path):
                            print(f"[WARN] Target {new_name} already exists. Merging contents...")
                            # Move files from old to new
                            for file in os.listdir(item_path):
                                src_file = os.path.join(item_path, file)
                                dst_file = os.path.join(new_path, file)
                                if not os.path.exists(dst_file):
                                    os.rename(src_file, dst_file)
                            # Remove old empty dir
                            os.rmdir(item_path)
                            print(f"[MERGED] {item} -> {new_name}")
                        else:
                            os.rename(item_path, new_path)
                            print(f"[RENAME] {item} -> {new_name}")
                    except Exception as e:
                        print(f"[ERROR] Could not rename {item}: {e}")
            else:
                 print(f"[SKIP] {item}: No 'L number' pattern found.")

def main():
    parser = argparse.ArgumentParser(description="Rename folders to ChX format.")
    parser.add_argument('dirs', nargs='+', help='Target directories to scan')
    
    args = parser.parse_args()
    
    for d in args.dirs:
        rename_folders(d)

if __name__ == "__main__":
    main()
