---
name: export-slide
description: 匯出與發布 Marp 投影片 (Export & Git Push)
---

# 投影片匯出技能 (Export Slide Skill)

此技能專注於將 Markdown 投影片匯出為 PDF，生成課程地圖，以及發布到 Git 儲存庫。

## 匯出方法 (Export Method)

當使用者提出「匯出資料夾」或「匯出 .md 檔案」為 PDF 時，請使用以下指令。

-   **匯出工具**: `export.py`
    -   必須確認來源檔案為 Marp 格式 (frontmatter 含有 `marp: true`)。
    -   **匯出單檔**: `python .agent/skills/export-slide/scripts/export.py -f <檔案路徑>`
    -   **匯出資料夾**: `python .agent/skills/export-slide/scripts/export.py -d <資料夾路徑>`
    -   **匯出所有**: `python .agent/skills/export-slide/scripts/export.py -a`

-   **匯出後續**: 
    -   告知使用者 PDF 已儲存於 `PDF` 對應目錄。

## 課程地圖 (Course Map)

-   **生成地圖**: `generate_map.py`
    -   **Trigger**: 當使用者說「更新課程地圖」或 "Update course map" 時。
    -   **Command**: `python .agent/skills/export-slide/scripts/generate_map.py -d <CourseFolder>` (例如: `Mobile手遊`)
    -   **注意**: 腳本會檢查 `settings.json` 的 `MapLock` 設定。

## 索引生成 (Index Generation)

-   **生成索引**: `make_index.py`
    -   **Command**: `python .agent/skills/export-slide/scripts/make_index.py`
    -   這會掃描 PDF 資料夾並在 `display/index.html` 生成索引頁面。

## 檢查工具 (Check Tools)

-   **檢查投影片**: `check_slides.py`
    -   **Command**: `python .agent/skills/export-slide/scripts/check_slides.py`
    -   檢查課程設定並根據規則更新/刪除課程地圖。

## 清理工具 (Cleanup)

-   **清理舊檔**: `cleanup_pdf.py`
    -   **Command**: `python .agent/skills/export-slide/scripts/cleanup_pdf.py`
    -   刪除 `PDF` 資料夾中沒有對應 Markdown 來源的孤立 PDF 檔案。

## Git 發布 (Git Push)

若使用者要求「Git Push」或執行 `/git-push`，請參照 `.agent/skills/git-push/SKILL.md` (若存在) 或執行以下標準流程：

1.  清理 PDF (`cleanup_pdf.py`)
2.  匯出所有投影片 (`export.py -a`)
3.  生成索引 (`make_index.py`)
4.  Git Add, Commit, Push (需手動執行 git 指令或呼叫 git 技能)
