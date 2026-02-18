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

### Chapter 11
# 程式邏輯入門 - JavaScript 基礎

## Horazon
## 互動媒體設計 (一學期)

---

# 為什麼要學 JavaScript?

<br>

HTML 是骨架，CSS 是皮膚，JavaScript (JS) 是**靈魂**。

-   **沒有 JS 的網頁**：像是一張海報，只能看，不能動。
-   **有 JS 的網頁**：像是一個應用程式，可以跟你互動。
    -   點按鈕跳出視窗。
    -   檢查表單有沒有填錯。
    -   從伺服器抓取資料 (例如天氣、股價)。
    -   製作網頁遊戲。

> **JavaScript 是目前世界上最熱門的程式語言，沒有之一。**

---

# Hello World

<br>

我們怎麼開始寫 JS？

1.  在 HTML 裡面，用 `<script>` 標籤包起來。
2.  通常放在 `<body>` 的**最下面** (確保 HTML 載入完了才執行 JS)。

```html
<body>
    <h1>我的網頁</h1>
    
    <script>
        alert("Hello World!"); // 跳出警告視窗
        console.log("你好，控制台！"); // 在 Console 印出訊息
    </script>
</body>
```

> **Console 在哪？**
> 按 `F12` 開發者工具 -> 切換到 `Console` 分頁。

---

# 變數 - 記憶體的盒子

<br>

變數就是用來**存資料**的盒子。

### 宣告方式 (ES6 標準)：
1.  **`let`**：一般的變數，數值**可以**改變。
    -   `let score = 100;`
    -   `score = 90;` (OK!)
2.  **`const`**：常數，數值**不能**改變。
    -   `const pi = 3.14;`
    -   `pi = 3.14159;` (Error! 會報錯)

> **`var`** 是舊時代的寫法，盡量少用 (因為它的作用域很混亂)。

---

# 資料型別

<br>

JS 裡的資料分幾種：

1.  **Number (數字)**：`10`, `3.14`, `-5`。
2.  **String (字串)**：用引號包起來的文字。
    -   `"Hello"`, `'你好'`, `` `模板字串` ``。
3.  **Boolean (布林)**：只有兩種，`true` (真) 或 `false` (假)。
4.  **Array (陣列)**：一排盒子，存多個資料。
    -   `let fruits = ["Apple", "Banana", "Orange"];`
5.  **Object (物件)**：有多個屬性的複雜東西。
    -   `let student = { name: "John", age: 18 };`

---

# 運算子

<br>

-   **算術運算**：`+`, `-`, `*`, `/`, `%` (取餘數)。
    -   **注意**：字串相加是「串接」。
    -   `"10" + 20` 變成 `"1020"` (不是 30 喔！)。
-   **比較運算**：
    -   `>` (大於), `<` (小於), `>=` (大於等於)。
    -   `===` (嚴格等於)：數值和型別都要一樣。
    -   `!==` (不等於)。
    -   *盡量不要用 `==` (寬鬆等於)，它會亂轉型。*
-   **邏輯運算**：
    -   `&&` (AND, 且)：兩邊都要對，才是對。
    -   `||` (OR, 或)：只要有一邊對，就是對。
    -   `!` (NOT, 非)：把對變錯，錯變對。

---

# 條件判斷 (If...Else)

<br>

讓程式有「思考」的能力。

```javascript
let score = 85;

if (score >= 60) {
    console.log("及格！");
} else {
    console.log("被當了 QQ");
}
```

還可以有多個條件：
```javascript
if (score >= 90) { ... }
else if (score >= 80) { ... }
else { ... }
```

---

# 迴圈

<br>

讓程式幫你做重複的事。

### For 迴圈 (固定次數)
```javascript
// 印出 0 到 4
for (let i = 0; i < 5; i++) {
    console.log("第 " + i + " 次執行");
}
```

### 陣列迴圈 (遍歷資料)
```javascript
let fruits = ["Apple", "Banana", "Orange"];

fruits.forEach(function(item) {
    console.log("我喜歡吃 " + item);
});
```

---

# 函式 - 打包程式碼

<br>

把一堆程式碼包成一個指令，隨時可以呼叫。

### 定義函式：
```javascript
function sayHello(name) {
    console.log("你好，" + name + "！");
}
```

### 呼叫函式：
```javascript
sayHello("小明"); // 印出：你好，小明！
sayHello("阿華"); // 印出：你好，阿華！
```

> **參數**：括號裡的 `name`，是我們傳進去的資料。

---

# 實作練習：BMI 計算機 (邏輯版)

<br>

請在 Console 裡寫一個計算 BMI 的程式：

1.  定義變數 `height` (身高，公尺) 和 `weight` (體重，公斤)。
2.  計算 BMI = 體重 / (身高 * 身高)。
3.  使用 `if...else` 判斷：
    -   BMI < 18.5: "過輕"
    -   18.5 <= BMI < 24: "正常"
    -   BMI >= 24: "過重"
4.  用 `console.log` 印出結果。

```javascript
let h = 1.75;
let w = 70;
// ... (請自己寫寫看)
```

---

# 下週預告

<br>

今天的程式碼都只能在黑黑的 Console 裡面跑，很無聊吧？
下週我們要讓 JS 來控制 HTML！

**網頁互動實作 - DOM 操作與事件**
-   如何按一個按鈕就改變背景顏色？
-   如何把 BMI 的結果顯示在網頁上？
-   什麼是 DOM (Document Object Model)？

準備好，下週你的網頁就會「活」過來了！

---
