---
name: slide
description: 用於建立與管理課程 Marp 投影片的技能。
---

# 投影片技能 (Slide Skill)

此技能協助建立、更新與格式化**任何教學科目**的 Marp 投影片。

## 教學風格與方針 (Teaching Guidelines)

1.  **背景設定**:
    -   **身份**: 弘光科技大學 多媒體與遊戲發展系 助理教授。
    -   **科目**: 遊戲引擎與遊戲程式。
    -   **對象**: 學生基礎較弱且被動，**必須用最淺顯易懂的方式**進行解說。

2.  **撰寫風格**:
    -   **精準直白**: 內容偏向技術精準度，不繞彎路。
    -   **嚴肅專業**: **拒絕**俏皮語氣、玩梗或過度譬喻。
    -   **簡單明瞭**: 用詞需極度簡單，降低文字閱讀門檻，讓學生能直觀理解。
    -   **降低資訊密度**: 每個頁面的資訊量應盡量減少，保持版面清爽，避免學生消化不良。
    -   **用語規範**: 避免使用「本週、下週」等時間性字眼，改用「本章、下一章」。
    -   **特殊規定**: 不需要「下課」頁面。

3.  **主題配色 (依資料夾/科目統一)**:
    -   **Mobile手遊**: **綠色系** (`#15803d` -> `#22c55e`).
    -   **WebHalf互動媒體**: **橘色系**.
    -   **CSharp程式**: **藍色系**.
    -   **AI2應用程式**: **紫色系**.
    -   **Horazon額外內容**: **灰紫色系** (`#581c87` -> `#64748b`).
    -   (若遇**新科目**，請務必先詢問使用者偏好顏色).

## 使用方法 (Usage)

1.  **建立新投影片**:
    -   **位置**: 根據主題建立於 `MD` 目錄下的對應子資料夾中 (例如 `MD/CSharp程式` 或 `MD/WebHalf互動媒體`)。
    -   **命名**: 參照該資料夾現有檔案的命名規則並遞增編號 (例如 `Web_02.md` -> `Web_03.md`)。
    -   套用 `HoraStyle` 主題。
    -   (不需要加入學習地圖)
2.  **格式規則**:
    -   標題：`h1` 用於大標題，`h3` 用於章節標示。
    -   程式碼區塊：使用標準 Markdown 語法 (```)。
    -   視覺效果：使用 `HoraStyle.css` 定義的樣式類別。

3.  **匯出方法 (Export Method)**:
    -   當使用者提出「匯出資料夾」或「匯出 .md 檔案」為 PDF 時。
    -   **第一步**: 確認該檔案是否為 Marp 格式 (檢查 frontmatter 是否含有 `marp: true`)。
    -   **第二步**: 若確認為 Marp 檔案，**必須優先使用** `python .agent/skills/slide/scripts/export.py` 進行匯出。
    -   **具體執行**:
        -   匯出單檔：`python .agent/skills/slide/scripts/export.py -f <檔案路徑>`
        -   匯出資料夾：`python .agent/skills/slide/scripts/export.py -d <資料夾路徑>`
        -   匯出所有：`python .agent/skills/slide/scripts/export.py -a`
    -   **第三步**: 匯出完成後，告知使用者 PDF 已儲存於 `PDF` 對應目錄。

## 參考模板 (Reference)

-   **模板檔案**: `.agent/skills/slide/reference/template.md`
    -   可複製此檔案作為新投影片的起點。

## 內容撰寫指南 (Content Guide)

4.  **投影片結構**:
    -   **首頁 (Lead)**: 包含課程標題 (#) -> 章節編號 (###) -> 章節副標 (##)。需使用 `<!-- _class: lead -->`。
    -   **內容頁**: 每頁一個核心主題，使用 H1 (#) 作為頁面標題。
    -   **程式教學**: 先說明觀念，再展示程式碼，最後解釋輸出結果。
    -   **總結頁**: 課程結束前列出重點回顧。

2.  **排版建議**:
    -   善用 **條列式** (List) 呈現重點，避免過多長文。
    -   使用 `<br>` 增加垂直間距。
    -   重點關鍵字可用 `<mark>關鍵字</mark>` (螢光筆效果) 或 `**粗體**` 強調。

3.  **程式碼規範**:
    -   務必指定語言以啟用語法高亮 (例如: ` ```csharp ` 或 ` ```html `)。
    -   字串請依照 `HoraStyle` 設定，顯示為紅色以利閱讀 (自動套用)。

## 指令 (Commands)

-   `export_pdf`: 執行 `.agent/skills/slide/scripts/export.py` 以產生 PDF 檔案。
    -   **注意**: 請務必在**使用者明確要求匯出**時才執行此指令。
    -   **匯出所有**: `python .agent/skills/slide/scripts/export.py` (預設)
    -   **匯出單檔**: `python .agent/skills/slide/scripts/export.py -f <path/to/file.md>`
    -   **匯出資料夾**: `python .agent/skills/slide/scripts/export.py -d <path/to/directory>`
    -   **清理舊檔**: `python .agent/skills/slide/scripts/cleanup_pdf.py`
        -   刪除 `PDF` 資料夾中沒有對應 Markdown 來源的孤立 PDF 檔案。
