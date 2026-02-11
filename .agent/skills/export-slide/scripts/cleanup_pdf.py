import os
import argparse
from pathlib import Path

# Configuration
MD_ROOT = 'MD'
PDF_ROOT = 'PDF'

def cleanup_orphaned_pdfs(pdf_root, md_root, dry_run=False):
    """
    Removes PDF files in pdf_root that do not have a corresponding MD file in md_root.
    """
    pdf_path_obj = Path(pdf_root)
    md_path_obj = Path(md_root)

    if not pdf_path_obj.exists():
        print(f"PDF directory not found: {pdf_root}")
        return

    print(f"Scanning {pdf_root} for orphaned PDFs (Source: {md_root})...")
    
    deleted_count = 0
    
    for pdf_file in pdf_path_obj.rglob('*.pdf'):
        # Get relative path from PDF root
        rel_path = pdf_file.relative_to(pdf_path_obj)
        
        # Construct expected MD path
        # PDF/Folder/File.pdf -> MD/Folder/File.md
        expected_md_file = md_path_obj / rel_path.with_suffix('.md')
        
        if not expected_md_file.exists():
            if dry_run:
                print(f"[DRY RUN] Would delete: {pdf_file}")
            else:
                try:
                    os.remove(pdf_file)
                    print(f"[DELETE] {pdf_file}")
                    deleted_count += 1
                except OSError as e:
                    print(f"[ERROR] Failed to delete {pdf_file}: {e}")
                    
            # Check if parent directory is empty and remove if so
            parent_dir = pdf_file.parent
            if parent_dir != pdf_path_obj and not any(parent_dir.iterdir()):
                 if dry_run:
                     print(f"[DRY RUN] Would delete empty directory: {parent_dir}")
                 else:
                     try:
                        parent_dir.rmdir()
                        print(f"[RMDIR] {parent_dir}")
                     except OSError:
                        pass # Directory might not be empty or other parsing error
        # else:
            # print(f"[KEEP] {pdf_file} (Found {expected_md_file})")

    if dry_run:
         print("Dry run completed.")
    else:
         print(f"Cleanup completed. Deleted {deleted_count} files.")

def main():
    parser = argparse.ArgumentParser(description="Cleanup orphaned PDF slides.")
    parser.add_argument('--dry-run', action='store_true', help="Show what would be deleted without actually deleting.")
    
    args = parser.parse_args()
    
    cleanup_orphaned_pdfs(PDF_ROOT, MD_ROOT, args.dry_run)

if __name__ == "__main__":
    main()
