---
marp: true

theme: HoraStyle
paginate: true
style: |
  :root {
    --title-bg: linear-gradient(90deg, #2563eb, #3b82f6);
    --title-text-color: #ffffff;
  }
  section.lead {
    background: linear-gradient(135deg, #172554 0%, #000000 100%);
  }
---


<!-- _class: lead -->
<!-- _paginate: false -->

### Ch. 4
# 變數宣告與使用
## Horazon
## C#程式設計

---

# 程式學習地圖 (初步、核心邏輯)

#### 基本結構
#### <mark>變數宣告</mark>
#### 循序
#### 選擇 (if, switch)
#### 迴圈 (for, while, do-while)


---
# 程式碼：為什麼需要變數

```cs
Console.WriteLine("你好, Horazon!");
```
在程式使用中，如果都是一成不變的輸出文字，是無法發揮電腦功能的。
我們要製作一個可以修改的 **容器** 來儲存資料


---

# 什麼是變數 (Variables)？

* **定義**：變數是電腦記憶體中用來儲存資料的「容器」。
* **概念**：你可以把它想像成一個貼有**標籤**的**盒子**。
    * **標籤** = 變數名稱 (Name)
    * **盒子大小/種類** = 資料型別 (Data Type)
    * **內容物** = 儲存的值 (Value)



---

# 變數的宣告與賦值

在 C# 中，使用變數前必須先宣告其型別。

**基本語法：**
資料型別 變數名稱 = 初始值;

```csharp
// 範例：儲存玩家分數
int score = 100;

// 範例：儲存玩家名稱
string playerName = "Gemini";

// 範例：儲存身高
double height = 175.5;
```

---

# 常用資料型別




型別 | 說明 | 範例 
-----|------|:-----:
int | 整數 |  20, -2
double | 雙精度浮點數 | 3.21, -0.5
float | 單精度浮點數 | 10.0f, 5f 
bool | 真假值/布林 | true,false
string | 字串 | "你好","Hello"

---

# 命名規則 (Camel Case)

## 好的命名能讓程式更好讀：

✅ userAge, totalPrice (小駝峰式)

✅ itemNo1, itemNo2 (小駝峰式 後面使用數字)

⚠️ MyName, UnitLife (大駝峰式Pascal Case，可以使用但不建議)

⚠️ 年齡, 身高 (中文可使用，但不建議)

❌ 123name (不能數字開頭)

❌ my name (不能有空格)

---

# 使用變數

在這個例子中，我們宣告變數、賦值、並使用它們
請嘗試修改成自己的名字，並且將分數改為100分
```cs
using System;

var myName = "小明";
int score = 95;

Console.WriteLine(myName+" 的分數是 "+score+" 分");
```

---
# 輸出技巧
```cs
using System;

var myName = "小明";
int score = 95;

Console.WriteLine(myName+" 的分數是 "+score+" 分");
```
這段程式碼中，輸出部分使用 + 來連接文字與變數，
經常使用後會有點麻煩，我們可以改為使用<mark> $ ( format )</mark>

```cs
Console.WriteLine($"{myName} 的分數是 {score} 分");
```

---

# 變數重新賦值

變數就像一個**盒子**，在程式執行的過程中，你可以隨時更換盒子裡裝的資料。

* **第一次賦值**：稱為「初始化」(Initialization)。
* **重新賦值**：用新的值「覆蓋」舊的值。

<br>
當你要改變變數的值時，<mark>不需要</mark>再次寫出型別（如 `int` 或 `string`）。

```cs
int score = 100;    // 建立變數並給予初始值 100
score = 80;         // 重新賦值為 80 (舊的 100 消失了)
score = 50;         // 再次更換為 50
```

---
# 常數 (Constant)

常數(const)使用規則
- 必須在宣告的時候賦予初始值
- 之後不能再改變它的數值

```cs
const double Pi = 3.14159;
const int MaxSpeed = 120;
const string AppName = "我的應用程式";
```

---
# 常見錯誤：重複宣告

已使用過的變數名稱不能再次使用，就算是不同型態也不行

```cs
int score = 90;
double score = 90.5;    //此行錯誤❌
```
<br>
以上程式碼會發生錯誤

---
# 常見錯誤：賦值型態錯誤

你必須賦予相同型態的數值，否則會發生錯誤

```cs
int score = 90.5;           //此行錯誤❌

string myName = "Horazon";
myName = 50;                //此行錯誤❌
```

---
# 常見問題：常數

沒有給予常數初始值

```cs
double PI;              //此行錯誤❌
```
<br>

對常數重新賦值
```cs
string myName = "Horazon";
myName = "Horazon2";    //此行錯誤❌
```



