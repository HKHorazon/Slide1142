import os
import json

def check_progress():
    base_dir = r"e:\弘光\課程\114.2\MD"
    print(f"{'Course Name':<30} | {'Completed Chapter'}")
    print("-" * 50)

    for root, dirs, files in os.walk(base_dir):
        if "settings.json" in files:
            settings_path = os.path.join(root, "settings.json")
            try:
                with open(settings_path, 'r', encoding='utf-8') as f:
                    settings = json.load(f)
                    course_name = settings.get("CourseName", "Unknown Course")
                    complete_chapter = settings.get("CompleteChapter", "N/A")
                    
                    if complete_chapter != "N/A":
                        # Calculate display length for proper alignment with Chinese characters
                        display_len = 0
                        for char in course_name:
                            display_len += 2 if ord(char) > 127 else 1
                        
                        padding = 30 - display_len
                        if padding < 0: padding = 0
                        
                        print(f"{course_name}{' ' * padding} | {complete_chapter}")
            except Exception as e:
                pass

if __name__ == "__main__":
    check_progress()
