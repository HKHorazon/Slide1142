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

###  Ch. 2

# 程式語言 與 C#

## Horazon
## C#程式設計

---
# 名詞解釋

## 程式
是指一組指示電腦或其他具有訊息處理能力的電子裝置<mark>每一步動作的指令</mark>，通常用某種程式設計語言編寫，執行於某種目標體系結構上

## 程式語言
一套用於定義程式(電腦如何工作)的<mark>詞彙和語法規則</mark>。

---
# 程式語言的種類

### 低階語言
* 機械語言
* 組合語言
### 高階語言
* 程序性語言 (FORTRAN, COBAL, C ..)
* 物件導向語言 (C++, VB, Java, C# ..)
* 應用軟體語言 (VBA, Javascript ..)

---
# 高階與低階語言
#### 電腦只能閱讀機械語言，高階語言是給人類閱讀的
* 我們學習的程式語言幾乎都是高階語言
* 電腦必須藉由編譯器 或 直譯器 將高階語言轉換為機械語言
<!-- 向右移動 -->
<style scoped>
img {
  transform: translateX(500px) translateY(20px);
}
</style>
![HighVsLow](../../IMAGE/CSharp/Ch2/CSharp_Ch02_02.gif)

---
# 編譯器與直譯器
#### 編譯器 (Compiler)
- 完整閱讀程式碼再建立執行檔
- C++, Java, C#
#### 直譯器 (Interpreter)
- 一行一行閱讀並執行
- Python, JavaScript

<br>
編譯器 與 直譯器都是一個程式，通常由另一種程式語言(常見為c++)撰寫


---
# 如何撰寫程式

打開記事本，寫一段程式並存檔

要求Compiler讀取該程式碼並編譯

獲得一個執行檔，即可執行
<br><br>
這樣就可以撰寫並執行程式，但太不方便了..

---
# 整合開發環境 (IDE)

**Integrated Development Environment**
* 一種輔助程式開發人員開發軟體的應用軟體

* 適用於一或多種程式語言

* 高亮關鍵字、外框、行號等

* 自動提示、完成程式碼、AI整合等

* 如：Visual Studio, Eclipse

---
# C# (C Sharp) 本堂課的程式語言

#### 起源：C -> C++ -> Java -> C# 
* 2000年 、 微軟
#### 特性
* 物件導向
* 編譯器
* .NET框架
#### 最新版本 : C# 13 
#### 穩定版本 : C# 8 

---
# Microsoft Visual Studio
<br>

#### 下載與安裝
https://visualstudio.microsoft.com/zh-hant/downloads/
<br>

建議註冊微軟帳號、能註冊Github帳號更好

實際上，可以使用其他IDE，如VS Code來撰寫會更方便
但是需要額外安裝一些套件

