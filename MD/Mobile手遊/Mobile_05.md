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

# Chapter 05
# 物理系統 (Physics 2D)

## Horazon
## 手機遊戲開發

---

# 複習：上週重點

-   [x] 學會 C# 腳本基礎。
-   [x] 認識變數 (int, float, string)。
-   [x] 認識方法 (Start, Update)。
-   [x] 成功印出 Hello World。

程式寫好了，但... 物件還是不會動？
因為我們還沒加上**物理**。

---

# 本章目標

今天要讓你的遊戲世界擁有真實的物理法則。

1.  認識 **Rigidbody 2D** (剛體)。
2.  認識 **Collider 2D** (碰撞器)。
3.  學會使用 **Physics Material 2D** (物理材質)。
4.  理解 **Trigger** (觸發器) 的用途。
5.  透過程式偵測碰撞 (`OnCollisionEnter2D`)。

---

# 什麼是物理引擎？

Unity 內建了強大的物理引擎 (Box2D)。
它可以幫你模擬：

-   重力 (Gravity)
-   摩擦力 (Friction)
-   反彈力 (Bounciness)
-   碰撞偵測 (Collision Detection)

**你不需要自己寫 F=ma，只要掛上 Component 就好！**


---

# 物理雙壁

要有物理反應，必須要有這兩個東西：

1.  **Rigidbody 2D (身體)**
    -   讓物件受重力影響，可以被推動。
2.  **Collider 2D (形狀)**
    -   定義物件的實體範圍，讓它不會穿牆。

> **Warning**: 請務必選有 **2D** 字尾的 Component！(3D 的 BoxCollider 沒用)

---

# Rigidbody 2D (剛體)

這是物理系統的核心。
任何「會動的」物理物件都需要它。

### 設定屬性 (Inspector)：
-   **Body Type**：
    -   **Dynamic** (預設)：受重力與力影響 (主角、敵人、箱子)。
    -   **Kinematic**：不受重力影響，但會推動別人 (移動平台)。
    -   **Static**：完全不動 (牆壁、地板)。
-   **Mass**：質量 (越重越難推)。
-   **Gravity Scale**：重力倍率 (1=地球重力，0=無重力)。


---

# 重要設定：Constraints

在 2D 遊戲中，這非常重要！

### Freeze Rotation Z
-   預設情況下，球滾動會旋轉。
-   但如果你的人物 (膠囊體) 走路走到一半跌倒滾走怎麼辦？
-   **一定要勾選 Freeze Rotation Z**，鎖住 Z 軸旋轉，讓主角永遠站著。

---

# 實作練習 1：自由落體

1.  在天空建立一個 **Square**。
2.  Add Component -> **Rigidbody 2D**。
3.  按下 **Play**。
4.  觀察方塊是否掉下去？
    -   如果掉出畫面，表示重力生效了。
    -   如果沒掉，檢查 Body Type 是否為 Dynamic。

---

# Collider 2D (碰撞器)

只有剛體，物體是「幽靈」，會穿過地板。
我們需要 **Collider** 來定義它的實體。

### 常見類型：
-   **Box Collider 2D**：方塊 (箱子、磚塊)。
-   **Circle Collider 2D**：圓形 (球、金幣)。
-   **Capsule Collider 2D**：膠囊形 (最適合**人類角色**)。
-   **Polygon Collider 2D**：多邊形 (不規則地形)。

---

# 實作練習 2：腳踏實地

1.  幫剛剛的 Square 加上 **Box Collider 2D**。
    -   你會看到綠色的外框線。
2.  建立一個新的 Square 當作地板，拉長。
3.  幫地板加上 **Box Collider 2D**。
    -   **不用** 加 Rigidbody 2D (因為地板是 Static 的)。
4.  按下 **Play**。
5.  方塊應該會掉下來，並停在地板上！

---

# 編輯碰撞範圍

有時候圖片很大，但實體很小 (例如樹冠很大，但只有樹幹會撞到)。

1.  在 Inspector 找到 Collider 2D 元件。
2.  點選 **Edit Collider** 按鈕 (右邊的小圖示)。
3.  在 Scene 視窗拖曳綠色的小點點，調整大小。


---

# Physics Material 2D (物理材質)

想要做彈力球？還是溜冰場？

