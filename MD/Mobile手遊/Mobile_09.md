---
marp: true
theme: HoraStyle
paginate: true
style: |
  :root {
    --title-bg: linear-gradient(90deg, #15803d, #22c55e);
    --title-text-color: #ffffff;
  }
  section.lead {
    background: linear-gradient(135deg, #052e16 0%, #000000 100%);
  }
---

<!-- _class: lead -->
<!-- _paginate: false -->

### Chapter 09

# 玩家角色-基礎

## Horazon
## 手機程式設計

---

# 角色

我們已經把遊戲的「世界」（場景、攝影機）建構好了。

在正常的遊戲開發流程中，通常會由**角色（核心玩法）**開始製作。
但因為角色設定的細節相對較多且複雜，為了讓大家循序漸進，我們才將角色設定放在場景之後。

現在，讓我們開始賦予遊戲靈魂吧！

---

# 課前暖身：什麼是操作手感 (Game Feel)？

在開始製作角色之前，我們先來體驗一下什麼是**好的手感**。
強烈推薦大家試玩這款由[死亡細胞]作者製作的小型DEMO：
👉 [Game Feel 體驗器 (點我試玩)](https://deepnight.net/games/game-feel/)

按下enter可調整功能。

---

# 本章目標

1.  與美術素材整合 (Sprite)。
2.  設定 **Capsule Collider 2D** (碰撞體)。
3.  調整 **Rigidbody 2D** 參數 (決定手感關鍵)。
4.  解決「卡牆」與「滾得像皮球」的物理問題。
5.  將主角製作成 **Prefab** (預製物)。

> 老師已經完成大部分，所以主要為說明，但你也可以做一些調整!

---

# 步驟 1：匯入角色素材

1.  **尋找素材**：找一張主角的**站立 (Idle)** 圖片。
2.  **匯入專案**：將圖片拖入 Unity 下方的 `Project` 視窗內的 `Sprites` 資料夾中。
3.  **設定屬性**：
    - 點擊剛匯入的圖片。
    - 在右側 `Inspector` 視窗中，將 **Texture Type** 設定為 `Sprite (2D and UI)`。
    - 確保 **Pixels Per Unit** 數值合理（例如 100，確保角色大小適中）。
    - 點擊下方的 **Apply** 儲存設定。
4.  **放置場景**：將設定好的圖片從 `Project` 拖入中央的 `Scene` 或 `Hierarchy` 中。
5.  **命名**：在 `Hierarchy` 中點擊該物件，按下 `F2`，將其命名為 `Player`。

---
# 步驟 1B: 角色與圖片的層級

我們需要建立一個空物件作為主角的「骨架」，再把圖片當作它的「皮」。

Player (空物件)
    └─ Img_Player (圖片)

這樣做的好處是，未來如果要幫角色加上一些「裝飾物件」（如帽子、披風、光環等），直接把它們拖拉到 Player 父物件下就好，位置都已經幫你對齊好了。

---

# 步驟 2：選擇形狀 (Collider)

為了解決「碰撞」的問題，我們需要幫角色加上碰撞體。不同形狀有不同效果：

-   ❌ **Box (方塊)**：適合箱子或牆壁。若用在角色，頭部容易卡在天花板角落，腳部在下坡會卡住。
-   ❌ **Circle (圓形)**：適合球體。若用在角色，會站不穩，容易像球一樣滾動。
-   ✅ **Capsule (膠囊)**：**最佳選擇！**
    -   頭腳圓滑：不會卡住，上下坡順暢。
    -   身體直長：最符合人類的直立身形。


---

# 設定 Collider (防呆步驟)

1.  在 `Hierarchy` 點選 `Player`。
2.  在右側 `Inspector` 點擊最下方的 **Add Component**。
3.  搜尋並選擇 **Capsule Collider 2D**。
4.  點選元件上的 **Edit Collider** (一個小小的綠色編輯按鈕)。
5.  **調整綠色外框**：在場景中拖拉綠色點點，使其貼合角色的身體。
    -   💡 **防呆提示**：腳底要稍微修圓一點，**不要**切齊地面，這樣走上斜坡時比較不會卡到邊角。

---

# 步驟 3：賦予重量 (Rigidbody)

1.  同樣點選 `Player`，點擊 **Add Component**。
2.  搜尋並選擇 **Rigidbody 2D**。
3.  這時候按 Play，主角會受重力影響掉下去 (這是正常的！)。

### 手感調整關鍵 (Gravity Scale)：
-   預設值 `1`：感覺有點像在月球漫步，輕飄飄的，不夠真實。
-   **建議值設定為 `3 ~ 5`**：
    -   像瑪利歐這類型的動作遊戲，通常重力數值較高。
    -   這樣跳起來落地比較快，操作感比較**俐落 (Snappy)**。

---

# 災難預防 1：不倒翁現象

如果你現在讓角色去撞牆或走斜坡...
**他會跌倒並在地上滾走！** (因為他有物理重量跟碰撞體)

### 防呆解法 (鎖定旋轉)：
1.  在 `Player` 的 `Inspector` 中，找到剛加入的 **Rigidbody 2D** 元件。
2.  展開底下的 **Constraints** (物理約束) 選單。
3.  **勾選 Freeze Rotation Z** (凍結 Z 軸旋轉)。
4.  完成！這樣角色就永遠會直挺挺站著，不會旋轉跌倒了。

---

# 災難預防 2：壁虎功卡牆

如果你讓角色貼著牆壁跳躍...
**他會黏在牆壁上掉不下來！** 這是因為 Unity 預設物體之間有摩擦力 (Friction)。

### 防呆解法 (滑溜材質)：
1.  在 `Project` 視窗空白處，點擊右鍵 -> **Create** -> **2D** -> **Physics Material 2D**。
2.  將新建立的材質命名為 `Slippery` (滑溜)。
3.  點擊它，在 `Inspector` 設定：
    -   **Friction (摩擦力) = 0**
    -   **Bounciness (彈力) = 0** (別讓他彈起來)。
4.  將這個 `Slippery` 材質，拖曳到 `Player` 身上 **Capsule Collider 2D** 的 **Material** 欄位中。

*現在主角就像抹了油一樣，再也不會卡在牆壁上了！*

---

# 步驟 4：設定 Tag 與 Layer

為了讓遊戲中的敵人、金幣和機關能「認出」主角是誰。

1.  **設定 Tag (標籤)**：
    -   在 `Player` 的 `Inspector` 最上方，找到 **Tag** 下拉選單。
    -   選擇內建的 `Player`。
2.  **設定 Layer (圖層)**：
    -   找到 **Layer** 下拉選單，選擇 `Add Layer...`。
    -   在空白欄位輸入 `Player`，建立一個專屬圖層。
    -   回到 `Player` 物件，將 **Layer** 下拉選單改為剛剛新增的 `Player`。
    -   💡 **防呆提示**：這有助於之後設定「主角不要跟主角碰撞」或過濾特定物理效果。

---

# 步驟 5：設定 Sorting Layer

別忘了渲染順序，確保主角不會被背景遮住。

1.  找到主角的 **Sprite Renderer** 元件。
2.  展開 **Sorting Layer** 下拉選單，選擇 `Add Sorting Layer...`。
3.  建立一個新的層級：**Player**。
4.  調整層級順序：確保 `Player` 在 `Ground` 之下（更靠近螢幕），但在 `ForeGround` (前景) 之上。
5.  回到主角，將 **Sorting Layer** 改為剛建好的 `Player`。

---

# 步驟 6：準備腳本 (Script)

雖然下週才寫完整的移動邏輯，我們先把腳本的外殼準備好。

1.  在 `Project` 內建立一個新 C# 腳本 `PlayerController.cs`。
2.  將腳本拖曳掛載到 `Player` 身上。
3.  點擊兩下開啟腳本，宣告基本變數：

```csharp
public class PlayerController : MonoBehaviour
{
    public float moveSpeed = 5f; // 移動速度
    public float jumpForce = 10f; // 跳躍力道
    public Rigidbody2D rb; // 裝載剛體的變數

    void Start()
    {
        // 遊戲開始時，自動抓取身上的剛體元件，防呆設定！
        rb = GetComponent<Rigidbody2D>();
    }
}
```

---

# 步驟 7：製作成 Prefab (預製物)

**這一步非常重要！**
因為以後每一關都要用這隻設定好的主角。

1.  將 `Hierarchy` 的 `Player` 直接拖入 `Project` 下的 `Prefabs` 資料夾中。
2.  這時 `Hierarchy` 中的 `Player` 文字會變成**藍色**，代表成功變成 Prefab。
3.  以後開新關卡，只要把 `Player` Prefab 拉進去就好，不用再重新設定重力、摩擦力和 Collider！

---

# 常見問題排解 (Debug)

**Q: 主角穿過地板一直往下掉？**
A:
1. 可能是下落速度太快 (Gravity Scale 設太高)。
2. 💡 **解法**：將 Rigidbody 2D -> **Collision Detection** (碰撞偵測) 改為 **Continuous** (持續偵測)。

**Q: 膠囊的腳底是圓的，站在懸崖邊會慢慢滑下去？**
A:
這是膠囊體的物理特性。如果你很介意：
1. 腳底改平一點 (改用 Polygon Collider 畫多邊形)。
2. 或者用程式控制 (沒輸入按鍵時，強制鎖住 X 軸速度)。

---

# 關於子物件 (Children)

有時候我們會在主角底下掛載其他輔助物件：

-   **GroundCheck** (空物件)：放在腳底，之後用來偵測是否踩到地面。
-   **WeaponPosition** (空物件)：放在手上，之後用來發射子彈的生成點。
-   **Effects** (特效)：例如跑步產生的灰塵特效。

💡 **防呆提示**：記得將這些子物件加好後，要在 Prefab 上點擊 **Overrides -> Apply All**，確保它們都被存進 Prefab 裡！

---

# 總結

一個完美的動作遊戲主角基礎設定包含：

1.  **Capsule Collider** (圓滑的身體，不卡角)。
2.  **Rigidbody 2D** (適當的重力手感，並鎖定 Z 軸旋轉防跌倒)。
3.  **Physics Material** (零摩擦力，防黏牆)。
4.  **Prefab化** (方便每一關重複使用)。

地基打好了，下週我們就來寫扣人心弦的**移動程式**！

