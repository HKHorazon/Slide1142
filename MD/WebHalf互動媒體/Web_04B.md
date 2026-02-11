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

### Chapter 04B
# HTML 基本語法

## Horazon
## 互動媒體設計

---

# 什麼是 HTML?

## **H**yper**T**ext **M**arkup **L**anguage (超文字標記語言)

-   它**不是**程式語言，它是**標記語言**。
-   負責定義網頁的**結構**與**內容** (骨架)。
-   所有的網頁 (Google, Facebook, YouTube) 都是由 HTML 構成的。

---

# HTML 基本結構

一個標準的 HTML 檔案包含兩個主要部分：`<head>` 與 `<body>`。

```html
<!DOCTYPE html>       <!-- 1. 宣告文件類型 (HTML5) -->
<html lang="zh-TW">   <!-- 2. 根元素 (設定語言為繁體中文) -->
<head>
    <!-- 3. 頭部 (給瀏覽器看的資訊) -->
    <meta charset="UTF-8">
    <title>網頁標題</title> 
</head>
<body>
    <!-- 4. 身體 (給使用者看的內容) -->
    <h1>哈囉，世界！</h1>
</body>
</html>
```

---

# Head 與 SEO (Metadata)

位於 `<head>` 內的標籤雖然不會顯示在頁面上，但對 **SEO (搜尋引擎優化)** 至關重要。

-   **`<meta charset="UTF-8">`**
    -   設定編碼，防止中文變亂碼。
-   **`<meta name="viewport" content="...">`**
    -   **RWD 必備！** 讓網頁在手機上能正確縮放。
-   **`<meta name="description" content="...">`**
    -   網頁簡介，會顯示在 Google 搜尋結果下方。
-   **Open Graph (OG) Tags**
    -   當你在 FB/Line 分享連結時顯示的預覽圖與標題。
    -   `<meta property="og:image" content="cover.jpg">`

---

# 網頁圖示 (Favicon)

這是在瀏覽器分頁上顯示的小圖示：

1.  準備一張正方形的圖片 (png 或 ico)。
2.  放在網站根目錄。
3.  在 `<head>` 裡面加入：

```html
<link rel="icon" href="favicon.png" type="image/png">
```

> **小技巧**：這是讓網站看起來「專業」的關鍵細節！


---

# 常用文字標籤 (Text Tags)

-   **標題**：`<h1>` (最大) ~ `<h6>` (最小)
    -   *注意：一個頁面最好只有一個 h1*。
-   **段落**：`<p>` (Paragraph)
    -   會自動帶有上下間距。
-   **換行**：`<br>` (Break)
    -   空標籤，不用結束標籤。
-   **分隔線**：`<hr>` (Horizontal Rule)
-   **強調**：
    -   `<b>` (Bold) / `<strong>` (語氣加重，SEO加分)
    -   `<i>` (Italic) / `<em>` (Emphasis，語氣強調)

---

# 清單標籤 (Lists)

整理條列式內容：

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">

<div>

### 無序清單 (`<ul>`)
(Unordered List)
通常是圓點項目符號。

```html
<ul>
  <li>蘋果</li>
  <li>香蕉</li>
</ul>
```
</div>

<div>

### 有序清單 (`<ol>`)
(Ordered List)
會有數字排序 (1, 2, 3...)。

```html
<ol>
  <li>註冊帳號</li>
  <li>驗證信箱</li>
</ol>
```
</div>

</div>

> **巢狀清單**： `li` 裡面還可以再包一個 `ul` 喔！

---

# 圖片標籤 (Images)

使用 `<img>` 標籤插入圖片 (空標籤)。

```html
<img src="路徑" alt="替代文字" title="滑鼠提示">
```

-   **`src` (Source)**：
    -   **相對路徑**：`images/pic.jpg` (推薦)
    -   **絕對路徑**：`https://example.com/pic.jpg` (連結外部圖片)
-   **`alt` (Alternative)**：
    -   圖片跑不出來時顯示的文字。
    -   **身心障礙輔助 (盲人讀屏軟體)** 會唸出這段文字。
    -   Google 圖片搜尋也靠它來認識這張圖。

---

# 路徑觀念 (Paths)

這是在寫網頁時最容易錯的地方！

-   **`./`**：代表**目前資料夾** (同層)。
    -   `./style.css` (或是直接寫 `style.css`)
-   **`../`**：代表**上一層資料夾**。
    -   `../images/logo.png` (去上一層找 images 資料夾)
-   **`/`**：代表**根目錄** (網站的最頂層)。

