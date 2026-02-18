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

### Chapter 07
# 網頁結構基礎 - HTML

## Horazon
## 互動媒體設計 (一學期)

---

# 網頁三劍客

<br>

回顧一下，每個網頁都是由這三種檔案組成的：

1.  **HTML** (.html)：**骨架**。決定網頁有哪些內容 (標題、圖片、按鈕)。
2.  **CSS** (.css)：**皮膚**。決定網頁長什麼樣子 (顏色、大小、排版)。
3.  **JavaScript** (.js)：**靈魂**。決定網頁怎麼互動 (點擊、動畫、運算)。

> 今天我們專注於 **HTML (HyperText Markup Language)**。

---

# 開發環境準備：VS Code

<br>

工欲善其事，必先利其器。
請確認你已經安裝好 **Visual Studio Code**。

### 必裝擴充套件：
1.  **Chinese (Traditional)**：繁體中文介面。
2.  **Live Server**：即時預覽網頁 (存檔自動重整)。
3.  **Auto Rename Tag**：自動修改前後標籤。
4.  **Prettier** (選用)：自動排版程式碼。

---

# 建立你的第一個專案

<br>

1.  在桌面上建立一個資料夾 `MyFirstWeb`。
2.  開啟 VS Code -> **檔案** -> **開啟資料夾**。
3.  建立一個檔案 `index.html`。
    -   *為什麼是 Index？* 因為這是網頁伺服器預設的首頁檔名。
4.  建立一個資料夾 `images` (用來放圖片)。

---

# Emmet：一秒生出骨架

<br>

在 `index.html` 裡面，輸入驚嘆號 `!`，然後按 `Tab` 鍵。
你會看到：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```

這就是網頁的標準結構！

---

# HTML 結構解析

<br>

-   `<!DOCTYPE html>`：告訴瀏覽器：「我是用最新的 HTML5 標準寫的」。
-   `<html>`：根元素，包住所有東西。
-   `<head>`：**給瀏覽器看的資訊** (標題、編碼、SEO、CSS連結)。
    -   使用者在頁面上看不到這裡的東西。
-   `<body>`：**給使用者看的內容** (文字、圖片、影片)。
    -   你要呈現的內容全部寫在這裡。

---

# HTML 標籤語法

<br>

大多數標籤都是**成對**出現的：

```html
<標籤名稱 屬性="值"> 內容 </標籤名稱>
```

-   **起始標籤**：`<p>`
-   **結束標籤**：`</p>` (多一個斜線)
-   **內容**：夾在中間的文字。

**例外 (空標籤 Void Elements)**：
有些標籤沒有內容，所以不需要結束標籤。
-   `<img>` (圖片)
-   `<br>` (換行)
-   `<hr>` (分隔線)

---

# 常用標籤：標題與段落

<br>

-   **標題**：`<h1>` 到 `<h6>`
    -   `<h1>` 用於網頁主標題 (一個頁面建議只有一個)。
    -   `<h2>`, `<h3>` 用於副標題、章節標題。
    -   *不要為了讓字變大而使用標題，樣式請交給 CSS。*

-   **段落**：`<p>`
    -   一般的內文文字。
    -   瀏覽器會自動在段落前後加上一些空白間距。

---

# 常用標籤：列表

<br>

-   **無序列表**：`<ul>` + `<li>`
    -   前面會有小圓點。
    -   適用於：導覽列、特點介紹。

```html
<ul>
    <li>Figma</li>
    <li>HTML</li>
    <li>CSS</li>
</ul>
```

-   **有序列表**：`<ol>` + `<li>`
    -   前面會有數字 (1, 2, 3...)。
    -   適用於：步驟說明、排行榜。

---

# 常用標籤：超連結

<br>

網頁之所以叫「網」頁，就是因為有連結。

```html
<a href="https://www.google.com" target="_blank">前往 Google</a>
```

-   **`href`** (Hypertext Reference)：目標網址。
-   **`target="_blank"`**：在新分頁開啟 (選用)。
-   內容可以是文字，也可以是圖片 (把 `<img>` 包在 `<a>` 裡面)。

---

# 常用標籤：圖片

<br>

```html
<img src="images/logo.png" alt="網站Logo" width="200">
```

-   **`src`** (Source)：圖片來源。
    -   絕對路徑：`https://example.com/cat.jpg`
    -   相對路徑：`./images/cat.jpg` (推薦)
-   **`alt`** (Alternative Text)：替代文字。
    -   當圖片跑不出來時顯示的文字。
    -   **對 SEO 和 視障人士 (螢幕閱讀器) 非常重要！**
-   **`width` / `height`**：設定寬高 (通常建議在 CSS 設定)。

---

# 區塊元素 vs 行內元素

<br>

HTML 元素分為兩大類特性：

### 1. 區塊元素 (Block)
-   **霸道**：自己獨佔一行，左右撐滿。
-   可以設定寬高。
-   例如：`<div>`, `<p>`, `<h1>`, `<ul>`, `<li>`。

### 2. 行內元素 (Inline)
-   **合群**：可以跟別人擠在同一行。
-   **不能**設定寬高 (寬度由內容撐開)。
-   例如：`<span>`, `<a>`, `<img>`, `<b>`。

---

# 容器標籤：Div 與 Span

<br>

當我們需要把一堆東西包起來做排版時：

-   **`div` (Division)**：
    -   最通用的**區塊**容器。
    -   本身沒有意義，純粹為了分組或排版。
    -   例如：把 標題+圖片+內文 包成一個 `<div class="card">`。

-   **`span`**：
    -   最通用的**行內**容器。
    -   用來包住一段文字中的「特定幾個字」來改顏色。
    -   例如：`<p>今天是 <span>星期五</span> 喔！</p>`

---

# 語意化標籤

<br>

HTML5 引入了有意義的標籤，讓結構更清晰 (對 SEO 有幫助)。
不要整個網頁都用 `<div>`！

-   `<header>`：頁首 (Logo, 導覽列)。
-   `<nav>`：導覽選單。
-   `<main>`：主要內容區。
-   `<section>`：章節區塊。
-   `<article>`：獨立的文章內容。
-   `<footer>>`：頁尾 (版權宣告, 聯絡資訊)。

> **口訣：頭(Header)、身(Main)、腳(Footer)。**

---

# 實作練習：個人簡介網頁

<br>

利用今天學到的標籤，做出你的第一個網頁：

1.  **標題** (`h1`)：你的名字。
2.  **副標題** (`h2`)：你的職稱或科系。
3.  **照片** (`img`)：放置一張個人頭像。
4.  **簡介** (`p`)：一段自我介紹。
5.  **技能** (`ul`+`li`)：列出你會的技能 (Figma, HTML, Gaming...)。
6.  **連結** (`a`)：連到你的 IG 或 GitHub。

記得存檔後用 **Live Server** 預覽喔！

---

# 下週預告

<br>

現在你的網頁只有黑白文字，很醜對吧？
下週我們要變魔術了！

**網頁樣式美化 - CSS**
-   如何改變顏色與字體？
-   如何讓圖片變圓形？
-   如何做出版面配置 (Layout)？
-   認識 Flexbox 排版神器。

請把今天的 `index.html` 留好，下週我們會繼續幫它「化妝」！

---
