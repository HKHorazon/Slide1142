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

### Chapter 13

# UI 介面設計 

## Horazon
## 手機程式設計

---

# 複習：上週重點

-   [x] 製作了 Idle, Run, Jump 動畫片段。
-   [x] 設定 Animator Controller 狀態機。
-   [x] 透過程式傳遞參數，讓主角動起來。

現在遊戲玩起來很有感了，但是...
「我吃了多少金幣？」
「我還剩多少血？」
今天我們要加上**抬頭顯示器 (HUD)**。

---

# 本章目標

1.  認識 **Canvas (畫布)** 系統。
2.  使用 **TextMeshPro** 顯示高品質文字。
3.  掌握 **RectTransform** 與 **Anchors (錨點)**。
4.  製作金幣計數器 UI。

---

# 什麼是 UI？

UI = User Interface (使用者介面)。
在遊戲中，通常指飄在螢幕最上層，**這層不會被攝影機移動影響**。

-   血條 (Health Bar)
-   分數 (Score)
-   按鈕 (Button)
-   搖桿 (Joystick)

---

# 建立 Canvas

所有 UI 元素都必須放在 **Canvas** 底下。

1.  Hierarchy 右鍵 -> **UI** -> **Canvas**。
2.  你會發現場景中出現一個**超級巨大**的白框。
    -   別擔心，這是正常的。
    -   Canvas 的 1 單位 = 螢幕的 1 像素 (1 pixel)。
    -   遊戲世界的 1 單位 = 1 公尺 (1 meter)。

3.  同時會自動產生一個 `EventSystem` 物件 (千萬別刪！刪了按鈕會失效)。

---

# Canvas Scaler (重要設定)

為了適應不同手機的解析度 (iPhone, Samsung...)，我們需要設定縮放模式。

1.  選取 Canvas。
2.  Inspector -> **Canvas Scaler** 元件。
3.  **UI Scale Mode**: 改為 **Scale With Screen Size**。
4.  **Reference Resolution**: 設為 **1920 x 1080** (標準 HD)。

*這樣一來，不管手機螢幕多大，UI 都會自動等比例縮放。*

---

# TextMeshPro (TMP)

Unity 舊版的 `Text` 很模糊，現在我們都用 `TextMeshPro`。

1.  Canvas 右鍵 -> **UI** -> **Text - TextMeshPro**。
2.  第一次使用會跳出視窗：**TMP Importer**。
3.  點擊 **Import TMP Essentials**。
    -   (下面的 Examples & Extras 不用裝)。
4.  完成後，你會看到一個清晰銳利的文字物件。

---

# 實作練習 1：金幣計數器

1.  在 Project 找一張金幣圖示 (Icon)。
2.  Canvas 右鍵 -> **UI** -> **Image**。
    -   Source Image: 拖入金幣圖。
    -   把圖移到左上角。
3.  建立一個 **Text (TMP)**。
    -   內容寫 `x 0`。
    -   放在金幣圖示旁邊。
    -   字體調大一點 (例如 60)。
    -   顏色改為黃色或白色。

---

# RectTransform 與 錨點 (Anchors)

這是 UI 最難懂也最重要的部分。

如果你把金幣 UI 放在左上角，但手機變寬了 (iPad)，UI 會跑掉嗎？

### Anchors (錨點)
Inspector 中有一個方塊圖示 (Anchor Presets)。
-   點擊它，按住 **Shift + Alt**。
-   選擇 **左上角 (Top-Left)**。
-   這代表：**UI 的左上角，永遠對齊螢幕的左上角**。

*不管螢幕怎麼變，金幣 UI 永遠會在左上角！*

---

# 實作練習 2：連結程式

UI 做好了，但還是顯示 0。我們要用程式更新它。

建立腳本 `UIManager.cs`：

```csharp
using UnityEngine;
using TMPro; // 1. 引用 TMP 命名空間

public class UIManager : MonoBehaviour
{
    public TextMeshProUGUI scoreText; // 2. 宣告 UI 變數

    public void UpdateScoreUI(int newScore)
    {
        scoreText.text = "x " + newScore.ToString();
    }
}
```

