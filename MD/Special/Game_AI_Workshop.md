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
    background: linear-gradient(135deg, #1e3a8a 0%, #000000 100%);
  }
  table {
    font-size: 26px;
    margin-left: auto;
    margin-right: auto;
  }
---

<!-- _class: lead -->
<!-- _paginate: false -->

# AI 遊戲開發工作坊
## Game Development with AI

### 仕明 老師 (Horazon)

---

# 課程目標
## Goal of this Workshop

在 **2.5 小時** 內，體驗遊戲開發的樂趣！

1. **認識遊戲引擎**：使用 2D 橫向捲軸 (Side-Scrolling) 模板
2. **AI 輔助程式**：讓 ChatGPT 幫你寫程式
3. **創意發想**：為遊戲加入你的獨特功能

---

# 為什麼要用遊戲引擎？
## Why use a Game Engine?

想像你要**蓋房子**：
- **不用遊戲引擎 (No Engine)**：從燒磚塊、砍樹、製作水泥開始。 (太慢了！Too slow!)
- **使用遊戲引擎 (With Engine)**：你有現成的牆壁、窗戶、地基。只要**組裝**起來就好。

**遊戲引擎幫你處理了難搞的事：**
- 物理運算 (Physics)
- 畫面渲染 (Graphics)
- 聲音播放 (Audio)

---

# 常見遊戲引擎比較
## Common Game Engines

| Engine | 特色 (Feature) | 適合 (Best for) | 難度 (Difficulty) |
|:---:|:---|:---|:---:|
| **Unity** | 通用性強、資源多 | 手遊、2D/3D、獨立遊戲 | ⭐⭐⭐ |
| **Unreal** | 畫面頂級、藍圖系統 | 3A 大作、寫實風格 | ⭐⭐⭐⭐⭐ |
| **Godot** | 輕量、開源免費 | 2D 遊戲、快速原型 | ⭐⭐ |

> **我們今天選擇 Unity**，因為它最適合初學者入門且資源最豐富！

---

# 這些都是用 Unity 做的！
## Made with Unity

| | |
|:---:|:---:|
| **Genshin Impact** (原神) | **Pokémon GO** |
| **Among Us** | **Fall Guys** |
| **Hollow Knight** (空洞騎士) | **Overcooked!** |

> **其實你常玩的遊戲，很多都是 Unity 做的！**

---

# 這是什麼課程？

我們**不用**從頭開始寫程式！
主要任務是：
1. **玩**：先跑通既有的遊戲。
2. **想**：你想要加什麼功能？（障礙物？敵人？金幣？）
3. **問**：學會怎麼「命令」AI 幫你實現願望。

---

# 你的工具箱 (Toolkit)

1. **Unity 遊戲引擎** (或者是我們提供的 2D 引擎)
2. **2D 橫向捲軸模板** (Template)
3. **Generative AI** (ChatGPT / Claude / Gemini)

---

# 步驟 1：打開模板
## Open the Template

1. 下載並解壓縮專案檔。
2. 開啟對應的場景 (Scene)。
3. 按下 **Play** 按鈕試玩看看！
   - 它可以移動嗎？
   - 它可以跳躍嗎？

---

# 認識我們的模板
## Meet our Template

我們的遊戲非常簡單，由三個部分組成：

1. **主角 (Player)**：你可以控制它左右移動和跳躍。
2. **場景 (Level)**：地板、牆壁、障礙物。
3. **終點 (Flag)**：遊戲的目標！

### 🏆 獲勝條件 (Win Condition)
> **主角 碰到 旗子 = 獲勝！**
> **Player touches Flag = Win!**

---

# 認識 Unity 介面
## Unity Interface 5 Major Windows

1. **Hierarchy (階層)**：遊戲裡有哪些東西？ (清單)
2. **Scene (場景)**：編輯遊戲的世界 (上帝視角)
3. **Game (遊戲)**：玩家看到的畫面 (鏡頭視角)
4. **Inspector (屬性)**：調整物件的大小、顏色、數值
5. **Project (專案)**：你的倉庫 (所有圖片、聲音、腳本)

---

# 編輯你的世界 (Tilemap)
## Editing the World

遊戲場景是一塊一塊畫出來的！

1. 開啟 **Tile Palette** 視窗 (`Window > 2D > Tile Palette`)
2. 選擇 **筆刷 (Brush)** 工具
3. 選取你要的 **地板 (Tile)**
4. 在場景中 **畫 (Paint)** 出你的關卡！

> **Tip**: 記得畫在 Grid 物件下的正確 Layer 哦！

---

# 更多好東西 (Prefabs)
## Using Prefabs

除了畫地圖，我們還有現成的**物件**可以放！

1. 找到 **Prefabs** 資料夾
2. 把你想要的東西 **拖 (Drag)** 進場景：
   - 🚩 **旗幟 (Flag)** (遊戲目標)
   - 🚧 **其他障礙物 (Obstacles)**

> **就像佈置房間一樣簡單！**

---

# 旗幟的功能
## Flag Logic

為什麼碰到旗子會贏？因為它有 **程式碼**！
Why does touching the flag make you win? Because it has **Code**!

```csharp
void OnTriggerEnter2D(Collider2D other) 
{
    // 如果碰到的是主角 (Player)
    if (other.name == "Player") 
    {
        Debug.Log("You Win!"); // 顯示獲勝訊息
    }
}
```

> **這就是所謂的「腳本 (Script)」！**

---

# 步驟 2：認識 AI 助手
## Meet your AI Copilot

我們雖然不會寫複雜的 C# 程式碼，但我們知道**遊戲邏輯**。

**只要你能描述清楚，AI 就能幫你寫出來！**

---

# 步驟 3：如何提問？ (Prompting)

### ❌ 不好的問法
> "幫我做一個好玩的遊戲。"
> (太模糊，AI 不知道你要什麼)

### ✅ 好的問法
> "我現在有一個 Unity 2D 專案。我想要讓主角按下 'Space' 鍵時可以**發射子彈**。
> 請提供一個簡單的 C# 腳本，並告訴我如何掛載到主角身上。"

---

# 實作挑戰：增加功能！
## Challenge Time

請嘗試加入以下任一個功能：

1. **二段跳 (Double Jump)**
2. **衝刺 (Dash)**
3. **受傷變色 (Hurt Effect)**
4. **吃到金幣的音效 (Coin Sound)**

---

# 範例：二段跳 (Double Jump)

**Prompt (提示詞):**
> "我正在製作一個 Unity 2D 平台遊戲。
> 請幫我修改一段角色控制腳本，讓我可以在空中多跳一次 (Double Jump)。
> 請給我變數 `jumpCount` 來控制跳躍次數。"

---

# 製作時間 (1.5 小時)
## Production Time

1. **修改**：調整變數 (速度、跳躍力)
2. **新增**：利用 AI 撰寫新腳本
3. **測試**：確保遊戲可以執行

---

# 成果發表
## Show & Tell

- 你的遊戲多了什麼功能？
- 你用 AI 解決了什麼問題？
- 最好玩的地方在哪裡？

---

# 結語

程式語法不再是障礙。
**想像力** 才是你的超能力！

### Have Fun!
