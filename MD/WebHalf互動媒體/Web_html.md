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

# HTML 基礎入門
## Horazon
## 互動媒體

---

# 什麼是 HTML?

## **H**yper**T**ext **M**arkup **L**anguage (超文字標記語言)

## 它**不是**程式語言，它是**標記語言**

## 負責定義網頁的**結構**與**內容** (骨架)

---
# 什麼是 DOM?

- **D**ocument **O**bject **M**odel (文件物件模型)
- 瀏覽器將 HTML 解析為**樹狀結構** (Tree Structure)
- 讓程式 (如 JavaScript) 可以改變網頁的**架構**、**樣式**與**內容**

HTML 標籤不僅是文字，更是 **DOM 節點 (Nodes)**。

---

# HTML 基本結構

一個標準的 HTML 檔案包含：

```html
<!DOCTYPE html>       <!-- 宣告文件類型 -->
<html>                <!-- 根元素 -->
<head>
    <title>標題</title> <!-- 網頁資訊 (不會顯示在頁面上) -->
    <meta charset="UTF-8">
</head>
<body>
    <!-- 這裡放網頁內容 -->
    <h1>哈囉，世界！</h1>
</body>
</html>
```

---

# HTML 標籤語法

標籤通常成對出現：
```html
<標籤名>內容</標籤名>
```

標籤內可以設定**屬性** (Attribute)：
```html
<標籤名 屬性名="屬性值">內容</標籤名>
```

部分標籤是**空標籤** (Empty Tag)，沒有結束標籤：
```html
<br> <!-- 換行 -->
```


---

# 核心標籤解說

- **`<html>`**：HTML 文件的根元素，包裹所有內容。
- **`<head>`**：包含網頁的元數據 (metadata)，如標題、編碼設定、CSS 連結等。
- **`<body>`**：包含網頁的所有**可見內容**，如文字、圖片、影片等。


---
# Meta 標籤 (Metadata)

位於 `<head>` 內，提供**瀏覽器**與**搜尋引擎**資訊。
`<meta>`是一種**空標籤** (不需要結束標籤)。


- **編碼設定** (防止亂碼)：
  `<meta charset="UTF-8">`
- **RWD 設定** (讓網頁在不同設備上正確縮放)：
  `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- **SEO 描述** (讓搜尋引擎知道你的網站是什麼)：
  `<meta name="description" content="網頁簡介...">`

---


# 文字標籤 (Text Tags)

- **標題**：`<h1>` (最大) ~ `<h6>` (最小)
- **段落**：`<p>` 文字段落 `</p>` (會有上下間距)
- **換行**：`<br>` (強制換行)
- **水平線**：`<hr>` (分隔線)
- **強調**：`<b>` (粗體), `<i>` (斜體)
- **行內容器**：`<span>` (用於特定文字樣式設定)

```html
<h1>主標題</h1>
<p>這是一段文字，包含 <b>粗體</b> 與 <i>斜體</i>。<br>這是第二行。</p>
```

---

# 圖片標籤 (Image Tag)

使用 `<img>` 標籤插入圖片 (不須成對出現的標籤)。

- **`src`** (Source)：圖片的路徑 (網址或檔案路徑)。
- **`alt`** (Alternative)：圖片無法顯示時的替代文字 (對 SEO 與無障礙很重要)。
- **`width` / `height`**：設定寬高 (像素或百分比)。

```html
<img src="logo.png" alt="網站 Logo" width="200">

<img src="https://example.com/cat.jpg" alt="可愛貓咪">
```

---

# 連結標籤 (Link Tag)

使用 `<a>` (Anchor) 標籤建立超連結。

- **`href`** (Hypertext Reference)：連結的目標網址。
- **`target`**：開啟方式，`_blank` 代表在新分頁開啟。

```html
<!-- 連到外部網站 -->
<a href="https://www.google.com" target="_blank">Google</a>

<!-- 連到同網站的其他頁面 -->
<a href="about.html">關於我們</a>

<!-- 圖片連結 -->
<a href="index.html">
  <img src="home-icon.png" alt="首頁">