---

# 單例模式 (Singleton) 預告

為了讓所有東西 (金幣、玩家) 都能輕易找到 UIManager，我們通常會用**單例模式**。
這我們下週會詳細講，今天先用簡單的 `FindObjectOfType`。

---

# 修改 PlayerCollection 腳本

回到之前寫的吃金幣腳本 (`PlayerCollection.cs`)。

```csharp
    // 加入變數
    public UIManager uiManager;

    void Start()
    {
        // 自動尋找場景中的 UIManager
        uiManager = FindObjectOfType<UIManager>();
    }

    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("Coin"))
        {
            score++;
            // 更新 UI
            uiManager.UpdateScoreUI(score); 
            // ... (原本的音效與銷毀邏輯)
        }
    }
```

---

# 整合測試

1.  在 Hierarchy 建立一個空物件 `GameManager` (或 `_System`)。
2.  掛上 `UIManager` 腳本。
3.  把剛剛做的 TMP 文字物件，拖進 `Score Text` 欄位。
4.  按下 **Play**。
5.  去吃金幣。
    -   UI 數字有跟著跳動嗎？

---

# 進階 UI：世界座標 UI (World Space)

有時候我們想要 UI 跟著主角跑 (例如頭頂的血條、講話的氣泡)。

1.  建立一個新的 Canvas。
2.  Render Mode 改為 **World Space**。
3.  把 Canvas 縮得很小 (因為世界座標 1單位 = 1公尺)。
4.  把這個 Canvas 拖到 Player 物件底下，成為子物件。
5.  調整位置到頭頂。

*現在你就有一個跟著主角移動的 UI 了！*

---

# 字型問題 (Font Asset)

TextMeshPro 預設不支援中文字。
如果你輸入中文，會變成方塊 (口口口)。

### 解決方案：
1.  準備一個 `.ttf` 或 `.otf` 字型檔 (例如 Google Noto Sans)。
2.  Window -> TextMeshPro -> **Font Asset Creator**。
3.  設定 Source Font File。
4.  Character Set 選擇 **Custom Characters**，貼上你會用到的所有中文字 (或常用幾千字)。
5.  Generate Font Atlas -> Save。
6.  把這個新的 Asset 丟給 TMP 使用。

*(課堂上我們主要用英文就好，比較省事)*

---

# 常見錯誤 (Debug)

Q: UI 被場景擋住了？
A:
1.  Canvas 的 Sort Order 預設很高，理論上會在最上層。
2.  如果是 World Space Canvas，它就跟一般物件一樣受 Sorting Layer 影響，記得把它改為 `UI` Layer。

Q: 按鈕按不到？
A:
1.  檢查 EventSystem 還在不在？
2.  檢查前面有沒有 Image 擋住了射線 (Raycast Target 要關掉)。

---

# 總結

UI 是玩家獲取資訊的窗口。

1.  **Canvas** 是所有 UI 的家。
2.  **Anchor** 決定 UI 在不同螢幕的位置。
3.  **TextMeshPro** 顯示文字。
4.  透過腳本 **UpdateScoreUI** 即時更新數值。

---

# 下週預告

我們現在有計分，有主角，有地圖。
但死掉只能重來，沒有勝利畫面，也沒有主選單。

下週我們將整合遊戲流程 (Game Loop)：
-   **GameManager** (遊戲總管)。
-   Start Scene (主畫面)。
-   Level Scene (遊戲關卡)。
-   GameOver Scene (結算畫面)。

---

# Q & A

-   可以做血條 (Slider) 嗎？
    -   可以，Unity 有 Slider 元件。
    -   程式控制 `slider.value = currentHp / maxHp;`。
-   字體可以加外框嗎？
    -   TMP 的 Material 面板打開，勾選 **Outline** 就可以調粗細和顏色了。

*(助教巡堂協助)*
