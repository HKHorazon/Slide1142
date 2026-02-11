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

### Chapter 06
# 互動機制與金幣 

## Horazon
## 手機遊戲開發

---

# 複習：上週重點

-   [x] 物理與碰撞系統 (Rigidbody & Collider)。
-   [x] 物理材質 (Physics Material)。
-   [x] Trigger (觸發器) 的概念。

但目前為止，撞到東西只會從 Console 說「痛」，這不是遊戲啊！
今天要來做真正的**遊戲機制**。

---

# 本章目標

我們將製作遊戲中最經典的元素：

1.  **Prefab (預製物件)**：大量製作金幣。
2.  **Tag (標籤)**：分辨誰是金幣、誰是陷阱。
3.  **Script Logic**：吃金幣加分、踩陷阱重來。
4.  **Audio**：加入吃金幣的音效。

---

# 什麼是 Prefab (預製物件)？

這可能是 Unity 最重要的概念之一。

### 餅乾模具 (Cookie Cutter) 理論
-   **Prefab** = 模具。
-   **Instance (場景裡的物件)** = 印出來的餅乾。

如果你想把 100 塊餅乾從圓形改成星形...
**只要改模具 (Prefab) 或是資料，這 100 塊餅乾就會全部變成星形！**


---

# 為什麼需要 Prefab？

想像你場景裡有 50 枚金幣。

**不用 Prefab：**
-   你想把金幣變大一點。
-   你必須選取 50 個物件，一個個改 (或是全選改)。
-   如果以後又要改顏色？又要再做一次。

**使用 Prefab：**
-   雙擊 Prefab 檔案進入編輯。
-   改一次。
-   **全世界的 50 枚金幣同步更新！**

---

# 實作練習 1：製作金幣 Prefab

1.  在場景建立一個 **Circle** (改名 Coin)。
2.  將顏色改為黃色。
3.  加入 **Circle Collider 2D**。
4.  勾選 **Is Trigger** (因為我們要穿過它)。
5.  **關鍵步驟**：將 `Coin` 從 Hierarchy 拖曳到 Project 視窗的 `Prefabs` 資料夾中。
6.  你會發現 Hierarchy 的 `Coin` 字體變成**藍色**了。


---

# 實作練習 2：量產金幣

現在你有了模具。

1.  從 Project 視窗把 `Coin` Prefab 拖進場景。
2.  拖 10 次，放在不同位置。
3.  或者用 Ctrl+D 複製場景裡已經是 Prefab 的金幣。

**試驗**：
-   點選 Project 裡的 Coin Prefab。
-   修改顏色變成紅色。
-   看場景裡的 10 枚金幣是不是都變紅了？

---

# Unpack Prefab (解壓縮)

如果你希望某個金幣「與眾不同」，不再受 Prefab 控制...

1.  在該物件上按右鍵 -> **Prefab** -> **Unpack**。
2.  它會變回普通的 GameObject (黑色字體)。
3.  之後修改 Prefab，這個物件就不會跟著變了。

---

# Tag (標籤) 系統

程式怎麼知道玩家撞到的是「好吃的金幣」還是「會死的陷阱」？

我們需要貼標籤。

### Unity 內建標籤：
-   **Untagged** (預設)
-   **Player**
-   **MainCamera**
-   ...

---

# 自訂 Tag

1.  點選任一物件，看 Inspector 最上方。
2.  點選 **Tag** 下拉選單 -> **Add Tag...**。
3.  點 `+` 號，新增兩個 Tag：
    -   `Coin`
    -   `Trap`

*(注意：大小寫要完全一致，建議首字大寫)*

---

# 賦予 Tag

1.  選取 Project 裡的 **Coin Prefab**。
2.  將 Tag 改為 `Coin`。
3.  現在場景裡那 10 枚金幣都會自動變成 Coin Tag 了！

*(再次證明 Prefab 的強大)*

---

# 實作練習 3：收集金幣腳本

我們需要一個腳本來處理「碰到東西」的邏輯。
通常這個腳本會掛在**玩家 (Player)** 身上。


建立腳本 `PlayerCollection.cs`：