> **建議**：專案結構要清楚，通常開一個 `images` 資料夾統一管理圖片。

---

# 連結標籤 (Hyperlinks)

使用 `<a>` (Anchor) 標籤。

```html
<a href="https://google.com" target="_blank">前往 Google</a>
```

-   **`href`**：目標網址。
-   **`target="_blank"`**：在新分頁開啟 (保留你的網站不被關掉)。
-   **錨點連結**：連結到同頁面的特定位置。
    -   `<a href="#section1">跳到第一章</a>`
    -   `<h2 id="section1">第一章</h2>`

---

# 區塊與行內元素 (Block vs Inline)

這是 HTML 排版的基礎觀念：

### 1. 區塊元素 (Block)
-   **獨佔一行**，會自動換行。
-   可以設定寬高 (width/height)。
-   例如：`<div>`, `<p>`, `<h1>`, `<ul>`, `<li>`

### 2. 行內元素 (Inline)
-   **不會換行**，跟別人在同一排。
-   寬高由內容決定，設定 width 無效。
-   例如：`<span>`, `<a>`, `<b>`, `<img>`

> **`<div>`** 是最常用的區塊容器 (無語義)，用來分組排版。
> **`<span>`** 是最常用的行內容器，用來改一段文字中的某幾個字顏色。

---

# ID 與 Class (最重要的屬性)

為了之後寫 CSS (樣式) 做準備，一定要分清楚這兩個：

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">

<div>

### 1. id (身分證字號)
- **唯一性**：一個頁面中，同一個 id 只能出現一次。
- **用途**：錨點連結、JavaScript 控制特定元素。
- **寫法**：`<div id="header">`

</div>

<div>

### 2. class (制服/班級)
- **重複性**：多個元素可以用同一個 class。
- **用途**：設定相同的 CSS 樣式 (例如：所有的按鈕都要紅色)。
- **寫法**：`<button class="btn-red">`

</div>

</div>

> **口訣**：只有一個用 id，有很多個用 class。


---

# 表格標籤 (Tables)

雖然現在不用表格排版了，但展示數據還是很好用。

```html
<table border="1">
  <thead> <!-- 表頭區 -->
    <tr>
      <th>姓名</th>
      <th>分數</th>
    </tr>
  </thead>
  <tbody> <!-- 內容區 -->
    <tr>
      <td>小明</td>
      <td>90</td>
    </tr>
     <tr>
      <td>小華</td>
      <td rowspan="2">80 (合併儲存格)</td>
    </tr>
  </tbody>
</table>
```

---

# 語意化標籤 (Semantic HTML)

HTML5 引入了更有意義的標籤，取代滿滿的 `<div>`。

讓程式碼更好讀，SEO 更好。

-   **`<header>`**：網站或區塊的**頁首** (Logo, 導覽列)。
-   **`<nav>`**：**導覽列** (選單)。
-   **`<main>`**：頁面的**主要內容** (每個頁面只能有一個)。
-   **`<article>`**：獨立的文章內容 (如：一篇部落格)。
-   **`<section>`**：內容的章節區塊。
-   **`<aside>`**：**側邊欄** (廣告, 推薦文章)。
-   **`<footer>`**：**頁尾** (版權宣告,聯絡資訊)。

---

# 語意化結構範例

```html
<body>
    <header>
        <nav>
            <a href="#">首頁</a>
            <a href="#">關於</a>
        </nav>
    </header>

    <main>
        <article>
            <h1>文章標題</h1>
            <p>文章內容...</p>
        </article>
        <aside>
            <p>相關推薦</p>
        </aside>
    </main>

    <footer>
        <p>&copy; 2026 Horazon. All rights reserved.</p>
    </footer>
</body>
```

---

# 表單標籤 (Forms) - 互動的核心

讓使用者輸入資料。

```html
<form action="/submit" method="post">
    <!-- 標籤與關聯 -->
    <label for="username">帳號：</label>
    <input type="text" id="username" name="user" placeholder="請輸入帳號" required>
    
    <label for="password">密碼：</label>
    <input type="password" id="password" name="pass">
    
    <button type="submit">登入</button>
</form>
```

-   **`<label>`**：點選文字也能選中輸入框，增加可用性。
-   **`placeholder`**：提示文字 (灰色字)。
-   **`required`**：設定為必填。

---

# 更多表單元素

