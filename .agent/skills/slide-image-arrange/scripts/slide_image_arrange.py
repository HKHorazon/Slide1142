import os
import sys
import re
import math

BASE_MD_DIR = r"e:\弘光\課程\114.2\MD"

def calc_text_height(text_chunk):
    h = 0
    img_pattern = re.compile(r'!\[\s*(?!bg)[^\]]*\]\([^\)]+\)|<img\s+[^>]+>')
    for line in text_chunk.split('\n'):
        lb = line.strip()
        if not lb:
            h += 10
            continue
        if img_pattern.search(line) or lb.startswith("<!--") or lb.startswith("<style"): 
            continue
            
        if lb.startswith("# "): h += 110
        elif lb.startswith("## "): h += 80
        elif lb.startswith("### "): h += 60
        elif lb.startswith("- ") or lb.startswith("* ") or re.match(r'^\d+\.\s', lb):
            char_count = len(lb)
            lines_wrapped = math.ceil(char_count / 30.0) if char_count > 30 else 1
            h += 42 * lines_wrapped
        else:
            char_count = len(lb)
            lines_wrapped = math.ceil(char_count / 32.0) if char_count > 32 else 1
            h += 42 * lines_wrapped
    return h

def process_md_file(md_path, force=False):
    md_path = os.path.abspath(md_path)
    if not os.path.isfile(md_path) or not md_path.lower().endswith('.md'):
        return

    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ 讀取失敗: {md_path} ({e})")
        return

    lines = content.split('\n')
    slides = []
    current_slide = []
    
    for line in lines:
        if line.strip() == "---":
            slides.append(current_slide)
            current_slide = []
        else:
            current_slide.append(line)
    if current_slide:
        slides.append(current_slide)

    updated_any = False
    new_slides = []
    
    img_pattern = re.compile(r'!\[\s*(?!bg)[^\]]*\]\([^\)]+\)|<img\s+[^>]+>')
    spacer_pattern = re.compile(r'\n*<!-- auto-spacer -->.*?<!-- auto-spacer -->\n*', re.DOTALL)

    for slide_lines in slides:
        slide_content = "\n".join(slide_lines)
        
        has_spacer = bool(spacer_pattern.search(slide_content))
        if has_spacer:
            slide_content = spacer_pattern.sub('\n', slide_content)
        
        # 嚴格把關：只要投影片已經有 <style> 或 <style scoped>，就絕對不碰它！
        # 這樣就保證了老師自己修改過的比例配置不會被洗掉
        if "<style scoped>" in slide_content or "<style>" in slide_content:
            new_slides.append(slide_content)
            continue
            
        s_lines = slide_content.split('\n')
        first_img_idx = -1
        last_img_idx = -1
        img_count = 0
        
        for i, line in enumerate(s_lines):
            if img_pattern.search(line):
                if first_img_idx == -1:
                    first_img_idx = i
                last_img_idx = i
                img_count += len(img_pattern.findall(line))
        
        if img_count == 0:
            new_slides.append(slide_content)
            continue

        text_before = "\n".join(s_lines[:first_img_idx])
        text_after = "\n".join(s_lines[last_img_idx+1:])
        
        height_before = calc_text_height(text_before)
        height_after = calc_text_height(text_after)
                
        top_offset = 60 + height_before + 10
        if top_offset > 600:
            top_offset = 600
            
        bottom_margin = 40
        available_height = 720 - top_offset - height_after - bottom_margin
        
        if available_height < 150:
            available_height = 150
            
        css_rules = []
        if img_count == 1:
            w = 90
            max_h = available_height # 動態上限保護
            css_rules.append(f"img:nth-of-type(1) {{\n  display: block;\n  object-fit: contain;\n  width: {w}%;\n  max-height: {max_h}px;\n  margin: 10px auto;\n}}")
        elif img_count == 2:
            w = 48
            max_h = available_height
            for i in range(2):
                css_rules.append(f"img:nth-of-type({i+1}) {{\n  display: inline-block;\n  object-fit: contain;\n  width: {w}%;\n  max-height: {max_h}px;\n  margin: 10px 1%;\n}}")
        elif img_count == 3:
            w = 31
            max_h = available_height
            for i in range(3):
                css_rules.append(f"img:nth-of-type({i+1}) {{\n  display: inline-block;\n  object-fit: contain;\n  width: {w}%;\n  max-height: {max_h}px;\n  margin: 10px 1%;\n}}")
        else:
            cols = 2 if img_count == 4 else 3
            w = 48 if cols == 2 else 31
            max_h = (available_height - 20) // 2 
            for i in range(img_count):
                css_rules.append(f"img:nth-of-type({i+1}) {{\n  display: inline-block;\n  object-fit: contain;\n  width: {w}%;\n  max-height: {max_h}px;\n  margin: 10px 1%;\n}}")

        style_block = "<style scoped>\n" + "\n".join(css_rules) + "\n</style>\n\n"
        
        slide_content = slide_content.strip('\n')
        new_slides.append(style_block + slide_content)
        updated_any = True

    if updated_any:
        new_content = "\n---\n".join(new_slides)
        if new_content.startswith("\n---\n"):
            new_content = new_content[1:]
            
        try:
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ 已插入自動排版(保護既有設定版): {md_path}")
        except Exception as e:
            print(f"❌ 寫入失敗: {md_path} ({e})")

def process_target(target):
    if target.lower() == 'all':
        for root, _, files in os.walk(BASE_MD_DIR):
            for file in files:
                if file.lower().endswith('.md'):
                    process_md_file(os.path.join(root, file))
        print("🎉 全部處理完成。")
    elif os.path.isdir(target):
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
        print(f"❌ 錯誤: 找不到路徑 {target}，請確認是否正確輸入或輸入 'all'")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python slide_image_arrange.py <target_path|all>")
        sys.exit(1)
    
    process_target(sys.argv[1])
