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

### Chapter 13
# 響應式網頁設計 (RWD)

## Horazon
## 互動媒體設計 (一學期)

---

# 什麼是 RWD？

<br>

**響應式網頁設計**

以前，我們得做兩個網站：
-   `www.example.com` (電腦版)
-   `m.example.com` (手機版)

現在，我們只需要做**一個網站**，它會自動適應任何螢幕大小 (手機、平板、筆電、大螢幕)。
這就是 RWD。

---

# 核心三要素

<br>

要達成 RWD，必須具備三個條件：

1.  **Viewport Meta Tag**：告訴瀏覽器「我要做 RWD」。
2.  **流動佈局 (Fluid Layout)**：寬度用 `%` 而不是 `px`。
3.  **媒體查詢 (Media Queries)**：CSS 的條件判斷式。

---

# 1. Viewport 設定

<br>

如果你沒加這一行，手機瀏覽器會以為它是電腦螢幕，然後把網頁縮很小 (像以前的 iPhone 3GS 看網頁那樣)。

請確保你的 HTML `<head>` 裡有這一行 (VS Code 的 `!` 會自動幫你加)：

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

-   `width=device-width`：寬度 = 裝置寬度。
-   `initial-scale=1.0`：初始縮放比例 1:1 (不縮放)。

---

# 2. 圖片自適應

<br>

這是最容易壞掉的地方。如果圖片寬度 800px，手機寬度只有 375px，圖片就會爆出去。

**萬用解法 (CSS Reset 裡必加)**：

```css
img {
    max-width: 100%;
    height: auto;
}
```

-   `max-width: 100%`：圖片最大只能跟父容器一樣寬。
-   `height: auto`：高度自動計算，保持圖片比例不變形。

---

# 3. 媒體查詢 (Media Queries)

<br>

CSS 的核心魔法。
「如果螢幕寬度滿則某個條件，就套用這些 CSS。」

```css
/* 預設樣式 (電腦版) */
body {
    background: white;
    font-size: 16px;
}

/* 當螢幕寬度 "小於" 768px 時 (平板/手機) */
@media (max-width: 768px) {
    body {
        background: lightgray;
        font-size: 14px;
    }
}
```

---

# 斷點

<br>

我們通常會設定幾個關鍵的斷點來切換樣式：

1.  **Mobile (手機)**：< 576px
2.  **Tablet (平板)**：576px ~ 768px
3.  **Desktop (桌面)**：> 992px
4.  **Large Desktop (大螢幕)**：> 1200px

> **Bootstrap** 或 **Tailwind CSS** 等框架都幫你定義好這些斷點了。

---

# 行動優先 (Mobile First)

<br>

以前我們習慣先寫電腦版，再用 `@media (max-width)` 去修手機版。
現在主流推薦 **Mobile First**：

**先寫手機版 CSS，再用 `@media (min-width)` 去加強電腦版。**

```css
/* 預設樣式 (手機版) */
.container { padding: 10px; }

/* 當螢幕 "大於" 768px 時 (平板/電腦) */
@media (min-width: 768px) {
    .container { padding: 40px; }
}
```

**好處**：手機版程式碼最精簡，效能最好 (不用覆蓋樣式)。

---

# RWD 導覽列

<br>

RWD 最經典的挑戰就是 Navbar。

-   **大螢幕**：選單橫排顯示 (Home, About, Contact)。
-   **小螢幕**：選單隱藏，變成一個「三條線 (漢堡圖示)」。
    -   點擊漢堡圖示 -> 選單從旁邊或上面滑出來。

這需要結合 **HTML (結構)** + **CSS (隱藏/顯示)** + **JS (點擊切換 Class)**。

---

# Flexbox 在 RWD 的應用

<br>

記得 `flex-direction` 嗎？

```css
.card-group {
    display: flex;
    flex-direction: column; /* 手機版：直排 */
}

@media (min-width: 768px) {
    .card-group {
        flex-direction: row; /* 電腦版：橫排 */
    }
}
```

只要一行 CSS，就能讓版面從直的變橫的！

---

# Grid 在 RWD 的應用

<br>

Grid 更強大，直接改欄數。

```css
.gallery {
    display: grid;
    grid-template-columns: 1fr; /* 手機版：1欄 */
    gap: 10px;
}

@media (min-width: 576px) {
    .gallery {
        grid-template-columns: 1fr 1fr; /* 平板：2欄 */
    }
}

@media (min-width: 992px) {
    .gallery {
        grid-template-columns: 1fr 1fr 1fr 1fr; /* 電腦：4欄 */
    }
}
```

---

# 實作練習：響應式卡片

<br>

利用上次的卡片元件，做一個 RWD 畫廊：

1.  **HTML**：放 6 張卡片。
2.  **CSS (Mobile First)**：
    -   預設 `grid-template-columns: 1fr` (單欄)。
    -   圖片 `max-width: 100%`。
3.  **Media Query**：
    -   `@media (min-width: 768px)` -> 改成 3 欄 (`1fr 1fr 1fr`)。

**測試方式**：
打開 Chrome 開發者工具 (`F12`)，切換到手機模式 (Device Toolbar)，拉動寬度看看變化。

---

# 下週預告

<br>

寫程式很累對吧？
尤其是被那些分號、括號搞得頭很痛的時候。

下週我們要進入**快樂天堂**：

**進階無程式碼平台 - Wix**
-   不用寫一行程式碼。
-   拖拉放完成專業網站。
-   直接發布上線。

但別忘了，正是因為你懂了 HTML/CSS 基礎，你用 Wix 會比別人強 100 倍 (因為你懂它的原理)！

---
