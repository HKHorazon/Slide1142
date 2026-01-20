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

### Chapter 11
# UI 介面設計 (UGUI)

## Horazon
## 手遊程式設計

---

# 章節目標

-   認識 Unity UI 系統 (**Canvas**)
-   製作 **分數顯示** (Text) 與 **血條** (Image)
-   了解 **Anchor (錨點)** RWD 概念

---

# 1. 建立畫布 (Canvas)

所有 UI 介面 (文字、按鈕、圖片) 都必須放在 Canvas 底下。

1.  Hierarchy 右鍵 -> UI -> **Canvas**。
2.  你會發現畫面多了一個超級大的白框，這是正常的。
3.  **重要設定**：
    -   點選 Canvas。
    -   Inspector -> Canvas Scaler。
    -   UI Scale Mode 改為 **Scale With Screen Size**。
    -   Reference Resolution 設為 **1920 x 1080** (手機主流解析度)。

---

# 2. 製作分數文字

1.  右鍵點 Canvas -> UI -> **Text (TMP)** (使用 TextMeshPro 較清晰)。
2.  (第一次用需點擊 Import TMP Essentials)。
3.  設定內容：
    -   Text: `Score: 0`
    -   Font Size: 60
    -   Color: 白色 (加一點 Outline 更好看)

---

# 3. 錨點 (Anchor) 的奧義

手機螢幕有長有短，UI 怎麼才不會跑版？要靠 **Anchor** (四個三角形圖示)。

**設定分數在左上角**：
1.  點選 Text 物件的 Rect Transform 左上角方塊。
2.  按住 **Alt 鍵** (重要！)。
3.  點擊「**左上角**」的圖示。
4.  你會發現 UI 自動貼齊左上角，且螢幕變大變小都會黏在那裡。

---

# 4. 程式控制顯示

回到 `GameManager`，我們要讓 UI 顯示真正的分數。

```csharp
using TMPro; // 1. 引用 TMP 函式庫

public class GameManager : MonoBehaviour
{
    // ... (原本的 Singleton) ...
    
    public TextMeshProUGUI scoreText; // 2. UI 欄位

    public void AddScore(int amount)
    {
        score += amount;
        
        // 3. 更新文字
        // scoreText.text 是字串， score 是數字，要用 ToString()
        scoreText.text = "Score: " + score.ToString(); 
    }
}
```

記得把場景上的 Text 拖進 Script 欄位！

---

# 5. 製作主選單 (Main Menu)

1.  建立一個新 Scene，存檔為 `Menu`。
2.  建立 Canvas。
3.  加入 **UI -> Button**。
4.  設定按鈕文字為 "Start Game"。
5.  建立一個簡單腳本 `MenuManager`：

```csharp
using UnityEngine.SceneManagement;

public void StartGame()
{
    // 切換到遊戲場景 (記得把場景加入 Build Settings)
    SceneManager.LoadScene("Level1");
}
```

---

# 6. 按鈕綁定事件 (OnClick)

1.  選取 Button 物件。
2.  Inspector 下方找到 **On Click ()** 清單。
3.  按下 **+** 號。
4.  將掛有腳本的物件 (MenuManager) 拖入空格。
5.  右側選單選擇 `MenuManager` -> `StartGame()`。

試玩看看，按下按鈕應該就會跳轉關卡了！

---

# 總結

-   **Canvas Scaler**：解決手機解析度適配問題。
-   **Anchor**：確定位 UI 永遠在螢幕正確位置。
-   **Button OnClick**：不需要寫程式偵測滑鼠，用拉選的即可觸發。

下一章，我們要讓遊戲變得「有感覺」，加入音樂與特效！