```html
<!-- 單選題 (Radio) - name 要一樣才能互斥 -->
<label><input type="radio" name="gender" value="male"> 男</label>
<label><input type="radio" name="gender" value="female"> 女</label>

<!-- 多選題 (Checkbox) -->
<label><input type="checkbox" name="interest" value="game"> 遊戲</label>
<label><input type="checkbox" name="interest" value="code"> 程式</label>

<!-- 下拉選單 (Select) -->
<select name="city">
    <option value="taipei">台北</option>
    <option value="taichung" selected>台中</option>
</select>

<!-- 多行文字 (Textarea) -->
<textarea rows="5" placeholder="請留言..."></textarea>
```

---

# HTML5 新型態輸入 (New Input Types)

手機瀏覽器會根據 type 跳出不同的鍵盤喔！

```html
<!-- 1. 日期選擇器 -->
<label>生日：<input type="date"></label>

<!-- 2. 顏色選擇器 -->
<label>喜歡的顏色：<input type="color"></label>

<!-- 3. 數值滑桿 (0~100) -->
<label>滿意度：<input type="range" min="0" max="100"></label>

<!-- 4. 檔案上傳 -->
<label>上傳大頭貼：<input type="file" accept="image/*"></label>
```

> **試試看**：用手機打開這些網頁，日期選擇器會變得很方便！


---

# 多媒體標籤 (Multimedia)

HTML5 讓播放影音變得超簡單，不用再裝 Flash 了！

### 聲音 (Audio)
```html
<audio controls src="music.mp3">
    您的瀏覽器不支援 audio 標籤。
</audio>
```

### 影片 (Video)
```html
<video controls width="640" poster="cover.jpg">
    <source src="movie.mp4" type="video/mp4">
</video>
```

### 嵌入 YouTube (Iframe)
-   去 YouTube 影片下方按「分享」->「嵌入」，複製程式碼貼上即可。

---

# 嵌入 Google 地圖 (Google Maps)

同樣使用 `<iframe>` 技術：

1.  打開 Google Maps 搜尋地點 (例如：弘光科技大學)。
2.  按「分享」->「嵌入地圖」。
3.  複製 HTML 程式碼。
4.  貼到你的網頁中。

```html
<iframe src="https://www.google.com/maps/embed?..." width="600" height="450" ...>
</iframe>
```

> **用途**：放在「聯絡我們」頁面，讓客戶直接導航。


---

# 特殊字元 (Character Entities)

有些符號在 HTML 有特殊意義 (如 `<` )，直接打會出錯，要用代碼：

<style scoped>
table {
    font-size: 0.85em;
    width: 50%; /* 加寬一點，避免內容擠壓 */
}
/* 分別設定三個欄位的寬度 */
th:nth-child(1) { width: 20%; } /* 符號 */
th:nth-child(2) { width: 20%; } /* 代碼 */
th:nth-child(3) { width: 50%; } /* 說明 */
</style>

| 符號 | 代碼 | 說明 |
| :--- | :--- | :--- |
| **<** | `&lt;` | Less Than (小於) |
| **>** | `&gt;` | Greater Than (大於) |
| **&** | `&amp;` | Ampersand (和) |
| **"** | `&quot;` | 雙引號 |
| **(空白)** | `&nbsp;` | 不換行空白  |
| **©** | `&copy;` | 版權符號 |

---

# 註解 (Comments)

給人看的，瀏覽器會忽略不執行。
**快速鍵**：`Ctrl + /`

```html
<!-- 這裡是導覽列區域 -->
<nav>...</nav>

<!-- 
    我可以
    換行寫
    註解
-->
```

**好習慣**：在複雜的 `</div>` 結尾處加上註解，標示這是誰的結尾。
```html
</div> <!-- End of .container -->
```

---

# 實作練習：語意化部落格

請建立一個 `blog.html`，運用語意化標籤：

1.  **Header**：包含標題 `<h1>` 和導覽列 `<nav>`。
2.  **Main**：
    -   **Article**：一篇假文章 (`<h2>`, `<p>`, `<img>`)。
    -   **Aside**：側邊欄，包含作者簡介與大頭貼。
3.  **Footer**：版權宣告 `&copy; 2026`。
4.  **Form**：在文章下方加入一個留言區 (`<textarea>`, `<button>`)。

---

# 總結

1.  HTML 是網頁的**骨架**，要結構清晰。
2.  善用 **Emmet** 加速開發。
3.  **路徑 (`./`, `../`)** 要搞清楚。
4.  **區塊** vs **行內** 元素的排版特性不同。
5.  使用 **語意化標籤** (`header`, `main`, `footer`) 提升 SEO。
6.  利用 **表單** 與使用者互動。

**下週，我們將學習 CSS，幫這個骨架穿上漂亮的衣服！**

