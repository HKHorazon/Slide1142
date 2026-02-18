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

### Chapter 12
# 網頁互動實作 - DOM 操作與事件

## Horazon
## 互動媒體設計 (一學期)

---

# 什麼是 DOM？

<br>

**Document Object Model**

-   瀏覽器把 HTML 程式碼讀進去後，會自作主張把它轉成一個樹狀結構的物件，這個物件就叫 DOM。
-   JS 透過 DOM 來控制 HTML。
-   簡單來說：**DOM 就是 JS 和 HTML 溝通的橋樑。**

> `document` 是這個大樹的根節點 (Root)。

---

# 抓取元素

<br>

要控制誰，先把它抓出來。

### 1. 透過 ID (最快)
```javascript
const title = document.getElementById("title");
```

### 2. 透過 Selector (最強)
```javascript
// 抓第一個符合的 (像 CSS 選擇器一樣)
const box = document.querySelector(".box");

// 抓所有符合的 (回傳陣列)
const allItems = document.querySelectorAll("li"); 
```

---

# 修改內容

<br>

抓到元素後，我們可以改它的內容。

```javascript
const title = document.getElementById("title");

// 1. 修改文字 (innerText)
title.innerText = "你好，JS！";

// 2. 修改 HTML (innerHTML)
title.innerHTML = "<em>斜體字</em>"; // 會解析 HTML 標籤
```

> **注意**：`innerHTML` 有資安風險 (XSS)，如果是使用者輸入的內容，請用 `innerText`。

---

# 修改樣式

<br>

JS 也可以直接改 CSS。

```javascript
const box = document.querySelector(".box");

// 1. 直接改 style 屬性 (駝峰式命名)
box.style.backgroundColor = "red"; // background-color -> backgroundColor
box.style.fontSize = "24px";
box.style.display = "none"; // 隱藏元素

// 2. 透過 Class 切換 (推薦！)
box.classList.add("active");    // 加上 .active
box.classList.remove("active"); // 移除 .active
box.classList.toggle("active"); // 切換 (有就刪，沒有就加)
```

---

# 事件監聽

<br>

網頁要互動，就要監聽使用者的動作 (事件)。

```javascript
const btn = document.getElementById("myBtn");

// 當按鈕被點擊 (click) 時，執行函式
btn.addEventListener("click", function() {
    alert("你按到我了！");
});
```

### 常用事件：
-   `click`：滑鼠點擊。
-   `mouseenter` / `mouseleave`：滑鼠移入/移出。
-   `keydown`：鍵盤按下。
-   `submit`：表單送出。
-   `scroll`：網頁捲動。

---

# 實作練習：計數器

<br>

做一個有 `+` 和 `-` 按鈕的計數器。

### HTML:
```html
<h1 id="count">0</h1>
<button id="btn-add">+1</button>
<button id="btn-sub">-1</button>
```

### JavaScript:
1.  抓取三個元素。
2.  宣告一個變數 `num = 0`。
3.  監聽 `+` 按鈕：`num` 加 1，更新 `h1`。
4.  監聽 `-` 按鈕：`num` 減 1，更新 `h1`。

---

# 實作練習：背景變色器

<br>

做一個按鈕，按下去隨機改變網頁背景顏色。

```javascript
const btn = document.getElementById("bg-btn");

btn.addEventListener("click", function() {
    // 產生隨機顏色
    const r = Math.floor(Math.random() * 256);
    const g = Math.floor(Math.random() * 256);
    const b = Math.floor(Math.random() * 256);
    
    // 套用到 body 背景
    document.body.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;
});
```

> **Math.random()**：產生 0 ~ 1 之間的小數。
> **Math.floor()**：無條件捨去取整數。

---

# 總結：DOM 操作三部曲

<br>

任何網頁互動，基本都脫離不了這三個步驟：

1.  **選取**：用 `querySelector` 找到你要控制的 HTML 標籤。
2.  **監聽**：用 `addEventListener` 監聽使用者的動作。
3.  **反應**：在函式裡面，修改 DOM 的內容或樣式。

---

# 下週預告

<br>

現在我們的網頁在電腦看很漂亮，但在手機看可能就跑版了。

**響應式網頁設計**
-   如何讓網頁適應手機、平板、桌面？
-   深入 Media Queries。
-   Flexbox 和 Grid 在 RWD 的應用。
-   行動優先 (Mobile First) 的設計思維。

準備拿出你的手機來測試網頁吧！

---
