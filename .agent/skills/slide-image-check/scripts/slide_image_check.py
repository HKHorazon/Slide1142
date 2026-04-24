import os
import sys
import re
import shutil

BASE_MD_DIR = r"e:\弘光\課程\114.2\MD"
BASE_IMG_DIR = r"e:\弘光\課程\114.2\IMAGE"

def clean_filename(name):
    # 將空白替換為底線，並移除其他可能的非法字元
    name = name.replace(" ", "_").replace("%20", "_")
    return re.sub(r'[\\/*?:"<>|]', "", name).strip()

def get_relative_path(from_dir, to_path):
    # 取得相對路徑並統一替換為斜線
    return os.path.relpath(to_path, from_dir).replace("\\", "/")

def get_unique_path(target_path):
    # 若檔案已存在，加上後綴直到唯一
    if not os.path.exists(target_path):
        return target_path
    
    base, ext = os.path.splitext(target_path)
    counter = 1
    while True:
        new_path = f"{base}_{counter}{ext}"
        if not os.path.exists(new_path):
            return new_path
        counter += 1

def process_md_file(md_path):
    md_path = os.path.abspath(md_path)
    if not os.path.isfile(md_path) or not md_path.lower().endswith('.md'):
        return

    md_dir = os.path.dirname(md_path)

    # 取得 CourseName 與 ChapterName
    course_name = "UnknownCourse"
    chapter_name = os.path.splitext(os.path.basename(md_path))[0]
    
    try:
        if md_path.startswith(os.path.abspath(BASE_MD_DIR)):
            rel_to_base = os.path.relpath(md_path, BASE_MD_DIR)
            parts = rel_to_base.split(os.sep)
            if len(parts) >= 2:
                course_name = parts[-2]
                # chapter_name = os.path.splitext(parts[-1])[0] # 已在上方定義
    except ValueError:
        pass

    target_img_dir = os.path.join(BASE_IMG_DIR, course_name, chapter_name)

    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ 讀取檔案失敗: {md_path} ({e})")
        return

    img_pattern = re.compile(r'!\[(.*?)\]\((<.*?>|.*?)\)')
    html_img_pattern = re.compile(r'<img\s+[^>]*src="([^"]+)"\s*(?:alt="([^"]*)")?[^>]*>')
    
    changes_made = []

    def handle_replacement(alt_text, img_src, original_text, is_html=False):
        # 略過網路圖片或 Base64
        if img_src.startswith('http://') or img_src.startswith('https://') or img_src.startswith('data:'):
            return original_text
            
        # 若路徑有使用 < > 包覆以處理空白，則去除它們以便正確處理
        clean_img_src = img_src
        if clean_img_src.startswith('<') and clean_img_src.endswith('>'):
            clean_img_src = clean_img_src[1:-1].strip()
        
        # 處理 URL 編碼的空白 (%20)
        clean_img_src = clean_img_src.replace("%20", " ")

        if os.path.isabs(clean_img_src):
            original_img_path = clean_img_src
        else:
            original_img_path = os.path.join(md_dir, clean_img_src)
            
        original_img_path = os.path.normpath(original_img_path)
        
        if not os.path.exists(original_img_path):
            return original_text

        orig_filename = os.path.basename(original_img_path)
        orig_dir = os.path.dirname(original_img_path)
        
        needs_move = False
        needs_rename = False
        
        new_filename = orig_filename
        new_dir = orig_dir

        # 規則 2：如果圖片在 MD 資料夾內（或 MD 的子資料夾），搬移至 IMAGE 對應目錄
        # 判斷是否為 md_dir 或其子目錄
        try:
            if os.path.commonpath([md_dir, orig_dir]) == md_dir:
                needs_move = True
                new_dir = target_img_dir
                os.makedirs(new_dir, exist_ok=True)
        except ValueError:
            pass
            
        # 規則 1：不允許檔名有空白，如果有，修改檔名
        if " " in new_filename or "%20" in new_filename:
            needs_rename = True
            new_filename = clean_filename(new_filename)
            
        if not needs_move and not needs_rename:
            # 檔案名稱沒空白，也沒有在 MD 目錄下，不需處理
            return original_text

        # 決定最終目標路徑
        target_img_path = get_unique_path(os.path.join(new_dir, new_filename))
        
        # 執行搬移或重新命名
        try:
            shutil.move(original_img_path, target_img_path)
        except Exception as e:
            print(f"  [錯誤] 無法搬移/重新命名檔案 {original_img_path}: {e}")
            return original_text

        # 轉換為從 MD 檔出發的相對路徑
        rel_path = get_relative_path(md_dir, target_img_path)
        
        action_msg = ""
        if needs_move and needs_rename:
            action_msg = f"已搬移並重新命名: {orig_filename} -> {target_img_path}"
        elif needs_move:
            action_msg = f"已搬移: {orig_filename} -> {target_img_path}"
        elif needs_rename:
            action_msg = f"已重新命名: {orig_filename} -> {new_filename}"
            
        changes_made.append(action_msg)
        
        if is_html:
            return original_text.replace(img_src, rel_path)
        else:
            return f"![{alt_text}]({rel_path})"

    def md_repl(match):
        alt_text = match.group(1)
        img_src = match.group(2).strip()
        return handle_replacement(alt_text, img_src, match.group(0), is_html=False)

    def html_repl(match):
        img_src = match.group(1)
        alt_text = match.group(2) if match.group(2) else ""
        return handle_replacement(alt_text, img_src, match.group(0), is_html=True)

    new_content = img_pattern.sub(md_repl, content)
    new_content = html_img_pattern.sub(html_repl, new_content)

    if new_content != content:
        try:
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"\n✅ 已更新 Markdown 檔案: {md_path}")
            for msg in changes_made:
                print(f"  - {msg}")
        except Exception as e:
            print(f"❌ 寫入檔案失敗: {md_path} ({e})")

def process_target(target):
    if target.lower() == 'all':
        print("🔍 掃描所有 MD 檔案...")
        for root, _, files in os.walk(BASE_MD_DIR):
            for file in files:
                if file.lower().endswith('.md'):
                    process_md_file(os.path.join(root, file))
        print("🎉 全部處理完成。")
    elif os.path.isdir(target):
        print(f"🔍 掃描資料夾: {target}")
        for root, _, files in os.walk(target):
            for file in files:
                if file.lower().endswith('.md'):
                    process_md_file(os.path.join(root, file))
        print(f"🎉 資料夾處理完成。")
    elif os.path.isfile(target):
        if target.lower().endswith('.md'):
            process_md_file(target)
            print(f"🎉 檔案處理完成。")
        else:
            print("❌ 錯誤：目標不是 .md 檔案。")
    else:
        print(f"❌ 錯誤: 找不到路徑 {target}，請輸入有效路徑或 'all'")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python slide_image_check.py <target_path|all>")
        sys.exit(1)
    
    target = sys.argv[1]
    process_target(target)
