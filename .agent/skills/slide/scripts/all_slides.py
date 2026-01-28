import argparse
import subprocess
import sys
import os

# Define paths to scripts
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CHECK_SLIDES_SCRIPT = os.path.join(SCRIPT_DIR, 'check_slides.py')
CLEANUP_SCRIPT = os.path.join(SCRIPT_DIR, 'cleanup_pdf.py')
EXPORT_SCRIPT = os.path.join(SCRIPT_DIR, 'export.py')
MAKE_INDEX_SCRIPT = os.path.join(SCRIPT_DIR, 'make_index.py')

def run_script(script_path, args=[]):
    """Runs a python script as a subprocess."""
    cmd = [sys.executable, script_path] + args
    print(f"\n[Running] {os.path.basename(script_path)} {' '.join(args)}")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print(f"Error running {script_path}. Exit code: {result.returncode}")
        sys.exit(result.returncode)

def main():
    parser = argparse.ArgumentParser(description="Orchestrate slide generation workflow.")
    parser.add_argument('git_push', nargs='?', choices=['true', 'false'], default='false', 
                        help="Whether to commit and push changes (true/false). Default: false")
    
    args = parser.parse_args()
    do_git = args.git_push.lower() == 'true'

    # 1. /check-slides
    run_script(CHECK_SLIDES_SCRIPT)

    # 2. /build-slides (Cleanup + Export -a)
    run_script(CLEANUP_SCRIPT)
    run_script(EXPORT_SCRIPT, ['-a'])

    # 3. /check-index (Make Index)
    run_script(MAKE_INDEX_SCRIPT)

    # 4. Git Commit & Push (Conditional)
    if do_git:
        print("\n[Git] Starting git commit and push...")
        try:
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "Auto-update slides and index"], check=True)
            subprocess.run(["git", "push"], check=True)
            print("[Git] Push success.")
        except subprocess.CalledProcessError as e:
            # Check if it was just "nothing to commit" which returns non-zero usually but isn't fatal for us
            print(f"[Git] Error (or nothing to commit): {e}")

if __name__ == "__main__":
    main()
