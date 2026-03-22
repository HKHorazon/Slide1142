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
## 手機程式設計

---

# 複習：上週重點

-   [x] 認識了 C# 腳本 (Script)。
-   [x] 學會宣告 **變數** (public int score)。
-   [x] 學會使用 **Debug.Log**。

今天我們要結合 **Ch04 的物理** 與 **Ch05 的程式**，
做出真正的「遊戲機制」！

---

# 本章目標

1.  **Prefab (預製物件)**：大量製作金幣。
2.  **Tag (標籤)**：分辨誰是金幣、誰是陷阱。
3.  **Trigger (觸發器)**：穿越偵測。
4.  **Script Logic**：撰寫「吃金幣加分」的程式。

---

# 什麼是 Prefab (預製物件)？

這可能是 Unity 最重要的概念之一。

### 餅乾模具 (Cookie Cutter) 理論
-   **Prefab** = 模具。
-   **Instance (場景裡的物件)** = 印出來的餅乾。

如果你想把 100 塊餅乾從圓形改成星形...
**只要改模具 (Prefab) 或是資料，這 100 塊餅乾就會全部變成星形！**

---

# 實作練習 1：製作金幣 Prefab

1.  找到專案裡的金幣，放入遊戲中。
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
-   看場景裡的 10 枚金幣是不是都變紅了？**(這就是 Prefab 的威力)**

---

# Tag (標籤) 系統

程式怎麼知道玩家撞到的是「好吃的金幣」還是「會死的陷阱」？
我們需要貼標籤。

1.  點選任一物件，看 Inspector 最上方。
2.  點選 **Tag** 下拉選單 -> **Add Tag...**。
3.  點 `+` 號，新增兩個 Tag：
    -   `Coin`
    -   `Trap`

---

# 賦予 Tag

1.  選取 Project 裡的 **Coin Prefab**。
2.  將 Tag 改為 `Coin`。
3.  現在場景裡那 10 枚金幣都會自動變成 Coin Tag 了！

---

# 實作練習 3：收集金幣腳本

我們需要一個腳本來處理「碰到東西」的邏輯。
通常這個腳本會掛在**玩家 (Player)** 身上。

建立腳本 `PlayerCollection.cs`：

> 這個程式碼也可以嘗試由AI撰寫

---

```csharp
using UnityEngine;

public class PlayerCollection : MonoBehaviour
{
    public int score = 0; // 記分板

    // 當穿過 Trigger 時 (Unity 內建神奇方法)
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

# 程式碼解析

 `void OnTriggerEnter2D(Collider2D other)`
-   當有人 (other) 進入我的 Trigger 範圍時，會自動執行。
-   **前提**：雙方必須至少有一個人有 **Rigidbody 2D**，且一方有勾選 **Is Trigger**。

 `other.CompareTag("Coin")`
-   檢查撞到的那個東西，標籤是不是 "Coin"。

 `Destroy(other.gameObject)`
-   消滅撞到的那個東西 (金幣)。
-   如果寫成 `Destroy(this.gameObject)` 就是自殺了...

---

# 測試遊戲

1.  選取場景中的 **Player**。
2.  掛上 `PlayerCollection` 腳本。
3.  Play！
4.  控制玩家撞金幣。
5.  觀察：
    -   金幣是否消失？
    -   Console 是否顯示分數增加？
    -   Inspector 裡的 Score 變數是否增加？

---

# 陷阱製作 (Trap)

1.  找一張尖刺的圖片 。
2.  製作成 **Trap Prefab**。
3.  Tag 設為 `Trap`。
4.  Collider 勾選 **Is Trigger**。

---

# 實作練習 4：死亡邏輯 (重來)

在 `PlayerCollection` 最上方加入： `using UnityEngine.SceneManagement;`

修改 `OnTriggerEnter2D`：


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

吃到金幣要有「叮」一聲。

1.  專案中挑選一個音效檔。
2.  在腳本宣告：`public AudioClip coinSound;`
3.  在吃金幣邏輯加入：
    ```csharp
    AudioSource.PlayClipAtPoint(coinSound, transform.position);
    ```
4.  **記得回 Unity，把音樂檔拖進腳本的 Coin Sound 欄位！**

---

# 總結

今天我們完成了遊戲的核心迴圈：

1.  **Prefab** 讓我們快速佈置關卡。
2.  **Tag** 讓我們區分物件功能。
3.  **OnTriggerEnter2D** 偵測碰撞。
4.  **Destroy** 讓物件消失。

現在這已經是一個「有輸贏」的遊戲了！

---

# 下週預告

目前的遊戲還有一個大問題：
**攝影機不會動！**

主角走出畫面就看不到了。
下週我們將介紹神器 **Cinemachine**，讓攝影機像拍電影一樣自動跟著主角。

---

# Q & A

-   撞到金幣沒反應？
    -   檢查金幣有沒有勾 `Is Trigger`。
    -   檢查金幣 Tag 是不是 `Coin` (大小寫要在意)。
    -   檢查 Player 有沒有掛 `PlayerCollection` 腳本。
    -   檢查 Player 有沒有 `Rigidbody 2D`。

