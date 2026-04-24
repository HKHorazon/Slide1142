---
name: slide-image-check
description: 用於檢查並處理 Markdown 檔案中的圖片：移除圖片檔名空白，並將原本與 md 放在同目錄的圖片搬移至對應的 IMAGE 資料夾並更新連結。
---

# slide-image-check 技能

這個技能負責維護 `e:\弘光\課程\114.2` 中的 `.md` 檔案，確保其圖片參照符合課程的存放規範。

## 功能說明
1. **圖片檔名無空白**：不允許 `.md` 檔案引用的圖片檔名有空白；若有，會自動將該圖片檔案重新命名（例如以底線 `_` 取代空白），並同步更新 `.md` 中的連結。
2. **圖片搬移**：不允許圖片存放在與 `.md` 相同的目錄內。如果發現圖片位於 MD 資料夾，會被自動搬移至 `IMAGE/{CourseName}/{ChapterName}/` 下，並自動更名與更新 `.md` 內的連結。
3. **處理回報**：每次執行後，會列出所有已變更的 Markdown 檔以及被搬移或重新命名的圖片路徑，以便追蹤。

## 觸發方式
當使用者提到 `/slide-image-check` 或是要求「處理 md 圖片」、「移除圖片空白」、「將 md 內的圖片移到 IMAGE」時，請執行此技能。

## 使用方式
使用 `run_command` 工具執行以下的 Python 腳本：

```bash
python .agent/skills/slide-image-check/scripts/slide_image_check.py <target_path>
```

參數 `<target_path>` 支援以下三種：
- **單一 `.md` 檔案**：如 `e:\弘光\課程\114.2\MD\CourseName\Chapter1.md`
- **單一資料夾**：如 `e:\弘光\課程\114.2\MD\CourseName`，會處理其中的所有 `.md` 檔。
- **所有資料夾**：直接傳入 `all`，會掃描 `e:\弘光\課程\114.2\MD` 目錄下所有的 `.md` 檔案。

## 執行範例
如果你想要處理某個特定資料夾：
```bash
python .agent/skills/slide-image-check/scripts/slide_image_check.py "e:\弘光\課程\114.2\MD\Mobile手遊"
```

如果你想要處理所有資料夾：
```bash
python .agent/skills/slide-image-check/scripts/slide_image_check.py all
```
