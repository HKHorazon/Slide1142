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
### Homework 3
# C# 程式設計
## 課後練習 作業三
## 物件導向 (OOP) 實戰挑戰
### (交通工具系統設計)

---

# 📝 繳交方式

### 請將以下 3 個題目的 C# 程式碼打包繳交：
- **作業一**：封裝 - 汽車類別實作
- **作業二**：繼承 - 腳踏車與交通工具
- **作業三**：抽象與多型 - 交通工具啟動系統

*   **格式**：`.zip` / `.rar` / `.7z` 壓縮檔
*   **注意**：將所有程式碼放在同一個專案，並且打包給我。

---

# 🚗 作業一：封裝 (Encapsulation)

### 🎯 需求說明
請設計一個 `Car` (汽車) 類別，將品牌與剩餘油量封裝起來，並提供駕駛方法。

### 📋 類別規格 (UML)
<div style="text-align: center; margin-top: 10px;">
  <img src="../../MERMAID/IMAGE/CSharp_13_HW_Q1.png" height="200">
</div>

---

# 🚗 作業一：輸出要求與提示

### 執行要求 (在 Main 方法中)：
1. 建立 `Car` 的實例。
2. 將 `Brand` 設定為 `"Toyota"`，`Fuel` 設定為 `50`。
3. 呼叫 `Drive()` 方法。

### 🖥️ 預期主控台輸出：
```
Toyota 汽車出發！目前剩餘油量：50
```

### 💡 提示：
* 類別內的欄位與方法皆需要使用 `public` 修飾詞。

---

# 🚲 作業二：繼承 (Inheritance)

### 🎯 需求說明
請建立一個基礎交通工具類別 `Vehicle`，並建立子類別 `Bicycle` (腳踏車) 繼承它，實現屬性的共用與擴充專屬方法。

### 📋 類別規格 (UML)
<div style="text-align: center; margin-top: 10px;">
  <img src="../../MERMAID/IMAGE/CSharp_13_HW_Q2.png" height="220">
</div>

---

# 🚲 作業二：輸出要求與提示

### 執行要求 (在 Main 方法中)：
1. 建立 `Bicycle` 的實例。
2. 設定其品牌 `Brand` 為 `"Giant"`，速度 `Speed` 為 `15`。
3. 印出品牌與速度，並呼叫 `RingBell()` 方法。

### 🖥️ 預期主控台輸出：
```
腳踏車品牌：Giant，目前速度：15 km/h
叮叮！腳踏車按了鈴鐺。
```

### 💡 提示：
* 使用 **冒號 `:`** 來進行類別繼承（例如 `class Bicycle : Vehicle`）。

---

# 🎭 作業三：抽象與多型

### 🎯 需求說明
請將 `Vehicle` 類別改為**抽象類別**，並定義抽象方法 `Move()`，強迫 `Car` 與 `Bicycle` 實作各自的移動方式。

### 📋 類別規格 (UML)
<div style="text-align: center; margin-top: 10px;">
  <img src="../../MERMAID/IMAGE/CSharp_13_HW_Q3.png" height="200">
</div>

---

# 🎭 作業三：輸出要求與提示

### 執行要求 (在 Main 方法中)：
1. 宣告一個 `Vehicle` 類別的陣列 (長度為 2)。
2. 分別將 `Car` 與 `Bicycle` 物件裝入陣列。
3. 使用 `foreach` 迴圈遍歷陣列，統一呼叫 `Move()` 方法。

### 🖥️ 預期主控台輸出：
```
汽車開動：轟隆隆！
腳踏車出發：踩踩踩！
```

### 💡 提示：
* 使用 `abstract` 定義抽象類別與方法，並在子類別使用 `override` 覆寫。
* 利用 `Vehicle[]` 陣列來實現多型的管理。
