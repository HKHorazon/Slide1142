---
name: arrange-image
description: 自動重新命名並整理 MD 檔內的圖片，將其搬移至專案 IMAGE 資料夾的對應章節下，並更新 MD 的相對路徑。
---

# Arrange Image

自動整理特定課程的 Markdown 檔案中所使用的圖片，讓原本散佈各處的圖片檔案搬移至有系統的目錄結構中。

## 觸發方式

當使用者要求「整理圖片」、「重新命名圖片」或明確提及 `arrange-image` 技能時。

## 使用說明

請透過 `run_command` 工具執行此技能的 Python 腳本：
```bash
python .agent/skills/arrange-image/scripts/arrange_image.py <target_path>
```
 `<target_path>` 可以是以下三種：
- **單一 `.md` 檔案** (例如 `e:\弘光\課程\114.2\MD\WebHalf互動媒體\Web_09.md`)
- **特定資料夾** (例如 `e:\弘光\課程\114.2\MD\WebHalf互動媒體`)
- **`all`** (遞迴處理 `e:\弘光\課程\114.2\MD` 目錄下所有的 `.md` 檔案)

## 動作細節

執行腳本時，會針對指定的 `.md` 檔案自動執行下列處理：
1. 找出檔案內所有引用的本地端圖片 (支援 Markdown 影像語法 `![]()` 與 HTML `<img>` 標籤)。
2. 將圖片檔案搬移至對應的資源資料夾：`e:\弘光\課程\114.2\IMAGE\課程名稱\章節名稱\`。
3. 依據來源重命名圖片檔案：若是引用文字 (alt-text) 有意義，則用 `章節名稱_自訂alt.png` 命名；若無則自動命名為 `章節名稱_流水號.png`。
4. 自動修改原本 `.md` 檔案內的圖片路徑，轉換為相對應的相對路徑 (例如：`../../IMAGE/xxx/xxx.png`)。