```csharp
using UnityEngine;

public class PlayerCollection : MonoBehaviour
{
    public int score = 0; // 記分板

    // 當穿過 Trigger 時
    void OnTriggerEnter2D(Collider2D other)
    {
        // 如果撞到的東西標籤是 "Coin"
        if (other.CompareTag("Coin"))
        {
            // 1. 加分
            score++;
            Debug.Log("吃到金幣了！目前分數：" + score);

            // 2. 銷毀金幣 (other.gameObject 是金幣，不是我)
            Destroy(other.gameObject);
        }
    }
}
```

---

# 測試遊戲

1.  場景上有一個代表玩家的膠囊 (或是方塊)。
2.  掛上 `PlayerCollection` 腳本，還有 `Rigidbody 2D`。
3.  確認金幣都有勾 `Is Trigger` 且 Tag 是 `Coin`。
4.  Play！
5.  控制玩家撞金幣，觀察金幣是否消失？Console 分數是否增加？

---

# 陷阱製作 (Trap)

1.  找一張尖刺的圖片 (或用三角形 Sprite)。
2.  製作成 **Trap Prefab**。
3.  Tag 設為 `Trap`。
4.  Collider 也可以勾 Is Trigger (代表碰到就死)。

---

# 遊戲重來 (Reload Scene)

當玩家碰到陷阱，我們希望遊戲重來。
這需要用到 **SceneManagement**。

在 `PlayerCollection` 最上方加入：
```csharp
using UnityEngine.SceneManagement; // 引用場景管理工具
```

---

# 實作練習 4：死亡邏輯

修改 `OnTriggerEnter2D` 方法，加入陷阱判斷：

```csharp
    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("Coin"))
        {
            score++;
            Destroy(other.gameObject);
        }
        else if (other.CompareTag("Trap")) // 如果撞到陷阱
        {
            Debug.Log("你死了！");
            // 重新讀取目前場景
            SceneManager.LoadScene(SceneManager.GetActiveScene().name);
        }
    }
```

---

# 音效回饋 (Audio)

吃金幣要有「叮」一聲才爽。

1.  準備一個 mp3 音效檔，放入 `Audio` 資料夾。
2.  但在哪裡播放？
    -   如果在金幣身上放 AudioSource，金幣被 Destroy 的瞬間，聲音也會被切斷！

### 解法：AudioSource.PlayClipAtPoint
這是一個靜態方法，會在特定位置產生一個暫時的聲音物件，播完自動銷毀。

---

# 實作練習 5：加入音效

1.  在腳本宣告變數：
    ```csharp
    public AudioClip coinSound;
    ```
2.  修改吃金幣邏輯：
    ```csharp
    if (other.CompareTag("Coin"))
    {
        score++;
        // 在金幣的位置播放聲音 (音量 1.0)
        AudioSource.PlayClipAtPoint(coinSound, other.transform.position, 1.0f);
        Destroy(other.gameObject);
    }
    ```
3.  **記得回 Unity，把音樂檔拖進腳本的 Coin Sound 欄位！**

---

# 常見錯誤 (Debug)

Q: 撞到金幣沒反應？
A:
1.  金幣有 Collider 2D 嗎？
2.  金幣有勾 Is Trigger 嗎？
3.  金幣的 Tag 設對了嗎？(拼字要一樣)
4.  Player 身上有 Rigidbody 2D 嗎？(碰撞雙方至少要有一方有剛體)

Q: 聲音沒出來？
A: 檢查 Inspector 的 Coin Sound 欄位是不是空的 (None)。

---

# 總結

今天我們完成了遊戲的核心迴圈雛形：

1.  **Prefab** 讓我們快速佈置關卡。
2.  **Tag** 讓我們區分物件功能。
3.  **Destroy** 讓物件消失。
4.  **SceneManager** 讓遊戲重來。

現在這已經是一個「能玩」的遊戲了！

---

# 下週預告

目前的遊戲還有一個大問題：
**攝影機不會動！**

主角走出畫面就看不到了。
下週我們將介紹神器 **Cinemachine**，讓攝影機像拍電影一樣運鏡。

---

# Q & A

-   可以做補血道具嗎？(原理跟金幣一模一樣，只是 score++ 變成 hp++)
-   可以做會動的敵人嗎？(加上移動程式的 Trap 就是敵人了)

*(助教巡堂協助)*
