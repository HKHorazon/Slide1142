import os
import json

def cleanup_settings(md_root="MD"):
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
                    
                    # Ensure CourseName exists (should have been added by previous script, but double check)
                    if "CourseName" not in data:
                        # Fallback to ChapterName if CourseName missing (safety net)
                        if "ChapterName" in data:
                            data["CourseName"] = data["ChapterName"]
                            changed = True
                    
                    # Remove ChapterName
                    if "ChapterName" in data:
                        del data["ChapterName"]
                        changed = True
                        
                    if changed:
                        with open(settings_path, "w", encoding="utf-8") as f:
                            json.dump(data, f, indent=4, ensure_ascii=False)
                        print(f"Cleaned {settings_path}")
                    else:
                        print(f"No changes for {settings_path}")
                        
                except Exception as e:
                    print(f"Error cleaning {settings_path}: {e}")

if __name__ == "__main__":
    cleanup_settings()
