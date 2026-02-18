---
description: 自動產生部落格文章 (搜尋、大綱、Banner、撰寫)。使用方式：/blog {主題}
---

當使用者輸入 `/blog {主題}` 時，請依照以下步驟執行：

1.  **資料蒐集 (Research)**
    -   使用 `search_web` 針對 `{主題}` 進行深入搜尋。
    -   找出該主題的核心概念、最新趨勢、優缺點或教學步驟。

2.  **擬定大綱 (Outline)**
    -   根據搜尋結果，規劃文章結構 (引言、核心段落、結論)。
    -   思考讀者想知道什麼，確保內容有價值。

3.  **製作 Banner (Image Generation)**
    -   使用 `generate_image` 製作一張 16:9 的 Banner。
    -   提示詞建議：「A professional, modern blog banner about {主題}, high quality, minimal text, 16:9 aspect ratio」。
    -   存檔路徑：`Blog/images/{主題}_banner.png` (若目錄不存在請建立)。

4.  **撰寫文章 (Drafting)**
    -   建立一個新的 Markdown 檔案。
    -   檔案路徑：`Blog/{YYYY-MM-DD}_{主題}.md` (若目錄不存在請建立)。
    -   **內容結構**：
        -   最上方插入 Banner：`![Banner](images/{主題}_banner.png)`
        -   **文章標題 (H1)**
        -   **引言**：吸引讀者興趣。
        -   **正文**：分段落撰寫，善用 H2, H3, 列表, 程式碼區塊。
        -   **結論**：總結重點或行動呼籲。

5.  **完成通知**
    -   告知使用者文章已生成，並提供檔案路徑。
