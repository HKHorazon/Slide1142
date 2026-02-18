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
<!-- _paginate: false -->

### Chapter 06
# 網頁原型製作 - Figma 實作

## Horazon
## 互動媒體設計 (一學期)

---

# 今日目標：打造高品質原型

<br>

上週我們學會了工具操作，今天我們要把它們組合起來，完成一個**高保真 (High-Fidelity)** 的網頁原型。

### 實作流程：
1.  **設定格線 (Grid System)**：讓版面整齊。
2.  **建立元件 (Components)**：製作 Navbar 與 Footer。
3.  **Hero Section 設計**：運用遮罩與排版。
4.  **內容區塊**：運用 Auto Layout 製作卡片。
5.  **互動原型 (Prototyping)**：讓按鈕可以點擊跳轉。

---

# 1. 設定畫布與格線 (Grid System)

<br>

專業的網頁設計都有隱形的格子。

1.  新增 Frame (`F`) -> 選擇 **Desktop (1440px)**。
2.  在右側屬性面板找到 **Layout Grid**，點 `+` 號。
3.  點擊九宮格圖示，將 Grid 改為 **Columns (欄)**。
4.  設定參數 (Bootstrap 標準)：
    -   **Count**: 12 (切成12欄)
    -   **Margin**: 100 (左右留白)
    -   **Gutter**: 24 (欄與欄的間距)
5.  你會看到紅色的直條，這就是你的對齊參考線。

> **Tip**: 按 `Shift + G` 可以隨時開關格線顯示。

---

# 2. 製作導覽列 (Navigation Bar)

<br>

導覽列是每個網頁都有的元件。

1.  **Logo**: 輸入文字 (例如 "MySite")，字體 24px 加粗。
2.  **選單項目**: 輸入 "首頁", "關於", "作品", "聯絡"。
3.  **Auto Layout**:
    -   選取這四個文字，按 `Shift + A`。
    -   設定間距 (Gap) 為 32px。
4.  **組合**:
    -   選取 Logo 和 選單群組，再按一次 `Shift + A`。
    -   將 Layout Mode 設為 **Horizontal** (橫向)。
    -   將對齊方式設為 **Space Between** (左右推開)。
    -   寬度設為 Fill Container (填滿容器)。
5.  **元件化**: 按 `Ctrl + Alt + K` 變成 Component。

---

# 3. 設計 Hero Section (首頁大圖)

<br>

第一眼的視覺衝擊。

1.  **背景圖**:
    -   畫一個矩形 (`R`)，寬度 Fill Container，高度 600px。
    -   放入我們用 AI 生成的背景圖。
    -   與上方的 Navbar 組合起來。
2.  **遮罩文字**:
    -   打上你的 Slogan (例如 "EXPLORE THE WORLD")，字體巨大 (96px)。
    -   顏色設為白色。
    -   加上 **Drop Shadow** (Y:4, Blur:10)，讓文字在複雜背景上也看得清。
3.  **CTA 按鈕**:
    -   做一個 "立即開始" 的按鈕，放在文字下方。

---

# 4. 製作內容卡片

<br>

我們要展示作品或服務，卡片式設計最常用。

1.  **圖片**: 畫一個矩形 (300x200)，填入圖片。
2.  **標題**: 輸入 "作品名稱" (20px Bold)。
3.  **內文**: 輸入一段假文 (16px Regular, 灰色)。
4.  **Auto Layout**:
    -   選取 標題 + 內文 -> `Shift + A` (Gap: 8px)。
    -   選取 圖片 + 文字群組 -> `Shift + A` (Gap: 16px)。
    -   加上 Padding (內距) 16px。
    -   加上 Stroke (邊框) 或 Drop Shadow。
    -   設定圓角 (Radius) 12px。

> **恭喜！你完成了一個響應式的卡片元件。**

---

# 5. 複製與排列

<br>

有了卡片元件後，我們要排列出網格。

1.  將卡片複製 3 份 (`Ctrl + D`)。
2.  選取這 3 張卡片，按 `Shift + A`。
3.  設定間距 24px。
4.  現在你有一個整齊的作品展示區了！
5.  利用 Plugin (Unsplash / Lorem Ipsum) 快速置換不同的圖片和文字，讓它看起來像真的內容。

---

# 6. 互動原型 (Prototyping)

