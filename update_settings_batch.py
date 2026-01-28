import os
import json

def update_settings(md_root="MD"):
    if not os.path.exists(md_root):
        print(f"Directory {md_root} not found.")
        return

    for item in os.listdir(md_root):
        full_path = os.path.join(md_root, item)
        if os.path.isdir(full_path):
            settings_path = os.path.join(full_path, "settings.json")
            if os.path.exists(settings_path):
                try:
                    with open(settings_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    
                    changed = False
                    
                    # 1. Add GenerateMap (Default True)
                    if "GenerateMap" not in data:
                        data["GenerateMap"] = True
                        changed = True
                    
                    # 2. Add CourseName (Default to ChapterName, which should exist)
                    if "CourseName" not in data:
                        # Use ChapterName if exists, else folder name
                        chapter_name = data.get("ChapterName", item)
                        data["CourseName"] = chapter_name
                        changed = True
                        
                    if changed:
                        with open(settings_path, "w", encoding="utf-8") as f:
                            json.dump(data, f, indent=4, ensure_ascii=False)
                        print(f"Updated {settings_path}")
                    else:
                        print(f"Skipped {settings_path} (fields already exist)")
                        
                except Exception as e:
                    print(f"Error updating {settings_path}: {e}")

if __name__ == "__main__":
    update_settings()
