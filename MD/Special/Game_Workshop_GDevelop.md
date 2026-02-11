---
marp: true
theme: HoraStyle
paginate: true
style: |
  :root {
    --title-bg: linear-gradient(90deg, #9333ea, #7e22ce);
    --title-text-color: #ffffff;
  }
  section.lead {
    background: linear-gradient(135deg, #581c87 0%, #000000 100%);
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

## Game Development
## Horazon

---

# 課程目標
## Goal of this Workshop

在 **極短時間** 內，體驗遊戲開發的樂趣！

1. **認識遊戲引擎**：為什麼我們需要它？
2. **選擇工具**：為什麼今天是 GDevelop？
3. **AI 輔助**：讓 AI 成為你的隊友

---

# 為什麼要用遊戲引擎？
## Why use a Game Engine?

想像你要**蓋房子**：
- **不用遊戲引擎**：從燒磚塊、砍樹、製作水泥開始。 (太累了！)
- **使用遊戲引擎**：你有現成的牆壁、窗戶、地基。只要**組裝**起來就好。

**遊戲引擎幫你處理了難搞的事：**
- 物理運算 (Physics)
- 畫面渲染 (Graphics)
- 聲音播放 (Audio)

---

# 常見遊戲引擎
## Common Game Engines

| Engine | 特色 (Feature) | 適合 (Best for) | 難度 (Difficulty) |
|:---:|:---|:---|:---:|
| **Unity** | 業界標準、功能強大 | 手遊、2D/3D、獨立遊戲 | ⭐⭐⭐ |
| **Unreal** | 畫面頂級、3A大作 | 寫實風格、大型專案 | ⭐⭐⭐⭐⭐ |
| **GDevelop** | **免程式碼、視覺化** | **初學者、快速原型** | ⭐ |

---

# 為什麼選 GDevelop 5 ?
## Why GDevelop?

既然 Unity/Unreal 這麼強，為什麼我們今天用 **GDevelop**？

1. **因為我們是「體驗」課程**：我們要的是**成就感**，不是挫折感。
2. **視覺化腳本 (Events)**：不用寫像咒語一樣的程式碼，用**選的**就好！
3. **快速 (Fast)**：不用安裝幾十 GB 的軟體，甚至網頁版就能跑。

> **今天，我們專注在「創意」，而不是「除錯」！**

---

# GDevelop 的邏輯：事件 (Events)
## The Logic: Events

在 GDevelop 中，我們不寫 Code，我們寫 **「當...就...」**

- **當 (Condition)**：按下空白鍵
- **就 (Action)**：角色跳起來

- **當 (Condition)**：碰到金幣
- **就 (Action)**：金幣消失 + 加分

> 這就是程式設計的核心邏輯，但你不用背指令！

---

# AI 能幫我們做什麼？
## AI in Game Dev

雖然 GDevelop 很簡單，但 AI 還是能幫大忙：

1. **生成素材 (Assets)**：沒有美術圖？叫 AI 畫！
2. **發想玩法 (Ideas)**：「幫我想一個太空主題的平台遊戲機關」
3. **解釋邏輯 (Logic)**：「我要怎麼做二段跳？請告訴我 GDevelop 的邏輯」

---

# 1. 介面導覽 (Interface)
## The GDevelop Layout (1/2)

GDevelop 的介面分為三個主要區域：

1.  **專案管理 (Project Manager)** (左側)：管理你的場景 (Scene)、圖片資源、外部事件。
2.  **場景編輯器 (Scene Editor)** (中央)：你的畫布。在這裡拖拉物件、設計關卡、擺放敵人。
3.  **物件面板 (Objects)** (右側)：管理遊戲中的所有元件 (主角、地板、金幣)。

---

# 1. 介面導覽 (Interface)
## The Events Sheet (2/2)

點擊上方的 **Events (事件)** 標籤，會進入邏輯編輯區。

-   這是遊戲的**大腦**。
-   我們在這裡告訴電腦：「當發生 A，就執行 B」。
-   完全不需要寫程式碼，只要用滑鼠點選即可！

---

# 2. 建立角色物件 (Character)
## Creating the Player (1/2)

1.  在右側 **Objects** 面板，點擊 **+ Add a new object**。
2.  選擇 **Sprite (精靈)**。
3.  命名為 `Player` (建議使用英文)。
4.  點擊 **Add an animation**，選擇一張靜態圖片即可 (先不需要動畫)。
5.  完成後，將 **Player** 拖進場景畫面中。

---

# 2. 建立角色物件 (Character)
## Editing the Hitbox (2/2)

為了讓碰撞更精準：

1.  點擊 **Edit collision masks** (編輯碰撞遮罩)。
2.  選擇 **Use a custom collision mask**。
3.  調整紅色的框框，讓它貼合角色的身體 (通常會比圖片略小)。
4.  點擊 **Apply** 完成。

---

# 3. 建立 Tile 地圖 (Tilemap)
## Creating the Level (1/2)

我們要畫出地板和平台。

1.  新增物件 -> 選擇 **Tiled Sprite (拼貼精靈)**。
2.  命名為 `Ground` 或 `Platform` (一樣從 Asset Store 找官方素材)。
3.  選擇一張 "地板" 的圖片。
4.  將它拖進場景中，不需要拉長縮短，開始使用**塗色**的方式製作！

> **Tiled Sprite** 會自動重複圖片，適合做長長的地板。

---

# 4. 角色移動與調整 (Movement)
## Adding Behaviors (1/2)

讓角色動起來不需要寫程式！

1.  雙擊 `Player` 物件 -> 切換到 **Behaviors (行為)** 分頁。
2.  點擊 **+ Add a behavior**。
3.  搜尋並選擇 **Platformer object** (平台角色)。
4.  這會自動給予角色：左右移動、跳躍、重力。

---

# 4. 角色移動與調整 (Movement)
## Solid Ground (2/2)

但是角色會掉出螢幕...因為地板是虛的！

1.  雙擊 `Ground` 物件 -> 切換到 **Behaviors** 分頁。
2.  點擊 **+ Add a behavior**。
3.  搜尋並選擇 **Platform** (平台)。
4.  現在，角色可以站在地板上了！

> **Tip**: 你可以在 Behavior 設定中調整跳躍高度 (Jump height) 和移動速度。

---

# 試玩與調整 (Preview & Tweak)
## Let's Play!

1.  點擊上方的 **Preview** 按鈕 (或是按 F4)。
2.  試著用 **方向鍵** 控制角色移動，**空白鍵** 跳躍。
3.  如果不滿意手感 (跳太高、走太慢)：
    -   回去修改 `Player` 的 **Behaviors** 數值。
    -   調整 **Gravity (重力)**、**Jump speed (跳躍力)**。

---

# 5. 事件說明 (Events Logic)
## Cause & Effect (1/2)

打開 **Events** 分頁，我們來寫邏輯。
GDevelop 的邏輯由兩個部分組成：

| **Condition (條件)** | **Action (動作)** |
|:---|:---|
| **"當...發生時"** | **"就執行..."** |
| (When) | (Do) |
| 如果條件是空的 (Empty) | 代表 "隨時 / 每一幀" 都執行 |

---

# 5. 事件說明 (Events Logic)
## Example (2/2)

試著讀讀看這個邏輯：

-   **Condition**: `Player` is in collision with `Coin`
-   **Action**: Delete object `Coin`

這代表：「當 **主角** 碰到 **金幣** 時，**刪除金幣** (被吃掉了)。」

---

# 6. 攝影機跟隨主角 (Camera)
## Camera Follow (1/2)

預設攝影機是不動的，我們希望它跟著主角跑。

1.  在 Events 頁面，新增一個事件 (Add a new event)。
2.  **Condition**: 留空 (代表 Always)。
3.  **Action**: 搜尋 **Camera** -> 選擇 **Center the camera on an object**。
4.  選擇物件：`Player`。

---

# 7. 金幣收集 (Coin Collection)
## Items & Scoring (1/2)

讓遊戲更有趣！

1.  新增一個 `Coin` 物件 (Sprite)。
2.  放在場景中。
3.  **新增事件**：
    -   **Condition**: `Player` collision with `Coin`
    -   **Action**: Delete object `Coin`

---

# 7. 金幣收集 (Coin Collection)
## Sound Effects (2/2)

撿到金幣要有聲音！

1.  在剛剛的事件中，**再加一個 Action**。
2.  搜尋 **Sound** -> **Play a sound**。
3.  選擇一個音效檔 (或是用內建的 Generate sound)。
4.  (進階：你也可以在這裡加分 `Variable` -> `Add 100 to Score`)

---

# 8. 死亡與重新開始 (Death & Restart)
## Hazards (1/2)

掉出地圖外應該要死掉重來。

1.  **Condition**: `Player` Y position > 1000 (掉到太低的地方)
    -   (你可以比對場景的高度，通常 > 1000 就是掉出去了)
2.  **Action**: **Change the scene** -> 選擇目前的場景名稱 (重新載入)。

---

# 8. 死亡與重新開始 (Death & Restart)
## Spikes (2/2)

碰到尖刺也要死掉。

1.  建立一個 `Spike` 物件。
2.  **Condition**: `Player` collision with `Spike`
3.  **Action**: **Change the scene** (或是把 Player 傳送回起點)。

---

# 9. 遊戲結束 (Game Over)
## Win Condition (1/2)

做一個終點旗幟！

1.  建立 `Flag` 物件。
2.  **Condition**: `Player` collision with `Flag`
3.  **Action**: Show text "You Win!" (顯示文字)。

---

# 9. 遊戲結束 (Game Over)
## Next Level (2/2)

或是直接跳到下一關？

-   **Action**: **Change to scene** -> `"Level 2"`

> **恭喜！你已經完成了一個完整的遊戲迴圈 (Game Loop)！**
> Start -> Play -> Die/Win -> Restart/Next

---

# 10. 分享你的遊戲 (Share Your Game)
## Show off your work!

做完遊戲當然要給朋友玩！

1.  點擊左上角的 **File** -> **Publish web build** (或是上方發布按鈕)。
2.  選擇 **gd.games** (GDevelop 的免費託管平台)。
3.  登入/註冊帳號 (或是選擇 "Generate link")。
4.  幾秒鐘後，你就會獲得一個 **網址 (URL)**。
5.  傳給朋友，他們用手機就可以玩了！

---




# 實作時間！開始吧！
## Let's Make a Game!

---

# 結語
## Conclusion

遊戲開發不一定要很痛苦。
使用適合的工具，你也可以輕鬆做出自己的遊戲！

### Have Fun with GDevelop!