<br>

讓靜態圖片動起來！切換右側面板到 **Prototype** 分頁。

### 頁面跳轉 (Navigate To)
1.  點選 Navbar 上的 "關於" 文字。
2.  你會看到一個有 `+` 號的小圓點。
3.  按住 `+` 號，拖拉一條線連到 "關於我們" 的 Frame。
4.  設定觸發行為：**On Click** -> **Navigate to** -> **Smart Animate** (智慧動畫)。

> **Smart Animate** 會自動計算兩個頁面物件的變化，產生平滑的補間動畫 (例如圖片放大、位置移動)。

---

# 7. 捲動與固定

<br>

### 固定導覽列
-   選取 Navbar。
-   在 Design 面板勾選 **Fix position when scrolling**。
-   現在捲動頁面時，導覽列會固定在最上方。

### 水平捲動
-   如果你有一排卡片想做成可以左右滑動 (像 Netflix)：
1.  把卡片群組的 Frame 縮小，小於內容寬度。
2.  勾選 **Clip Content** (裁切內容)。
3.  在 Prototype 面板設定 **Overflow Scrolling** 為 **Horizontal**。

---

# 8. 預覽與分享

<br>

### 預覽 (Play)
-   點擊右上角的 **Play** 按鈕 (三角形)。
-   會開啟一個新視窗，你可以像操作真網頁一樣點擊你的設計。
-   檢查連結有沒有連錯？動畫順不順？

### 分享
-   點擊右上角藍色的 **Share** 按鈕。
-   你可以複製連結給老師或朋友。
-   設定權限：**can view** (只能看) 或 **can edit** (可以改)。

---

# Figma 常用快捷鍵大全

<br>

背下來，你的設計速度快 3 倍。

| 功能 | Windows | Mac |
| :--- | :--- | :--- |
| **複製** | Ctrl + D | Cmd + D |
| **群組** | Ctrl + G | Cmd + G |
| **解散群組** | Ctrl + Shift + G | Cmd + Shift + G |
| **Auto Layout** | Shift + A | Shift + A |
| **建立元件** | Ctrl + Alt + K | Cmd + Opt + K |
| **吸管 (吸色)** | I | I |
| **測量距離** | Alt (Hover) | Opt (Hover) |
| **隱藏 UI** | Ctrl + \ | Cmd + \ |

---

# 實作任務：個人網站 Prototype

<br>

請延續上週的規劃，完成以下頁面的 High-Fidelity 原型：

1.  **首頁 (Home)**
    -   Hero Section (大圖+文字)。
    -   最新消息/精選作品區 (至少 3 張卡片)。
2.  **關於我 (About)**
    -   個人照片 + 自我介紹。
    -   技能圖表 (試著用長條圖表示)。
3.  **作品集 (Portfolio)**
    -   網格排列的作品縮圖。

**要求**：必須設定好 Prototype 連結，讓我可以從首頁點進關於我，再點回首頁。

---

# UI 設計細節檢查

<br>

在交作業前，請自己檢查一遍：

-   [ ] **對齊了嗎？** 有沒有東西歪掉？
-   [ ] **字體統一嗎？** 不要同一個標題用三種不同大小。
-   [ ] **間距一致嗎？** 這裡空 20px，那裡不要空 25px。
-   [ ] **對比夠嗎？** 灰色的字在深色背景上看得到嗎？
-   [ ] **圖片變形了嗎？** 記得用 `K` 縮放或 Fill 模式。

---

# 補充資源：UI Kits

<br>

不想從零開始畫按鈕？

去 Figma Community 搜尋 **"UI Kit"** 或 **"Design System"**。
-   **Google Material Design 3**
-   **iOS 16 UI Kit**
-   **Ant Design**

直接把別人的元件複製過來改，這是業界常見的做法 (Don't reinvent the wheel)。

---

# 下週預告

<br>

設計搞定後，我們要開始寫真正的程式碼了！

**網頁結構基礎 - HTML**
-   從畫圖軟體切換到 VS Code。
-   把 Figma 裡的框框變成 `<div>`。
-   把 Figma 裡的文字變成 `<h1>`, `<p>`。
-   正式進入前端工程師的世界。

請確認電腦已安裝 **VS Code** 與 **Chrome** 瀏覽器。

---
