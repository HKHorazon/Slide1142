import os
import sys
import re
import shutil

BASE_MD_DIR = r"e:\弘光\課程\114.2\MD"
BASE_IMG_DIR = r"e:\弘光\課程\114.2\IMAGE"

def clean_filename(name):
    # 移除無法做為檔名的字元
    return re.sub(r'[\\/*?:"<>|]', "", name).strip()

def get_relative_path(from_dir, to_path):
    # 取得相對路徑並統一替換為斜線
    return os.path.relpath(to_path, from_dir).replace("\\", "/")

def process_md_file(md_path):
    md_path = os.path.abspath(md_path)
    if not os.path.isfile(md_path) or not md_path.lower().endswith('.md'):
        return

    # 取得 CourseName 與 ChapterName
    # MD路徑範例: e:\弘光\課程\114.2\MD\CourseName\ChapterName.md
    try:
        rel_to_base = os.path.relpath(md_path, BASE_MD_DIR)
        parts = rel_to_base.split(os.sep)
        if len(parts) >= 2:
            course_name = parts[-2]
            chapter_name = os.path.splitext(parts[-1])[0]
        else:
            print(f"Skipping {md_path} (不符合預期資料夾結構)")
            return
    except ValueError:
        return

    md_dir = os.path.dirname(md_path)
    target_img_dir = os.path.join(BASE_IMG_DIR, course_name, chapter_name)
    os.makedirs(target_img_dir, exist_ok=True)

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 正則表示式抓取 Markdown 語法與 HTML img 語法
    img_pattern = re.compile(r'!\[(.*?)\]\((.*?)\)')
    html_img_pattern = re.compile(r'<img\s+[^>]*src="([^"]+)"\s*(?:alt="([^"]*)")?[^>]*>')
    
    counter = 1
    
    def handle_replacement(alt_text, img_src, original_text, is_html=False):
        nonlocal counter
        
        # 略過網路圖片或 Base64
        if img_src.startswith('http://') or img_src.startswith('https://') or img_src.startswith('data:'):
            return original_text
            
        # 計算原始圖片絕對路徑
        if os.path.isabs(img_src):
            original_img_path = img_src
        else:
            original_img_path = os.path.join(md_dir, img_src)
            
        original_img_path = os.path.normpath(original_img_path)
        
        # 若圖片不存在於本地，則不處理以免破壞原文檔
        if not os.path.exists(original_img_path):
            print(f"找不到圖片: {original_img_path}")
            return original_text
            
        # 決定新檔名
        _, ext = os.path.splitext(original_img_path)
        ext = ext.lower()
        if not ext:
            ext = '.png'
            
        alt_clean = clean_filename(alt_text) if alt_text else ""
        if alt_clean:
            new_filename = f"{chapter_name}_{alt_clean}{ext}"
        else:
            new_filename = f"{chapter_name}_{counter:02d}{ext}"
            
        # 若有重名衝突，則增加序號直到不衝突 (除非它是同一個檔案)
        new_img_path = os.path.join(target_img_dir, new_filename)
        while os.path.exists(new_img_path) and os.path.abspath(original_img_path) != os.path.abspath(new_img_path):
            counter += 1
            if alt_clean:
                new_filename = f"{chapter_name}_{alt_clean}_{counter:02d}{ext}"
            else:
                new_filename = f"{chapter_name}_{counter:02d}{ext}"
            new_img_path = os.path.join(target_img_dir, new_filename)
            
        # 若原圖不在目標位置，則搬移
        if os.path.abspath(original_img_path) != os.path.abspath(new_img_path):
            shutil.move(original_img_path, new_img_path)
            print(f"Moved: {os.path.basename(original_img_path)} -> {new_img_path}")
            
        # 轉換為從 MD 檔出發的相對路徑
        rel_path = get_relative_path(md_dir, new_img_path)
        
        counter += 1
        
        if is_html:
            # HTML標籤的情況，單純把 src 的地方替換掉
            return original_text.replace(img_src, rel_path)
        else:
            # Markdown 標籤直接重建，若路徑有空白則包以 <> 以防破圖
            if ' ' in rel_path:
                return f"![{alt_text}](<{rel_path}>)"
            else:
                return f"![{alt_text}]({rel_path})"

    # 封裝 callback 函數給正則表達式
    def md_repl(match):
        alt_text = match.group(1)
        img_src = match.group(2).strip()
        # 若路徑有使用 < > 包覆以處理空白，則去除它們以便正確讀取實體檔案
        if img_src.startswith('<') and img_src.endswith('>'):
            img_src = img_src[1:-1].strip()
            
        replacement = handle_replacement(alt_text, img_src, match.group(0), is_html=False)
        # 若傳回新的 Markdown 字串且路徑包含空白，確保其合法性 (handle_replacement 回傳字串，若含有相對路徑需補回)
        # 不過 handle_replacement 在 is_html=False 時回傳 f"![{alt_text}]({rel_path})"
        # 我們直接在 handle_replacement 改寫邏輯比較優雅。
        return replacement

    def html_repl(match):
        img_src = match.group(1)
        alt_text = match.group(2) if match.group(2) else ""
        return handle_replacement(alt_text, img_src, match.group(0), is_html=True)

    new_content = img_pattern.sub(md_repl, content)
    new_content = html_img_pattern.sub(html_repl, new_content)

    # 只有當內容有切實改變時，才寫回檔案
    if new_content != content:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated paths in: {md_path}")

def process_target(target):
    if target.lower() == 'all':
        for root, _, files in os.walk(BASE_MD_DIR):
            for file in files:
                if file.lower().endswith('.md'):
                    process_md_file(os.path.join(root, file))
        print("全部處理完成。")
    elif os.path.isdir(target):
        for root, _, files in os.walk(target):
            for file in files:
                if file.lower().endswith('.md'):
                    process_md_file(os.path.join(root, file))
        print(f"資料夾 {target} 處理完成。")
    elif os.path.isfile(target):
        process_md_file(target)
        print(f"檔案 {target} 處理完成。")
    else:
        print(f"Invalid target: {target} (請輸入有效路徑或 'all')")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python arrange_image.py <target_path|all>")
        sys.exit(1)
    
    target = sys.argv[1]
    process_target(target)
