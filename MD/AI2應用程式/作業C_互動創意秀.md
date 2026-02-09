---
marp: true
theme: HoraStyle
paginate: true
style: |
  :root {
    --title-bg: linear-gradient(90deg, #7c3aed, #ec4899);
    --title-text-color: #ffffff;
  }
  section.lead {
    background: linear-gradient(135deg, #4c1d95 0%, #000000 100%);
  }
  table {
    font-size: 24px;
    margin-left: auto;
    margin-right: auto;
  }
---

<!-- _class: lead -->
<!-- _paginate: false -->

### 作業 C (期末)

# 互動創意秀 App

## 應用程式設計
## 繳交期限：第 16 週

---

# 作業說明

製作一個 **多媒體互動 App**，展現你這學期學到的所有技能！

### 主題 (3選1)
1. **打地鼠遊戲** ─ Canvas 動畫遊戲
2. **會說話的計算機** ─ 多媒體應用
3. **自訂主題專案** ─ 發揮創意！

<br>

<mark>這是期末作業，佔成績比例較重，請認真完成！</mark>

---

# 主題 1：打地鼠遊戲

製作經典的「Whack-a-Mole」遊戲！

### 畫面元件
- 一個 **Canvas**：遊戲區域
- 一個 **ImageSprite**：地鼠圖片
- 一個 **Label**：分數顯示
- 一個 **Button**：開始遊戲 / 重新開始
- 一個 **Clock**：計時器 (用來控制地鼠移動)

---

# 打地鼠：程式邏輯

### 核心流程
1. 按下「開始」按鈕，啟動 Clock 計時器
2. 每隔一段時間 (例如 1 秒)，地鼠隨機移動到新位置
3. 玩家點到地鼠 (ImageSprite.Touched) → 分數 +1
4. 遊戲時間到 (例如 30 秒) → 停止計時器，顯示最終分數

### 要用到的積木
- `ImageSprite.MoveTo(x, y)`：移動地鼠
- `隨機整數`：產生隨機座標
- `Clock.Timer` 事件：每秒觸發
- `全域變數 score`：累計分數

---

# 打地鼠：加分挑戰

讓遊戲更有趣！

### 進階功能 (選做)
- 🎵 打到地鼠時播放音效 (Sound 元件)
- ⏱️ 顯示倒數計時
- 🏆 遊戲結束後用 **TextToSpeech** 唸出「恭喜你得到 X 分！」
- 📱 使用 **多畫面**：開始畫面 → 遊戲畫面 → 結算畫面

---

# 主題 2：會說話的計算機

製作一個「語音互動」計算機！

### 畫面元件
- 兩個 **TextBox**：輸入數字
- 四個 **Button**：加減乘除
- 一個 **Label**：顯示結果
- 一個 **TextToSpeech**：語音輸出
- 一個 **SpeechRecognizer** (選做)：語音輸入

---

# 會說話的計算機：程式邏輯

### 核心功能
1. 輸入兩個數字，按下運算按鈕
2. 計算結果顯示在 Label
3. 用 **TextToSpeech.Speak** 把結果唸出來
   - 例如：「10 加 5 等於 15」

### 選做功能：語音輸入
1. 加一個「說話輸入」按鈕
2. 呼叫 **SpeechRecognizer.GetText**
3. 在 **SpeechRecognizer.AfterGettingText** 事件中，把聽到的數字填入 TextBox

---

# 會說話的計算機：加分挑戰

### 進階功能 (選做)
- 🎨 用 **Canvas.DrawText** 把算式畫在畫布上
- 📜 用 **清單 (List)** 記錄歷史計算紀錄
- 🔊 加入按鈕音效

---

# 主題 3：自訂主題專案

如果你有自己的創意想法，歡迎自訂主題！

### 規定
1. 必須用到 **至少 5 種以上** 不同的元件類型
2. 必須包含 **以下技能中的至少 4 項**：
   - 變數
   - 判斷式 (If/Else)
   - 迴圈 (For / While)
   - 清單 (List)
   - 多畫面 (Screen)
   - 多媒體 (Sound / TextToSpeech)
   - Canvas 動畫

3. 需事先與老師討論題目

---

# 自訂主題範例

以下是一些可以參考的方向：

| 類型 | 專案範例 |
|:---|:---|
| 🎮 遊戲 | 接球遊戲、躲避障礙物、記憶翻牌 |
| 📝 工具 | 待辦清單、記帳本、倒數計時器 |
| 📚 學習 | 英文單字卡、數學練習、問答遊戲 |
| 🎨 創意 | 繪圖板、音樂播放器、故事書 |

<br>

<mark>自訂主題可獲得創意加分！</mark>

---

# 評分標準

| 項目 | 配分 | 說明 |
|:---|:---:|:---|
| **完整度** | 35% | App 功能完整、可正常運作 |
| **技術應用** | 30% | 正確使用所學技能 |
| **介面設計** | 20% | 版面美觀、操作直覺 |
| **創意表現** | 15% | 有自己的想法與特色 |

### 加分項目
- 使用多媒體元件 (Sound/TTS)：+5 分
- 使用 Canvas 動畫：+5 分
- 多畫面完整設計：+5 分

---

# 繳交方式

### 需繳交兩樣東西：

1. **應用程式安裝檔 (.apk)**
   - 建置方式：Build → Android App (.apk)
   - 檔名：`作業C_學號_姓名.apk`

2. **簡報或說明文件**
   - 說明你的 App 功能、設計理念
   - 可用 PPT、Word 或 PDF
   - 檔名：`作業C_學號_姓名_說明.pdf`

### 上傳至學校 Moodle

---

# App 設定提醒

在打包前，記得設定好這些項目：

### Screen1 屬性
- **Title**：你的 App 名稱
- **Icon**：上傳一張自訂圖示 (建議 512x512)

### 打包步驟
1. Build → Android App (.apk)
2. 等待編譯完成
3. 測試 APK 是否能正常安裝運作

---

# 涵蓋技能 (全課程)

這份作業是期末總驗收！

| 技能類別 | 內容 |
|:---|:---|
| 基礎元件 | Button, Label, TextBox, Image |
| 排版 | Layout, Fill Parent |
| 資料處理 | 變數, 清單, Join |
| 流程控制 | If/Else, For Loop, While |
| 進階元件 | Notifier, Clock, Canvas |
| 多媒體 | Sound, TextToSpeech, SpeechRecognizer |
| 動畫 | ImageSprite, Ball, Touched, MoveTo |
| 架構 | Multi-Screen, Start Value |

---

# 期末發表

在繳交作業後，將進行現場發表！

### 發表流程
1. **Demo 展示** (2~3 分鐘)：操作你的 App
2. **技術說明** (1~2 分鐘)：解釋核心邏輯
3. **Q&A** (1 分鐘)：回答問題

### 評分
期末發表分數也會納入期末作業成績。

<br>

### 恭喜你完成這學期的學習！🎉
