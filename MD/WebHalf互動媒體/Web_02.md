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

# 網頁三大元素

## Horazon
## 互動媒體

---

# 3D模型 的 三大元素

如果要創造一個虛擬角色(3D模型)，我們需要什麼？
<br>

1. **骨架** (你是誰？有哪些部分？)

2. **衣服與外型** (你長什麼樣？好看嗎？)

3. **大腦與動作** (你會做什麼？點了會動嗎？)


---

# MVC

如果要建立網頁，也會有前段提到的骨架、外型、動作
在程式相關會有一個說明這種拆分的方式
稱之為 MVC ，分別是
<br>
**Model(模型)**：實際的骨架與內容

**View(外觀)**：美化網頁

**Control(控制)**：處理動作

---
# 網頁的MVC

而在網頁，分別有三種(標記/程式)語言對應這三個項目
<br>

**Model(模型)**：<mark>HTML</mark>，實際的骨架與內容

**View(外觀)**：<mark>CSS</mark>，美化網頁

**Control(控制)**：<mark>JavaScript</mark>，處理動作

---

# HTML

**全名：** HyperText Markup Language 
- 超文本標記語言，它不是一種程式語言

**任務：** 定義網頁有哪些內容。

**功能：** 告訴電腦「這裡有一顆頭」、「這裡有一隻手」。
<br>

```html
<button>我是一個按鈕</button>
<p>我是一段文字</p>
```

---

# CSS

**全名：** Cascading Style Sheets
- 階層式樣式表，它不是一種程式語言

**任務：** 負責美化，讓網頁變漂亮。

**功能：** 告訴電腦 文字是粉紅色、字體大小等等。
<br>

```css
button {
  background-color: pink;
  font-size: 20px;
}
```

---

# Java Script / JS

**全名：** Java Script 
- 直譯式程式語言 (和 Java 沒關係！)

**任務：** 處理動作、反應、計算。

**功能：** 點了按鈕會「跳舞」，或是點了角色會「說話」。

```js
function OnClick() {
    alert("你點到我了！痛！");
}
```

---

# 三元素合成

合起來的功能就是..

**Model(模型)**：<mark>HTML</mark>，畫出一個按鈕

**View(外觀)**：<mark>CSS</mark>，設定按鈕的邊框、顏色

**Control(控制)**：<mark>JavaScript</mark>，按鈕按下去的功能

<br>
撰寫以上的三種功能不一定是同一個人

其實遊戲開發或其他程式，也有所謂的MVC概念