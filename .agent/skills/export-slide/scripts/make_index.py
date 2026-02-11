import os
import sys

# Add the script directory to path so we can import export
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

import export

def make_index():
    print("Generating Index...")
    try:
        # 1. Generate display/index.html
        export.generate_index_html()
        
        # 2. Sync to Root
        print("Syncing root index.html...")
        display_index = os.path.join("display", "index.html")
        root_index = "index.html"
        
        # We assume the script is run from project root or paths are relative to it.
        # export.py usually assumes cwd is project root for reading MD/ folders.
        
        if os.path.exists(display_index):
            with open(display_index, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Adjust links for root location
            content = content.replace('../PDF', 'PDF')
            
            with open(root_index, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated root {root_index}")
        else:
            print(f"Warning: {display_index} not found.")
            
    except Exception as e:
        print(f"Failed to update index: {e}")

if __name__ == "__main__":
    make_index()
