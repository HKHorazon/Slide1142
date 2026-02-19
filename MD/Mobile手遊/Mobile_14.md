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

### Chapter 14

# 遊戲流程控制 (GameManager)

## Horazon
## 手機遊戲開發

---

# 複習：上週重點

-   [x] 建立了 Canvas UI。
-   [x] 學習了 TextMeshPro 與 Image。
-   [x] 寫了 UI 更新程式。

但現在的遊戲只是「有分數的測試場景」。
沒有開始畫面，也沒有結束畫面。
今天我們要把它串起來！

---

# 本章目標

1.  理解 **Singleton (單例模式)**。
2.  建立 **GameManager**。
3.  製作 **MainMenu (主選單)** 場景。
4.  製作 **GameOver (結束)** 轉場。
5.  使用 `SceneManager` 進行場景切換。

---

# 遊戲的生命週期 (Game Loop)

一個完整的遊戲流程通常是：

1.  **Boot (啟動)**：Logo 展示。
2.  **Title (標題)**：按 Start 開始。
3.  **Level 1 (關卡)**：遊玩中。
4.  **Win / Lose (結算)**：顯示分數。
5.  **Replay / Quit**：重玩或離開。

目前我們只有 Step 3。

---

# 什麼是 GameManager？

我們需要一個「總管」來管理全域狀態。

-   現在是第幾關？
-   玩家現在幾分？
-   遊戲暫停了嗎？
-   玩家死了嗎？

這些資訊**不應該**存在 Player 身上 (因為 Player 會死掉被銷毀)。
應該存在一個**永不磨滅**的物件上。

---

# 單例模式 (Singleton Pattern)

保證全世界只有一個 GameManager，而且大家都找得到它。

```csharp
public class GameManager : MonoBehaviour
{
    // 靜態變數，存取自己
    public static GameManager Instance;

    void Awake()
    {
        // 如果還沒有人當老大，我就是老大
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject); // 切換場景時不要刪除我
        }
        else
        {
            // 如果已經有老大了，我這個冒牌貨就自殺
            Destroy(gameObject);
        }
    }
}
```

---

# 實作 GameManager

1.  建立腳本 `GameManager.cs`。
2.  複製上面的 Singleton 程式碼。
3.  加入計分變數：
    ```csharp
    public int totalScore = 0;
    
    public void AddScore(int amount)
    {
        totalScore += amount;
    }
    ```
4.  在場景建立空物件 `GameManager`，掛上腳本。

---

# 修改其他腳本

現在大家都要聽老大的話。

### PlayerCollection.cs
```csharp
    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("Coin"))
        {
            // 直接呼叫靜態 Instance，不用再 Find 了！
            GameManager.Instance.AddScore(1);
            Destroy(other.gameObject);
        }
    }
```

*(注意：這樣寫的前提是場景裡必須要有 GameManager)*

---

# 場景切換 (Scene Management)

Unity 用 `SceneManager.LoadScene` 來換場景。

-   `LoadScene(0)`：載入編號 0 的場景。
-   `LoadScene("Level1")`：載入名稱為 Level1 的場景。

**重要設定**：
使用 `LoadScene` 前，必須把場景加入 **Build Settings**。

1.  File -> **Build Settings**。
2.  把你的 `Level1` (或是目前的場景) 拖進去。

---

# 製作主選單 (MainMenu)

1.  File -> **New Scene** -> Basic 2D。
2.  Save as `MainMenu`。
3.  建立 UI -> **Text**：寫上遊戲標題 (例如 "Super Cat Run")。
4.  建立 UI -> **Button**：
    -   文字改為 "START GAME"。
    -   調整大小與位置到畫面中間。

---

# 寫一個主選單腳本

建立腳本 `MainMenu.cs`：

```csharp
using UnityEngine;
using UnityEngine.SceneManagement;

public class MainMenu : MonoBehaviour
{
    public string levelToLoad = "Level1";

    public void PlayGame()
    {
        SceneManager.LoadScene(levelToLoad);
    }

    public void QuitGame()
    {
        Application.Quit(); // 離開遊戲 (在 Editor 無效)
        Debug.Log("Quit Game");
    }
}
```