</a>
```

---
# 表格標籤 (Table Tags)

<br>

使用 `<table>` 建立表格。
`<tr>` (Table Row)：表格的一列
`<th>` (Table Header)：標題儲存格 (通常粗體置中)
`<td>` (Table Data)：資料儲存格

```html
<table border="1">
  <tr>
    <th>姓名</th>
    <th>分數</th>
  </tr>
  <tr>
    <td>小明</td>
    <td>90</td>
  </tr>
</table>
```

---
# 其他常用標籤

- **`<br>`**：換行  (不須成對出現的標籤)
- **`<hr>`**：水平線 (不須成對出現的標籤)
- **`<span>`**：行內容器 (用於特定文字樣式設定)

```html
<br>
<hr>
<span>特定文字樣式</span>
```



---
# div ：現在HTML最重要的標籤

```html
<div>特定區塊樣式</div>
```

為什麼\<div\>是現在HTML最重要的標籤？
1. **佈局核心**：它是 CSS Flexbox 和 Grid 佈局的基礎，能自由建構複雜的網頁架構。
2. **樣式容器**：作為無語義的區塊元素，它不會自帶多餘樣式，是套用 CSS 樣式的最佳選擇。
3. **邏輯分組**：能將相關元素組成獨立區塊，方便進行內容管理與區塊化設計。
4. **組件化開發**：在現代前端框架中，`<div>` 常用作組件的封裝容器，便於維護與重用。


---

# 清單標籤 (List Tags)

- **無序清單** (`<ul>` + `<li>`)：項目符號通常是圓點。
- **有序清單** (`<ol>` + `<li>`)：項目會有數字排序 (1, 2, 3...)。

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">

<div>

**無序清單 (Unordered)**
```html
<ul>
  <li>蘋果</li>
  <li>香蕉</li>
</ul>
```
</div>

<div>

**有序清單 (Ordered)**
```html
<ol>
  <li>註冊帳號</li>
  <li>驗證信箱</li>
</ol>
```
</div>

</div>

---

# 按鈕與表單 (Button & Input)

用於與使用者互動。

- **按鈕**：`<button>`
- **輸入框**：`<input>` (空標籤)，透過 `type` 屬性改變類型。

```html
<!-- 普通按鈕 -->
<button>點我</button>

<!-- 文字輸入框 -->
<input type="text" placeholder="請輸入姓名">

<!-- 密碼輸入框 -->
<input type="password">

<!-- 日期選擇 -->
<input type="date">
```

---

# 實作練習：個人簡介

建立 `index.html`，試著包含以下內容：

1. `<h1>` 顯示你的名字。
2. `<p>` 簡短自我介紹。
3. `<img>` 放一張你的大頭貼或喜歡的圖片。
4. `<ul>` 列出 3 個興趣。
5. `<a href="...">` 連結到你的 IG 或 FB (設定新分頁開啟)。
6. `<button>` 一個 "聯絡我" 的按鈕。

---
# 實作練習：個人簡介 (結果)

<br>

```html
<!DOCTYPE html>
<html>
<head>
    <title>個人簡介</title>
</head>
<body>
    <h1>Horazon</h1>
    <p>多遊系老師，教學遊戲開發。</p>
    <img src="Horazon.jpg" alt="陳大衛">
    <ul>
        <li>電子遊戲</li>
        <li>桌上遊戲</li>
        <li>程式設計</li>
    </ul>
    <a href="https://www.instagram.com/username" target="_blank">Discord</a>
    <button>聯絡我</button>
</body>
</html>
```

---

# 結論

1. HTML 是一種標記語言，用於描述網頁的結構和內容。
2. HTML 標籤用來定義網頁的結構，如 `<html>`, `<head>`, `<body>` 等。
3. HTML 標籤可以包含屬性，用來提供額外的資訊。
4. HTML 標籤可以成對使用，如 `<p>` 與 `</p>`。
5. 也可以是空標籤，如 `<br>`。


---

# 重點回顧

1. **結構**：`html`, `head`, `body` 是基本骨架。
2. **文字**：標題用 `h1-h6`，段落用 `p`。
3. **媒體**：圖片用 `img` (記得 `alt`)，連結用 `a` (記得 `href`)。
4. **清單**：`ul` (點點) 與 `ol` (數字)，項目都用 `li`。
5. **互動**：`button` 與 `input` 讓使用者輸入資訊。

