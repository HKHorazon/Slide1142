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
<!--_paginate: false-->

### Chapter 04
# 物理與機關

## Horazon
## 手遊程式設計

---

# 章節目標

-   讓地圖有實體 (**Collider**)
-   了解剛體物理 (**Rigidbody**)
-   優化碰撞效能 (**Composite Collider**)
-   調整基礎機關 (移動平台、尖刺)

---

# 1. 為什麼角色會掉出地圖？

我們上週畫得很漂亮，但按下 Play 之後...

-   主角穿過了地板，掉到深淵裡。
-   **原因**：Tilemap 目前只是「畫在螢幕上的圖片」。
-   電腦不知道它是「硬的」還是「軟的」，也不知道它是牆壁。

---

# 2. 什麼是 Collider (碰撞器)？

Collider 是定義物件「外型」與「碰撞範圍」的元件。
一定要有碰撞器，物體才會有「實體」，不會互相穿透。

-   **Box Collider 2D**：方形 (適合箱子、地板)。
-   **Circle Collider 2D**：圓形 (適合球、金幣)。
-   **Polygon Collider 2D**：多邊形 (適合不規則形狀)。

---

# 3. 給地圖加上碰撞

我們畫好的地圖 (Tilemap) 也有專用的碰撞器。

1.  選取 Hierarchy 中的 `Tilemap` (例如 Ground_Map)。
2.  Add Component -> **Tilemap Collider 2D**。
3.  你會看到地圖上每一格都出現了綠色的網格線。

現在試玩看看，主角應該可以站在地上了！

---

# 4. 效能優化：Composite Collider

雖然能走了，但你有發現問題嗎？
**每一格瓦片都有一個獨立的綠色框框。**

-   如果地圖很大嗎，電腦要計算成千上萬個碰撞框，效能會變差。
-   我們希望「連在一起的地板」就變成「一整塊大碰撞體」。

---

# 使用 Composite Collider 2D

這是一個「合併工具」：

1.  在同一個 Tilemap 物件上，Add Component -> **Composite Collider 2D**。
2.  (Unity 會自動幫你加上 Rigidbody 2D，這是正常的)。
3.  回到上面的 **Tilemap Collider 2D** 元件。
4.  勾選 **Used By Composite** (給複合器使用)。

你會發現綠色框框合併成一大塊了！

---

# 5. 修正 Rigidbody 問題

剛才 Unity 自動加上的 Rigidbody 2D 預設是 **Dynamic** (會受重力)。
結果你的地板自己掉下去了！

-   找到 Tilemap 上的 **Rigidbody 2D** 元件。
-   將 **Body Type** 改為 **Static** (靜態)。

<br>
<mark>Static 代表：即使受碰撞也不會移動，也不受重力影響 (完全不動的牆)。</mark>

---

# 6. Rigidbody 2D (剛體) 深入講解

Rigidbody 決定了物件的「物理行為」。

常見的三種模式：
1.  **Dynamic (動態)**：受重力、受推力。主角、怪物、會動的箱子用這個。
2.  **Static (靜態)**：完全不動。地板、牆壁用這個。
3.  **Kinematic (運動學)**：不受物理力，但會動。例如移動平台 (Moving Platform)，它會動，但不會被主角撞飛。

<br>
**主角設定**：一定要有 Dynamic Rigidbody，不然跳不起來。

---

# 7. 放置機關：尖刺 (Spikes)

讓我們增加一點難度。

1.  匯入 `Spike` Prefab。
2.  這通常使用 `Polygon Collider 2D` 來貼合三角形形狀。
3.  如果不小心碰到尖刺，主角應該要受傷或死亡 (這部分下週會講邏輯)。
4.  目前先擺放位置，當作視覺障礙。

---

# 8. 放置機關：移動平台

1.  匯入 `MovingPlatform` Prefab。
2.  觀察它的設定：
    -   它通常是用 **Kinematic** Rigidbody (因為要浮在空中移動)。
    -   Inspector 上可能有 `Move Speed` (移動速度) 參數可以調整。
    -   試著改變參數，讓它跑快一點或慢一點。

---

# 總結

-   **沒有 Collider 就沒有實體**。
-   **Tilemap Collider** 要搭配 **Composite Collider** 優化效能。
-   地板要是 **Static**，主角要是 **Dynamic**，移動平台要是 **Kinematic**。
-   透過調整 Prefab 參數，不寫程式也能改變遊戲難度。

下一章我們將賦予這些機關真正的「功能」(例如踩到尖刺會死掉)！
