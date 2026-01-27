import os
import subprocess
import sys
import datetime

def git_push_flow():
    # 0. Environment check
    project_root = os.getcwd()
    print(f"[GitPush] Running in: {project_root}")
    
    # 0. Generate Course Maps (New Step)
    print("\n[GitPush] >>> Step 0: Generating Course Maps...")
    map_script = os.path.join(".agent", "skills", "slide", "scripts", "generate_map.py")
    md_root = "MD"
    
    if os.path.exists(map_script) and os.path.exists(md_root):
        # Iterate over all directories in MD/
        for item in os.listdir(md_root):
            full_path = os.path.join(md_root, item)
            if os.path.isdir(full_path):
                # Run generate_map.py -d <folder_name>
                try:
                    # Capture output to avoid cluttering unless error, or just let it print?
                    # generate_map prints useful info ("Skipping...", "Generating..."). Let it print.
                    print(f"--- Checking {item} ---")
                    subprocess.run([sys.executable, map_script, "-d", item], check=False) 
                except Exception as e:
                    print(f"Failed to generate map for {item}: {e}")
    else:
        print("[GitPush] Warning: generate_map.py or MD directory not found. Skipping Step 0.")

    # 1. Export Slides (This also updates display/index.html)
    print("\n[GitPush] >>> Step 1: Exporting Slides...")
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

    # 2. Update display/index.html paths (Verification)
    # The export script generates display/index.html by design.
    # We verify it exists.
    print("\n[GitPush] >>> Step 2: Verifying Index...")
    index_path = os.path.join("display", "index.html")
    if os.path.exists(index_path):
        print(f"[GitPush] Verified: {index_path} exists and was updated.")
    else:
        print(f"[GitPush] Warning: {index_path} was not found after export.")

    # 3. Git Commit
    print("\n[GitPush] >>> Step 3: Git Commit...")
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

    # 4. Git Push
    print("\n[GitPush] >>> Step 4: Git Push...")
    try:
        subprocess.run(["git", "push"], check=True)
        print("[GitPush] Push successful.")
    except subprocess.CalledProcessError as e:
        print(f"[GitPush] Git push failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    git_push_flow()