1.  Project 視窗按右鍵 -> **Create** -> **2D** -> **Physics Material 2D**。
2.  設定參數：
    -   **Friction** (摩擦力)：0 = 很滑 (冰)，1 = 很粗糙 (砂紙)。
    -   **Bounciness** (彈力)：0 = 不彈 (石頭)，1 = 超彈 (果凍)。

---

# 套用物理材質

1.  選取你的物理物件。
2.  找到 Rigidbody 2D 或 Collider 2D。
3.  將剛剛做好的 Material 拖曳到 **Material** 欄位中。

---

# 實作練習 3：超級彈力球

1.  建立一個 **Circle**。
2.  加入 **Rigidbody 2D** + **Circle Collider 2D**。
3.  建立一個物理材質，**Bounciness** 設為 0.9。
4.  套用到球上。
5.  Play！享受彈跳的樂趣。

---

# 碰撞 (Collision) vs 觸發 (Trigger)

有時候我們不想要「撞上去」，而是「穿過去」。
例如：吃金幣、走到終點線、踩到岩漿。

### Is Trigger
-   在 Collider 2D 元件上，勾選 **Is Trigger**。
-   物件會變成「鬼魂」，可以穿透。
-   但是**依然會被偵測到**！

---

# 程式偵測：Collision

要怎麼知道「撞到了」？我們要寫腳本。

```csharp
// 當發生實體碰撞時 (撞牆、撞人)
void OnCollisionEnter2D(Collision2D other)
{
    Debug.Log("撞到了：" + other.gameObject.name);
}
```

-   `Enter`：撞到的瞬間 (一次)。
-   `Stay`：持續接觸中 (每幀)。
-   `Exit`：離開碰撞的瞬間 (一次)。

---

# 程式偵測：Trigger

要怎麼知道「吃到了」？

```csharp
// 當穿過 Trigger 時 (吃金幣)
void OnTriggerEnter2D(Collider2D other)
{
    Debug.Log("吃到了：" + other.gameObject.name);
}
```

> **Note**: 參數型態不一樣喔！Collision 用 `Collision2D`，Trigger 用 `Collider2D`。

---

# 實作練習 4：陷阱腳本

我們來做一個碰到會說「痛！」的腳本。

1.  建立腳本 `DamageObject`。
2.  寫入 `OnCollisionEnter2D` 方法。
3.  裡面寫 `Debug.Log("好痛！");`。
4.  掛載到掉落的方塊上。
5.  Play -> 當方塊撞到地板時，Console 應該會出現訊息。

---

# Tilemap Collider 2D

還記得我們畫了很大的地圖嗎？
如果要幫地圖加上碰撞，難道要一個個畫 Box Collider？

**不用！**
1.  選取 **Tilemap** 物件。
2.  Add Component -> **Tilemap Collider 2D**。
3.  Unity 會自動根據每一格磚塊產生碰撞框。

*太神啦！*

---

# 效能優化：Composite Collider 2D

Tilemap Collider 會產生幾千個小方塊，效能不好。

1.  再加入 **Composite Collider 2D**。
2.  這會自動加入 Rigidbody 2D (記得把它改成 **Static**，不然地圖會掉下去！)。
3.  在 Tilemap Collider 2D 勾選 **Used By Composite**。
4.  你會發現所有的小方塊合併成一大塊了！

---

# 常見錯誤 (Debug)

Q: 物件直直掉穿過地板？
A:
1.  檢查地板有沒有 Collider 2D。
2.  檢查 Is Trigger 有沒有不小心勾到。
3.  檢查圖層 (Layer Collision Matrix，這比較進階，先確認基本設定)。

Q: 主角走路會跌倒？
A: 檢查 Rigidbody 2D -> Constraints -> **Freeze Rotation Z** 有沒有勾。

---

# 總結

物理系統是讓遊戲活起來的關鍵。

1.  **Rigidbody 2D**：讓它動。
2.  **Collider 2D**：讓它有形狀。
3.  **Physics Material**：摩擦力與彈力。
4.  **Trigger**：觸發事件 (金幣、傳送門)。
5.  **Tilemap Collider**：快速幫地圖加碰撞。

---

# 下週預告

有了物理，我們就可以做各種機關了！
下週我們來實作：

-   真正可互動的物件。
-   金幣收集系統。
-   會殺人的陷阱。
-   (並順便學習 Prefab 的概念)

---

# Q & A

有任何物理模擬不正常的問題？

-   物件卡住發抖？
-   穿牆？(速度太快會穿牆，要改 Collision Detection 為 Continuous)

*(助教巡堂協助)*
