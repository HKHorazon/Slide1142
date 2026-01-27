import os
import subprocess
import sys
import datetime

def git_push_flow():
    # 0. Environment check
    project_root = os.getcwd()
    print(f"[GitPush] Running in: {project_root}")
    
    # 1. Generate Course Maps
    print("\n[GitPush] >>> Step 1: Generating Course Maps...")
    map_script = os.path.join(".agent", "skills", "slide", "scripts", "generate_map.py")
    md_root = "MD"
    
    if os.path.exists(map_script) and os.path.exists(md_root):
        # Iterate over all directories in MD/
        for item in os.listdir(md_root):
            full_path = os.path.join(md_root, item)
            if os.path.isdir(full_path):
                # Run generate_map.py -d <folder_name>
                try:
                    print(f"--- Checking {item} ---")
                    subprocess.run([sys.executable, map_script, "-d", item], check=False) 
                except Exception as e:
                    print(f"Failed to generate map for {item}: {e}")
    else:
        print("[GitPush] Warning: generate_map.py or MD directory not found. Skipping Step 1.")

    # 2. Export Slides (This also updates display/index.html)
    print("\n[GitPush] >>> Step 2: Exporting Slides...")
    # Path to export script: .agent/skills/slide/scripts/export.py
    export_script = os.path.join(".agent", "skills", "slide", "scripts", "export.py")
    
    if not os.path.exists(export_script):
        print(f"Error: Export script not found at {export_script}")
        sys.exit(1)

    try:
        # Run export.py with -a (all)
        subprocess.run([sys.executable, export_script, "-a"], check=True)
        print("[GitPush] Slide export completed.")
    except subprocess.CalledProcessError as e:
        print(f"[GitPush] Export failed: {e}")
        sys.exit(1)

    # 3. Cleanup Old PDFs
    print("\n[GitPush] >>> Step 3: Cleaning up old PDFs...")
    cleanup_script = os.path.join(".agent", "skills", "slide", "scripts", "cleanup_pdf.py")
    
    if os.path.exists(cleanup_script):
        try:
            subprocess.run([sys.executable, cleanup_script], check=True)
            print("[GitPush] Cleanup completed.")
        except subprocess.CalledProcessError as e:
            print(f"[GitPush] Cleanup failed (non-critical): {e}")
    else:
        print(f"[GitPush] Warning: Cleanup script not found at {cleanup_script}")

    # 4. Regenerate Index (To remove deleted PDFs from listing)
    print("\n[GitPush] >>> Step 4: Regenerating Index...")
    # reuse export_script path, use -i flag
    try:
        subprocess.run([sys.executable, export_script, "-i"], check=True)
        print("[GitPush] Index regenerated.")
    except subprocess.CalledProcessError as e:
        print(f"[GitPush] Index regeneration failed: {e}")

    # 5. Sync Index to Root (display/index.html -> index.html)
    print("\n[GitPush] >>> Step 5: Syncing Root Index...")
    display_index = os.path.join("display", "index.html")
    root_index = "index.html"
    
    if os.path.exists(display_index):
        try:
            with open(display_index, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Fix relative paths: ../PDF -> PDF
            content = content.replace('../PDF', 'PDF')
            
            with open(root_index, "w", encoding="utf-8") as f:
                f.write(content)
            
            print(f"[GitPush] Updated root {root_index} from {display_index}")
        except Exception as e:
            print(f"[GitPush] Failed to sync root index: {e}")
    else:
        print(f"[GitPush] Warning: {display_index} not found.")

    # 6. Git Commit
    print("\n[GitPush] >>> Step 6: Git Commit...")
    try:
        subprocess.run(["git", "add", "."], check=True)
        
        # Check if there are changes to commit
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if status.stdout.strip():
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"Auto update: Export slides and update index ({timestamp})"
            subprocess.run(["git", "commit", "-m", message], check=True)
            print(f"[GitPush] Committed with message: {message}")
        else:
            print("[GitPush] No changes to commit.")
    except subprocess.CalledProcessError as e:
         print(f"[GitPush] Git stage/commit failed: {e}")
         sys.exit(1)

    # 6. Git Push
    print("\n[GitPush] >>> Step 6: Git Push...")

    try:
        subprocess.run(["git", "push"], check=True)
        print("[GitPush] Push successful.")
    except subprocess.CalledProcessError as e:
        print(f"[GitPush] Git push failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    git_push_flow()
