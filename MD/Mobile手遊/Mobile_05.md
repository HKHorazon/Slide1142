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

### Chapter 05
# 互動與邏輯 (預製功能)

## Horazon
## 手遊程式設計

---

# 章節目標

-   區分 **Trigger (觸發)** 與 **Collider (碰撞)**
-   體驗 **Trigger** 的功能 (金幣、機關)
-   體驗遊戲的 **勝利與失敗**
-   組合出第一個完整關卡

---

# 1. 碰撞 (Collision) vs 觸發 (Trigger)

在 Unity 的物理系統中，物體接觸有兩種反應：

1.  **Collider (碰撞)**：
    -   像是撞到牆壁。
    -   物體會被擋住，會反彈。
    -   功能：阻擋玩家，模擬真實世界。

2.  **Trigger (觸發)**：
    -   像是走過自動門感應器。
    -   物體會直接穿過去，**但會送出訊號**。
    -   功能：執行特定事件 (吃金幣、開門、受傷)。

---

# 2. 製作收集品：金幣 (Coin)

我們來擺放金幣讓玩家收集。

1.  將 `Coin` Prefab 拖入場景。
2.  觀察 Inspector 中的 **Circle Collider 2D**。
3.  你會發現 **Is Trigger** 選項被勾選了。

<br>
<mark>如果不勾選 Is Trigger，主角就會像踢足球一樣把金幣踢走，而不是吃掉它！</mark>

---

# 3. 製作目標：旗幟 (Goal)

遊戲需要一個過關的目標。

1.  將 `Goal` (旗幟) Prefab 拖曳到地圖終點。
2.  它通常也是一個 Trigger。
3.  當主角碰到的瞬間，會觸發勝利音效或畫面。

試玩看看，走到終點是否會發生事情？

---

# 4. 製作懲罰：死亡陷阱

掉出地圖外如果一直無限下墜，遊戲就壞了。
我們需要一個「死亡判定區」。

1.  在地圖最下方，建立一個空物件 (Create Empty)。
2.  加入 **Box Collider 2D**。
3.  勾選 **Is Trigger**。
4.  將 Collider 的範圍拉大，覆蓋整個地板下方。
5.  掛載我們準備好的 `PlayerDeath` 腳本 (或是 `DeadZone` Prefab)。

---

# 5. 組合關卡：設計師的挑戰

現在你手上已經有了所有的積木：

-   **地形** (Tilemap)：提供立足點。
-   **障礙** (Spikes)：提供挑戰。
-   **獎勵** (Coin)：引導玩家路徑。
-   **目標** (Goal)：給予成就感。

---

# 關卡設計 (Level Design) 練習

利用這週從素材包裡拿到的東西，與你畫好的地圖，設計一個「有點難但又不會太難」的關卡。

**思考方向**：
-   金幣是不是放在有點危險的地方？
-   跳躍距離會不會太遠跳不過去？
-   有沒有隱藏路徑？

---

# 總結 (第一階段)

恭喜！你已經利用 **Unity 的預製功能** 完成了一個可遊玩的遊戲原型。

-   我們學會了 **Project** 管理素材。
-   學會了 **Tilemap** 繪製地圖。
-   了解 **Collider** 與 **Trigger** 的運作原理。
-   **完全沒有寫任何程式碼！**

下一階段，我們要開始深入核心，學習如何**自己寫程式**來控制這一切！
