---
marp: true
theme: HoraStyle
paginate: true
style: |
  :root {
    --title-bg: linear-gradient(90deg, #ea580c, #f97316);
    --title-text-color: #ffffff;
  }
  section.lead {
    background: linear-gradient(135deg, #431407 0%, #000000 100%);
  }
---

<!-- _class: lead -->
<!--_paginate: false-->

### Chapter 04
# VS Code 編輯器攻略

## Horazon
## 互動媒體設計

---

# 為什麼需要專業工具？

寫網頁就像寫文章，雖然用「記事本」也能寫，但是...

-   **沒有顏色**：語法標示不清，很難分辨標籤與內容。
-   **沒有提示**：全部都要自己背，打錯一個字就掛掉。
-   **沒有除錯**：寫錯了找不到哪裡錯，浪費時間。
-   **沒有即時預覽**：改一個字就要去瀏覽器按 F5。

所以，我們需要一個強大的**IDE (整合開發環境)**！

---

# 為什麼選擇 VS Code?

-   **全名**：Visual Studio Code (不是 Visual Studio 喔！)
-   **開發者**：微軟 (Microsoft)。
-   **市佔率**：目前全球最受歡迎的程式碼編輯器 (超過 70% 工程師使用)。

### 優勢：
1.  **免費開源** (Open Source)。
2.  **跨平台** (Windows, Mac, Linux 都能用)。
3.  **輕量級** (開啟速度快，不吃電腦資源)。
4.  **擴充性強** (擁有海量的 Extensions 外掛)。

---

# Step 1: 下載與安裝

(如果你還沒安裝，請現在動手！)

1.  前往官網：[code.visualstudio.com](https://code.visualstudio.com/)
2.  點擊 **Download for Windows** (或是 Mac)。
3.  下載後執行安裝檔。
4.  安裝過程**一路按「下一步」** (Next) 即可。
    -   *建議勾選 "Add to PATH" (預設通常有勾)。*

---

# Step 2: 認識介面 (Interface Tour)

打開 VS Code，你會看到幾個主要區域：

1.  **活動列 (Activity Bar)** (最左側)：切換功能的按鈕。
    -   Explorer (檔案總管)
    -   Search (搜尋)
    -   Source Control (Git 版本控制)
    -   Run and Debug (除錯)
    -   **Extensions (擴充功能)**
2.  **側邊欄 (Side Bar)**：顯示檔案列表或搜尋結果。
3.  **編輯區 (Editor)**：寫程式的地方。
4.  **狀態列 (Status Bar)** (最下方)：顯示行號、編碼、Git 分支。

---

# Step 3: 重要功能 - 命令列面板

這可能是 VS Code 最強大的功能。

### 快捷鍵：`Ctrl + Shift + P` (Mac: Cmd + Shift + P)

-   這是一個「萬能搜尋框」。
-   可以在這裡找到 VS Code 的**所有功能**。
-   例如輸入：
    -   `Format Document` (排版程式碼)
    -   `Theme` (更換佈景主題)
    -   `Settings` (開啟設定)


---

# Step 4: 擴充套件 (Extensions) - 必裝篇

點擊左側 **四個方塊** 的圖示 (Extensions)，搜尋並安裝：

1.  **Chinese (Traditional)**
    -   讓介面變成**繁體中文**。
    -   *安裝後右下角會提示重啟 (Restart)*。
2.  **Live Server** (Ritwick Dey)
    -   讓你的電腦變成小型伺服器，**即時預覽**網頁。
    -   存檔 (Ctrl+S) 後，瀏覽器會自動重新整理，超方便！

---

# Step 5: 擴充套件 - 效率篇 (選裝)

讓你的開發速度倍增：

1.  **Auto Rename Tag**
    -   修改 HTML 標籤時 (`<h1>` 改成 `<h2>`)，尾巴的 `</h1>` 會**自動跟著變** `</h2>`。
    -   省去兩邊修改的麻煩。
2.  **Material Icon Theme**
    -   讓檔案總管的圖示變漂亮！
    -   HTML 檔會有橘色圖示，CSS 檔會有藍色圖示，一目了然。
3.  **Code Spell Checker**
    -   英文拼字檢查。
    -   避免變數名稱拼錯 (`backgroud` -> `background`) 導致程式跑不動。

---

# Step 6: 設定 (Settings)

VS Code 的設定分為兩種層級：

1.  **使用者設定 (User Settings)**
    -   **全域生效**。
    -   不管開哪個專案，設定都一樣 (例如：字體大小、佈景主題)。

2.  **工作區設定 (Workspace Settings)**
    -   **只對目前專案生效**。
    -   會在這個資料夾下產生一個 `.vscode` 資料夾。
    -   適合團隊合作，統一大家的排版規則。

> **如何開啟？**
> `Ctrl + ,` (逗號) -> 開啟設定頁面。

---

# 推薦的設定值

建議在設定中搜尋並調整：

-   `Font Size`: **16** (預設 14 有點小，保護眼睛)。
-   `Word Wrap`: **on** (自動換行，避免程式碼跑到螢幕外面)。
-   `Format On Save`: **勾選**。
    -   **超級重要！** 每次按 Ctrl+S 存檔時，自動幫你排版。
    -   從此不用手動對齊程式碼。

---

# Step 7: 建立專案與檔案結構

1.  在桌面上建立一個**新資料夾**，命名為 `MyWebsite`。
2.  回到 VS Code，點選 **「開啟資料夾」** (Open Folder)。
    -   *不要只開單一檔案，要開整個資料夾！*
3.  在左側檔案總管建立以下結構：
    -   `index.html` (首頁)
    -   `style.css` (樣式表)
    -   `script.js` (腳本)
    -   `images/` (建立一個資料夾放圖片)

> **命名規則**：
> 檔名一律使用**小寫英文**，單字之間用**連字號 (-)** 分隔。
> (例如：`my-profile.html`, `about-us.html`)。
> **千萬不要用中文檔名！**

---

# Step 8: Emmet 神奇語法

VS Code 內建 Emmet，讓你打程式碼像在飛。
在 HTML 檔案中輸入以下簡碼，然後按 **Tab**：

<style scoped>
table {
    font-size: 24px;
}
</style>

| 輸入簡碼 | 輸出結果 | 說明 |
| :--- | :--- | :--- |
| **`!`** | HTML5 基本骨架 | 一秒建置環境 |
| **`h1`** | `<h1></h1>` | 自動補完標籤 |
| **`.box`** | `<div class="box"></div>` | 自動產生 Class |
| **`#id`** | `<div id="id"></div>` | 自動產生 ID |
| **`ul>li*3`** | `<ul><li></li>...</ul>` | 產生 3 個列表項目 |
| **`p{Hello}`** | `<p>Hello</p>` | 產生帶內容的標籤 |

> **練習：** `div.container>ul>li.item*5` 試試看會發生什麼事？

---

# Step 9: 實戰預覽 (Live Server)

1.  在 `index.html` 輸入 `!` + `Tab`。
2.  在 `<body>` 裡輸入 `h1{Hello World}` + `Tab`。
3.  **存檔 (Ctrl + S)**。
4.  在檔案總管的 `index.html` 上按右鍵 -> **Open with Live Server**。
    -   或是看右下角有一個 `Go Live` 藍色按鈕。
5.  瀏覽器會自動彈出。
6.  試著把文字改成 `Hello CSS`，再次存檔。
7.  瀏覽器**不用重新整理**，字就會自動變！

---

# Step 10: 進階編輯技巧 (Advanced Editing)

讓你看起來像個駭客的技巧：

### 1. 多視窗編輯 (Split Editor)
-   **操作**：按住 `Alt` 點兩下檔案，或是拖曳標籤頁 (Tab) 到右邊。
-   **用途**：左邊寫 HTML，右邊寫 CSS，不用切來切去。
-   **快捷鍵**：`Ctrl + \` (反斜線)。

### 2. 專注模式 (Zen Mode)
-   **操作**：`Ctrl + K` 放開後馬上按 `Z`。
-   **效果**：全螢幕顯示程式碼，隱藏所有選單和側邊欄，讓你心無旁騖。
-   **退出**：按兩次 `Esc`。

---

# 程式碼導覽 (Navigation)

當檔案變得很長的時候...

### 1. 麵包屑 (Breadcrumbs)
-   位於編輯器最上方 (檔名旁邊)。
-   點擊可以快速跳轉。

### 2. 程式碼地圖 (Minimap)
-   位於編輯器最右側的縮圖。
-   可以快速預覽整份程式碼的結構，點擊快速捲動。

### 3. 折疊程式碼 (Folding)
-   滑鼠移到行號旁邊，會出現 `-` 號。
-   點擊可以把一整塊 `<div>...</div>` 收起來，讓畫面更清爽。

---

# 自訂程式碼片段 (User Snippets)

常常打一樣的程式碼很煩？自己做縮寫！

1.  `File` -> `Preferences` -> `Configure User Snippets`.
2.  選擇 `html.json` (或 `global`).
3.  輸入設定：
    ```json
    "My Signature": {
        "prefix": "sign",
        "body": [
            "<!-- Copryright 2026 Horazon -->",
            "<!-- Design by Me -->"
        ],
        "description": "我的簽名檔"
    }
    ```
4.  之後打 `sign` + `Tab` 就會自動出現那兩行！

---

# 必背快捷鍵 (Keyboard Shortcuts) - Windows

<style scoped>
table {
    font-size: 24px;
}
</style>

| 功能 | 快捷鍵 | 說明 |
| :--- | :--- | :--- |
| **命令面板** | `Ctrl + Shift + P` | 萬能搜尋 |
| **存檔** | `Ctrl + S` | 這是基本反射動作 |
| **複製整行** | `Shift + Alt + 下` | 不用選取，直接複製 |
| **移動整行** | `Alt + 上 / 下` | 超好用！調整順序 |
| **多重游標** | `Alt + 點擊` | 同時在多個地方打字 |
| **註解** | `Ctrl + /` | 把程式碼變成註解 |
| **搜尋檔案** | `Ctrl + P` | 快速開啟檔案 |
| **排版** | `Shift + Alt + F` | 若沒開自動排版可用 |
| **側邊欄開關**| `Ctrl + B` | 增加寫程式空間 |


---

# 整合終端機 (Integrated Terminal)

寫程式常需要打指令 (例如 Git, npm)。
不用另外開 CMD 或 PowerShell。

-   **開啟/關閉**：`` Ctrl + ` `` (Esc 下面那個波浪鍵)。
-   這個終端機的路徑**預設就在你的專案資料夾**，不用 `cd` 切換半天。

---


# 常見問題 (Troubleshooting)

### Q: Live Server 打不開？
A:
1.  確認你是在 `.html` 檔案上按右鍵。
2.  確認此資料夾是透過「開啟資料夾」打開的，而不是單獨開檔。
3.  如果 Port (5500) 被佔用，右下角點擊 Dispose 再重開。

### Q: 中文介面沒出來？
A: 安裝套件後，記得按 Restart 重啟 VS Code。

---

# 總結

-   **VS Code** 是目前最強的前端開發工具。
-   善用 **Extensions** (Live Server, Prettier) 提升效率。
-   **Emmet** 讓你打 HTML 像飛一樣。
-   **快捷鍵** (`Ctrl+S`, `Alt+上下`) 要練到變成肌肉記憶。
-   養成良好的**專案結構**習慣。

**下週，我們將深入 HTML 的語法細節！**

