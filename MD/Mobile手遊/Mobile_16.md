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

### Chapter 16

# 手機觸控操作

## Horazon
## 手機遊戲開發

---

# 複習：上週挑戰

-   [x] 成功輸出 APK 檔。
-   [x] 在手機上可以安裝並執行。

**但是...**
「老師，我的主角不會動！」
因為手機沒有鍵盤 (A/D/Space)，我們寫的 `Input.GetAxis` 沒收到訊號。

今天最後一哩路：**製作虛擬按鍵 (Virtual Controls)**。

---

# 本章目標

1.  製作螢幕虛擬按鈕 (左、右、跳)。
2.  使用 **EventTrigger** 偵測「按住」事件。
3.  修改 `PlayerController` 支援手機輸入。
4.  **期末專案 (Final Project)** 說明。

---

# 介面佈局 (UI Layout)

我們需要在螢幕上畫出控制器。

1.  在 Canvas 建立新的 **Panel**，命名為 `Controls`。
    -   把 Alpha 值調成 0 (透明底)。
2.  **D-Pad (方向鍵)**：
    -   在左下角放兩個 Button (或 Image)：`<` (左) 和 `>` (右)。
    -   Anchor 設為 **底端-左側 (Bottom-Left)**。
3.  **Jump Button (跳躍鍵)**：
    -   在右下角放一個 Button：`Jump`。
    -   Anchor 設為 **底端-右側 (Bottom-Right)**。

---

# 難點分析：按鈕 vs 按住

-   **一般 Button (OnClick)**：
    -   手指「點一下並放開」才觸發。
    -   適合：跳躍 (Jump)。
    -   **不適合：移動 (Move)**。因為移動需要「一直按著」。

-   **解決方案**：
    -   我們需要偵測 **PointerDown** (按下) 和 **PointerUp** (放開) 事件。

---

# 實作：手機輸入腳本

建立腳本 `MobileInput.cs`：

```csharp
using UnityEngine;

public class MobileInput : MonoBehaviour
{
    // 靜態變數，讓主角可以隨便讀取
    public static bool isLeftPressed = false;
    public static bool isRightPressed = false;
    public static bool isJumpPressed = false;

    // 給左鍵綁定
    public void OnLeftDown() { isLeftPressed = true; }
    public void OnLeftUp()   { isLeftPressed = false; }

    // 給右鍵綁定
    public void OnRightDown() { isRightPressed = true; }
    public void OnRightUp()   { isRightPressed = false; }
    
    // 給跳躍鍵綁定
    public void OnJumpDown() { isJumpPressed = true; }
    public void OnJumpUp()   { isJumpPressed = false; } // 跳躍其實不太需要 Up，但為了保險
}
```

---

# 設定 EventTrigger

1.  建立空物件 `MobileInputManager`，掛上 `MobileInput.cs`。
2.  選取 UI 上的 **左鍵 (<)**。
3.  Add Component -> **Event Trigger**。
4.  點 `Add New Event Type` -> **Pointer Down**。
    -   綁定 `MobileInputManager` -> `OnLeftDown`。
5.  點 `Add New Event Type` -> **Pointer Up**。
    -   綁定 `MobileInputManager` -> `OnLeftUp`。
6.  **右鍵 (>)** 與 **跳躍鍵** 依此類推。

---

# 修改主角程式 (PlayerController)

我們要同時支援鍵盤 (測試用) 與 手機 (發布用)。

```csharp
void Update()
{
    // 1. 讀取鍵盤
    float mx = Input.GetAxisRaw("Horizontal");

    // 2. 讀取手機 (覆蓋鍵盤)
    if (MobileInput.isLeftPressed) mx = -1;
    if (MobileInput.isRightPressed) mx = 1;

    // 3. 跳躍
    if ((Input.GetButtonDown("Jump") || MobileInput.isJumpPressed) && isGrounded)
    {
        Jump();
        MobileInput.isJumpPressed = false; // 按下即觸發，馬上重置
    }
    // ... (剩下的物理移動程式不用改)
}
```

---

# UI 優化：半透明與圖示

虛擬按鍵不要擋住畫面。

1.  把按鈕圖片的 **Alpha 值** 調低 (例如 100/255)，變成半透明。
2.  把文字 `<` 改成漂亮的箭頭圖示 (Sprite)。
3.  確保按鈕夠大！(手指很粗)，建議至少 100x100 像素。

---

# 總複習：我們學會了什麼？

1.  **Unity 介面與專案管理**。
2.  **Tilemap** 2D 地圖繪製。
3.  **C# 程式邏輯** (變數、判斷、迴圈、物件溝通)。
4.  **物理系統** (Rigidbody, Collider)。
5.  **Cinemachine** 運鏡。
6.  **Animator** 動畫。
7.  **UI** 介面與 **GameManager** 流程。
8.  **Android Build** 上架發布。

---



---



# 結語

> "Game development is hard, but seeing someone smile while playing your game makes it all worth it."

這門課只是個開始。
Unity 的世界還很大 (3D, VR, AR, Shader...)。
希望大家能保持熱情，繼續創作！

**祝大家期末順利，寒假愉快！**

---

# Q & A

最後一堂課，開放所有疑難雜症提問！

-   老師，我畢業專題想做這個...
-   老師，我想上架 Google Play 賺錢...

*(合照留念)*
