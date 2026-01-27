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

### Chapter 04
# VS Code

## Horazon
## 互動媒體設計

---

# 為什麼需要工具？

寫網頁就像寫文章，雖然用「記事本」也能寫，但是...

- **沒有顏色**：很難分辨標籤與內容
- **沒有提示**：全部都要自己背
- **沒有除錯**：寫錯了找不到

所以，我們需要一個強大的**編輯器**！

---

# 什麼是 VS Code?

- **全名**：Visual Studio Code
- **出身**：微軟 (Microsoft) 開發
- **優點**：
  1. **免費** (Open Source)
  2. **輕量** (不會讓電腦跑不動)
  3. **擴充性強** (想要什麼功能都有)

---

# Step 1: 下載與安裝

1.前往官網：[code.visualstudio.com](https://code.visualstudio.com/)
2.點擊 **Download for Windows** (或是 Mac)
3.下載後執行安裝檔
4.安裝過程**一路按「下一步」** (Next) 即可


---

# Step 2: 認識介面

打開 VS Code，你會看到...

- **左側欄 (Activity Bar)**：最重要的導航區
  - **檔案總管**：管理你的資料夾與檔案
  - **搜尋**：找字串
  - **擴充功能 (Extensions)**：安裝外掛的地方 (像四個方塊的圖示)
- **中間**：編輯程式碼的地方
- **下方**：狀態列 (顯示行號、編碼等)

---

# Step 3: 安裝關鍵套件 (Extensions)

點擊左側的 **擴充功能**  圖示，搜尋並安裝：

1. **Chinese (Traditional) Language Pack**
   - 讓介面變成**繁體中文** (安裝後需重啟)。
2. **Live Server**
   - 讓你的電腦變成小型伺服器，**即時預覽**網頁。
   - 作者：Ritwick Dey
3. **Prettier - Code formatter**
   - 幫你**自動排版**，讓程式碼整齊漂亮。

---

# Step 4: 建立第一個專案

1. 在桌面上建立一個**新資料夾**，命名為 `MySite`。
2. 回到 VS Code，點選 **「檔案」** > **「開啟資料夾」**。
3. 選擇剛剛的 `MySite` 資料夾。

> **注意**：不要直接開啟單一檔案，**養成「開啟資料夾」的好習慣**！

---

# Step 5: 建立 HTML 檔案

1. 在左側「檔案總管」的空白處按右鍵 (或點擊新增檔案圖示)。
2. 輸入檔名：`index.html`。
3. 按下 Enter。

> 為什麼叫 `index`？
> 因為瀏覽器預設會尋找名為 `index` 的檔案作為**首頁**。

---

# Step 6: 寫入第一段程式碼

1. 在編輯區輸入驚嘆號 `!`。
2. 按下 **Tab** 鍵 (或是 Enter)。
3. 神奇的事情發生了！VS Code 會自動幫你產生 HTML 基本骨架。

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

---

# Step 7: 預覽網頁 (Live Server)

1. 在 `<body>` 與 `</body>` 之間，輸入 `<h1>Hello World</h1>`。
2. 記得**存檔** (`Ctrl + S` / `Cmd + S`)。
3. 在編輯區按**右鍵**，選擇 **"Open with Live Server"**。
4. 瀏覽器會自動彈出，顯示你的網頁！

---

# 常見快速鍵 (必記)

- **存檔**：`Ctrl + S`
- **複製一行**：`Shift + Alt + 下`
- **移動一行**：`Alt + 上/下`
- **註解**：`Ctrl + /`
- **放大/縮小字體**：`Ctrl + +` / `Ctrl + -`

---

# 重點回顧

1. 下載並安裝 VS Code。
2. 安裝 **中文包** 與 **Live Server**。
3. 使用 **「開啟資料夾」** 來管理專案。
4. 建立 `index.html`。
5. 輸入 `!` + `Tab` 產生骨架。
6. 右鍵 **Open with Live Server** 預覽。
