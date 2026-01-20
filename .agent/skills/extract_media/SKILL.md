---
name: extract_media
description: 從 PPTX 或其他檔案萃取圖片與媒體資源的技能。
---

# 媒體萃取技能 (Extract Media Skill)

此技能用於從舊教材 (如 PPTX) 中批次萃取圖片與影片，以便於製作新教材時使用。

## 功能 (Features)

1.  **PPTX 圖片萃取**: 自動解壓縮 `.pptx` 檔並提取 `ppt/media` 下的所有檔案。
2.  **批次處理**: 支援指定單一檔案、多個檔案或整個資料夾。
3.  **自動歸檔**: 依據檔案名稱自動建立對應的輸出資料夾，例如 `Output/MySlides/image1.png`。

## 使用方法 (Usage)

### 1. 手動執行 (Command Line)
```bash
python .agent/skills/extract_media/scripts/extract.py [sources] -o [output_dir]
```

### 參數說明
- `sources`: 一個或多個來源路徑。可以是:
    - `.pptx` 檔案。
    - 包含 `.pptx` 的資料夾。
- `-o, --out`: (必填) 圖片輸出的根目錄。

## 範例

```bash
# 萃取單一檔案至指定目錄
python .agent/skills/extract_media/scripts/extract.py "OLD/AI2/L01.pptx" -o "IMAGE/AI2"

# 萃取多個檔案
python .agent/skills/extract_media/scripts/extract.py "file1.pptx" "file2.pptx" -o "IMAGE/Output"

# 萃取整個資料夾 (如 Mobile 課程)
python .agent/skills/extract_media/scripts/extract.py "OLD/Mobile" -o "IMAGE/Mobile"
```

## 注意事項
- 目前主要支援 `.pptx` (Open XML 格式)。
- 舊版 `.ppt` (OLE 格式) 因結構不同，無法使用此腳本解壓縮，需手動另存為 .pptx。
