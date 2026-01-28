import os
import json
import sys
import glob

# Add the script directory to path so we can import generate_map
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

import generate_map

INPUT_ROOT_DIR = 'MD'

def check_slides():
    print("Checking slides and course maps...")
    
    if not os.path.exists(INPUT_ROOT_DIR):
        print(f"Error: {INPUT_ROOT_DIR} not found.")
        return

    for item in os.listdir(INPUT_ROOT_DIR):
        full_course_path = os.path.join(INPUT_ROOT_DIR, item)
        if not os.path.isdir(full_course_path):
            continue
            
        print(f"\n--- Processing {item} ---")
        settings_path = os.path.join(full_course_path, 'settings.json')
        
        # 1. Load or Initialize Settings
        settings_data = {}
        if os.path.exists(settings_path):
            try:
                with open(settings_path, 'r', encoding='utf-8') as f:
                    settings_data = json.load(f)
            except Exception as e:
                print(f"Error reading settings for {item}: {e}")
                continue
        else:
            print(f"Settings not found for {item}. Creating defaults.")
            settings_data = {
                "IsDisplay": True,
                "Sequence": 999,
                "MapLock": False,
                "GenerateMap": True,
                "CourseName": item
            }
            # Write it later if needed, but logic below handles updates
            
        # 2. Ensure CourseName Correctness
        # Logic: If missing, set to folder name or ChapterName. 
        # User asked to "Ensure correctness" - assuming enforcing the field existence.
        dirty_settings = False
        
        if "CourseName" not in settings_data:
            course_name = settings_data.get("ChapterName", item)
            settings_data["CourseName"] = course_name
            dirty_settings = True
            print(f"Added missing CourseName: {course_name}")
            
        # Clean up legacy ChapterName if present
        if "ChapterName" in settings_data:
            del settings_data["ChapterName"]
            dirty_settings = True
            print("Removed legacy ChapterName")

        if dirty_settings:
            try:
                with open(settings_path, 'w', encoding='utf-8') as f:
                    json.dump(settings_data, f, indent=4, ensure_ascii=False)
                print("Updated settings.json")
            except Exception as e:
                print(f"Failed to update settings: {e}")

        # 3. Handle Map Logic
        map_lock = settings_data.get("MapLock", False)
        generate_map_flag = settings_data.get("GenerateMap", True)
        
        # Use simple heuristic to find map file: *_00_Map.md
        # Or asking generate_map what the filename is? 
        # generate_map.py logic: {prefix}_00_Map.md or Course_00_Map.md
        # Let's search for any *_00_Map.md
        map_files = glob.glob(os.path.join(full_course_path, '*_00_Map.md'))
        
        if map_lock:
            print(f"MapLock is TRUE. Skipping map operations.")
            continue
            
        if not generate_map_flag:
            print(f"GenerateMap is FALSE. Checking for deletion.")
            if map_files:
                for map_file in map_files:
                    try:
                        os.remove(map_file)
                        print(f"Deleted existing map: {os.path.basename(map_file)}")
                    except Exception as e:
                        print(f"Failed to delete {map_file}: {e}")
            else:
                 print("No map file found. Nothing to delete.")
        else:
            print(f"GenerateMap is TRUE. Updating map.")
            # Call generation script logic
            # Since we are in the same process, we can simple call the function if imported
            # But generate_map.py is designed to run standalone or imported.
            generate_map.generate_map(item)

if __name__ == "__main__":
    check_slides()
