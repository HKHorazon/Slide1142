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

# 角色膠囊 (Player Setup)

## Horazon
## 手機遊戲開發

---

# 角色

我們把「世界」建構好了。

正常遊戲的製作，通常會由角色 (核心玩法)開始製作
但我覺得角色設定相對較複雜，所以我們把角色設定放在後面。

現在，讓我們開始吧。


---

# 本章目標

1.  與美術素材整合 (Sprite)。
2.  設定 **Capsule Collider 2D**。
3.  調整 **Rigidbody 2D** 參數 (手感關鍵)。
4.  解決「卡牆」與「滾得像皮球」的問題。
5.  將主角製作成 **Prefab**。

---

# 步驟 1：匯入角色素材

1.  找一張主角的**站立 (Idle)** 圖片。
2.  拖入 Project -> Sprites 資料夾。
3.  設定 Texture Type = Sprite (2D and UI)。
4.  設定 Pixels Per Unit (確保大小適中)。
5.  拖入場景，命名為 `Player`。

---

# 步驟 2：選擇形狀 (Collider)

-   **Box (方塊)**：適合箱子。若用在角色，頭部容易卡在天花板角落。
-   **Circle (圓形)**：適合球。若用在角色，站不穩，容易滑動。
-   **Capsule (膠囊)**：**最佳選擇！**
    -   頭腳圓滑：不會卡住，上下坡順暢。
    -   身體直長：符合人形。

---

# 設定 Collider

1.  Add Component -> **Capsule Collider 2D**。
2.  點選 **Edit Collider**。
3.  調整綠色外框，貼合角色的身體。
    -   **注意**：腳底稍微修圓一點，不要切齊地面，這樣上坡比較不會卡到。

---

# 步驟 3：賦予重量 (Rigidbody)

1.  Add Component -> **Rigidbody 2D**。
2.  這時候按 Play，主角會掉下去 (正常)。

### 手感調整關鍵 (Gravity Scale)：
-   預設值 `1`：有點像在月球漫步，輕飄飄的。
-   **建議值 `3 ~ 5`**：
    -   瑪利歐類型的遊戲通常重力很強。
    -   這樣跳起來落地比較快，操作感比較**俐落 (Snappy)**。

---

# 災難預防 1：不倒翁

如果你現在讓角色去撞牆或斜坡...
**他會跌倒並滾走！**

### 解法：
1.  找到 Rigidbody 2D -> **Constraints** (約束)。
2.  **勾選 Freeze Rotation Z**。
3.  這樣角色就永遠不會旋轉跌倒了。

---

# 災難預防 2：壁虎功

如果你讓角色貼著牆壁跳...
**他會黏在牆壁上掉不下來！**
這是因為預設有摩擦力 (Friction)。

### 解法：
1.  建立一個 **Physics Material 2D**，命名 `Slippery` (滑溜)。
2.  設定 **Friction = 0**。
3.  設定 **Bounciness = 0** (別讓他彈起來)。
4.  將此材質拖到主角的 **Collider 2D** 上。

*現在主角就像抹了油一樣，不會卡牆了！*

---

# 步驟 4：設定 Tag 與 Layer

為了讓敵人和機關認識主角。

1.  **Tag**: 改為 `Player`。
2.  **Layer**:
    -   新增一個圖層 `Player`。
    -   將主角設為此圖層。
    -   (這有助於之後設定「主角不跟主角碰撞」或「主角不跟金幣碰撞」)。

---

# 步驟 5：設定 Sorting Layer

別忘了渲染順序。

1.  建立新的 Sorting Layer：**Player**。
2.  順序應該在 Ground 之上，ForeGround 之下。
3.  將主角的 Sprite Renderer -> Sorting Layer 改為 `Player`。

---

# 步驟 6：準備腳本

雖然下週才寫移動邏輯，我們先把殼準備好。

1.  建立腳本 `PlayerController.cs`。
2.  掛載到主角身上。
3.  宣告變數：

```csharp
public class PlayerController : MonoBehaviour
{
    public float moveSpeed = 5f;
    public float jumpForce = 10f;
    public Rigidbody2D rb;

    void Start()
    {
        // 自動抓取身上的剛體元件
        rb = GetComponent<Rigidbody2D>();
    }
}
```

---

# 步驟 7：製作成 Prefab

這一步最重要。
因為以後每一關都要用這隻主角。

1.  將 Hierarchy 的 `Player` 拖入 Project -> `Prefabs` 資料夾。
2.  以後開新關卡，直接把 Player Prefab 拉進去就好。
3.  不用重新設定重力、摩擦力、Collider。

---

# 整合測試：Cinemachine

還記得期中考前的攝影機嗎？

1.  選取場景中的 `CM vcam1`。
2.  將新的 `Player` 拖入 **Follow** 欄位。
3.  按下 **Play**。
4.  用滑鼠 (W工具) 拖著主角亂飛，攝影機應該要跟著跑。

---

# 常見問題

Q: 主角穿過地板掉下去？
A:
1.  速度太快 (Gravity Scale 設太高)。
2.  將 Rigidbody 2D -> **Collision Detection** 改為 **Continuous** (持續偵測)。

Q: 膠囊的腳底是圓的，站在懸崖邊會滑下去？
A:
這是膠囊體的特性。如果很介意，可以：
1.  腳底改平一點 (多邊形 Collider)。
2.  或者用程式控制 (沒輸入時鎖住 X 軸)。

---

# 關於子物件 (Children)

有時候我們會在主角底下掛東西：

-   **GroundCheck** (空物件)：放在腳底，用來偵測是否著地。
-   **WeaponPosition** (空物件)：放在手上，用來發射子彈。
-   **Effects** (特效)：跑步煙塵。

**記得這些都要包進 Prefab 裡！**

---

# 挑戰：斜坡測試

做一個 45 度的斜坡。

1.  放主角上去。
2.  因為 Friction = 0，他應該要**滑下來**。
3.  如果你希望他「站得住」但「牆壁不黏」...
    -   這就需要程式控制了 (之後章節會教)。
    -   目前的設定是「滑溜人」，適合快節奏動作遊戲。

---

# 總結

一個好的主角設定包含：

1.  **Capsule Collider** (圓滑的身體)。
2.  **Rigidbody 2D** (適當的重力與鎖定旋轉)。
3.  **Physics Material** (零摩擦力)。
4.  **Prefab** (重複使用)。

地基打好了，下週我們就來寫扣人心弦的**移動程式**！

---

# 下週預告

C# 程式重頭戲：
-   Input.GetAxis (讀取鍵盤)。
-   Rigidbody.velocity (修改速度)。
-   Flip (角色翻面)。

---

# Q & A

(開放提問)

-   想用方塊人當主角可以嗎？
    -   可以，但要有卡牆的心理準備，建議還是用膠囊包住方塊。

*(助教巡堂協助)*
