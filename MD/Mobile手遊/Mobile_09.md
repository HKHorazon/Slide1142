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

### Chapter 09
# 角色動畫系統 (Animator)

## Horazon
## 手遊程式設計

---

# 章節目標

-   認識 Unity 動畫系統 (**Mecanim**)
-   製作 **Idle** (待機) 與 **Run** (跑步) 動畫
-   使用程式切換動畫狀態 (**Transitions**)

---

# 1. 動畫三要素

在 Unity 讓圖片動起來，需要三個東西：

1.  **Sprite (圖片)**：連續動作的分解圖。
2.  **Animation Clip (動畫片段)**：把圖片串起來的影片檔 (例如 `Run.anim`)。
3.  **Animator Controller (控制器)**：大腦，決定現在要播哪一支影片。

---

# 2. 製作第一個動畫 (Idle)

1.  選取主角 (Player)。
2.  開啟 **Window -> Animation -> Animation**。
3.  點擊 **Create** 按鈕。
4.  命名為 `Player_Idle` (待機)。
5.  從 Project 視窗選取「站著不動」的幾張圖片，拖入 Animation 時間軸。
6.  按下播放鍵預覽，調整 **Samples** (影格率) 讓速度自然 (通常 10-15)。

---

# 3. 製作第二個動畫 (Run)

1.  在 Animation 視窗左上角的下拉選單，選擇 **Create New Clip**。
2.  命名為 `Player_Run` (跑步)。
3.  拖入「跑步中」的圖片序列。
4.  一樣調整速度。

(同樣步驟可以製作 Jump 跳躍動畫)

---

# 4. 設定狀態機 (Animator Window)

開啟 **Window -> Animation -> Animator**。你會看到像流程圖的畫面。

1.  **Entry**：入口，遊戲開始會連到的第一個狀態 (通常是 Idle)。
2.  **Make Transition**：
    -   對 `Idle` 按右鍵 -> Make Transition -> 連到 `Run`。
    -   對 `Run` 按右鍵 -> Make Transition -> 連回 `Idle`。

---

# 5. 設定切換條件 (Parameters)

我們要告訴大腦「什麼時候」該切換。

1.  在 Animator 左側點選 **Parameters** 分頁。
2.  按下 **+** 號，新增一個 **Float** 變數，命名為 `Speed`。
    -   (思路：速度 > 0.1 代表在跑，速度 < 0.1 代表停下)。
3.  點選 `Idle -> Run` 的白色箭頭 (連線)：
    -   取消勾選 **Has Exit Time** (不需播完就能切換)。
    -   Conditions 加入 `Speed Greater 0.1`。
4.  點選 `Run -> Idle` 的白色箭頭：
    -   取消勾選 **Has Exit Time**。
    -   Conditions 加入 `Speed Less 0.1`。

---

# 6. 用程式控制動畫

回到 `PlayerController` 腳本，我們要把變數傳給 Animator。

```csharp
public Animator anim; // 1. 宣告動畫控制器

void Update()
{
    float h = Input.GetAxisRaw("Horizontal");
    // ... (移動程式碼) ...

    // 2. 設定動畫參數
    // Mathf.Abs 是取絕對值 (不管正負，只看數值大小)
    anim.SetFloat("Speed", Mathf.Abs(h));
}
```

記得存檔後，把主角身上的 **Animator** Component 拖進腳本欄位！

---

# 總結

現在試玩看看：

-   **不動時**：播放 Idle 呼吸動畫。
-   **移動時**：瞬間切換成 Run 跑步動畫。
-   **變數傳遞**：Input -> Script -> Animator -> 畫面。

下一章，我們要讓遊戲不僅僅是移動，還要能跟世界**互動** (吃金幣、受傷)。