---

# 連接按鈕事件 (OnClick)

1.  把 `MainMenu.cs` 掛在 Canvas (或其他物件) 上。
2.  選取 Start 按鈕。
3.  找到 Inspector 的 **Button** 元件 -> **On Click ()**。
4.  點 `+` 號。
5.  把掛著腳本的 Canvas 拖進去。
6.  下拉選單選 **MainMenu** -> **PlayGame**。

*現在按下按鈕，就會跳轉到 Level1 了！*

---

# 製作 Game Over 畫面

1.  複製 MainMenu 場景，改名為 `GameOver`。
2.  把標題改成 "YOU DIED"。
3.  把按鈕改成 "RETRY"。
4.  修改按鈕事件，讓它跳回 `Level1` (或是 `MainMenu`)。
5.  **記得把 GameOver 場景加入 Build Settings！**

---

# 串接死亡邏輯

修改主角的死亡邏輯 (在 `PlayerCollection` 或 `GameManager`)：

```csharp
public void PlayerDie()
{
    // 存檔分數... (選修)
    // 跳轉到 GameOver 場景
    SceneManager.LoadScene("GameOver");
}
```

---

# 完整的遊戲流程

1.  啟動遊戲 -> 進入 `MainMenu`。
2.  按下 Start -> 載入 `Level1`。
3.  `GameManager` 初始化分數。
4.  玩家吃金幣 -> `GameManager` 加分。
5.  玩家死掉 -> 載入 `GameOver`。
6.  按下 Retry -> 載入 `MainMenu` 或 `Level1`。

---

# 跨場景資料傳遞 (DontDestroyOnLoad)

Q: 為什麼跳到 GameOver 後，分數歸零了？
A: 因為 `GameManager` 被銷毀了 (如果沒有設 DontDestroyOnLoad)。

如果我們有設定 Singleton + DontDestroyOnLoad：
-   `GameManager` 會一直活著。
-   到了 GameOver 場景，我們可以讀取 `GameManager.Instance.totalScore` 來顯示最終分數。

---

# 實作 GameOver 分數顯示

1.  在 GameOver 場景的 UI 加入一個 Text。
2.  寫一個腳本 `GameOverUI.cs`：

```csharp
void Start()
{
    int score = GameManager.Instance.totalScore;
    scoreText.text = "Final Score: " + score;
    
    // 顯示完可以重置分數，準備下一局
    GameManager.Instance.totalScore = 0; 
}
```

---

# 常見錯誤 (Debug)

Q: `LoadScene` 報錯 "Scene couldn't be loaded"？
A: 忘記把場景拉進 **Build Settings** 的 Scenes In Build 清單了。

Q: 按鈕沒反應？
A:
1.  On Click 沒綁定？
2.  場景裡沒有 EventSystem？
3.  前面有 Image 擋住射線？

Q: GameManager 出現兩個？
A: 檢查 Singleton 的 `Awake` 邏輯是否有寫 `Destroy(gameObject)`。

---

# 總結

今天我們把散落的珍珠串成項鍊。

1.  **SceneManager**：切換場景。
2.  **DontDestroyOnLoad**：保留資料。
3.  **Singleton**：全域管理。
4.  **Button OnClick**：UI 互動。

現在，這已經是一個完整的遊戲產品了。

---

# 下週預告

遊戲做好了，我們要把它裝進手機裡去炫耀！

-   **Build Settings** for Android.
-   **Player Settings** (換 Icon, 改名字)。
-   **Developer Mode** (開啟 USB 偵錯)。
-   建置 APK 檔案。

---

# Q & A

-   可以做暫停功能嗎？
    -   可以，`Time.timeScale = 0` (時間停止)。
    -   `Time.timeScale = 1` (時間恢復)。
-   可以做多關卡嗎？
    -   可以，Level1 通關碰觸發器 -> `LoadScene("Level2")`。

*(助教巡堂協助)*
