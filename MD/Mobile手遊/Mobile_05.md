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
# 程式基礎入門 (C# for Unity)

## Horazon
## 手機遊戲開發

---

# 複習：上週重點

-   [x] 使用 **Rigidbody 2D** 讓物件有重力。
-   [x] 使用 **Collider 2D** 讓物件有實體。
-   [x] 操控老師提供的 **Player** 在地圖上移動。

但是... 你有沒有想過，為什麼按下鍵盤，角色就會動？

---

# 本章目標

這堂課我們來揭開那個「黑盒子」的神秘面紗。

1.  了解什麼是 **Script (腳本)**。
2.  認識基本語法：**變數** (Variables)、**方法** (Methods)。
3.  在 Unity Console 印出 `Hello World`。
4.  (Optional) 偷看一眼 `PlayerController.cs`。

---

# 什麼是腳本 (Script)？

如果 GameObject 是演員，Component 是戲服...
那 **Script 就是劇本**。

它告訴演員：
-   什麼時候要走？
-   什麼時候要跳？
-   被打到要損多少血？

我們寫的劇本，也是一種 **Component**。

---

# 建立你的第一個腳本

1.  在 Project 視窗 (Script 資料夾) 按右鍵。
2.  **Create** -> **C# Script**。
3.  **立刻命名！** (不要點別的地方)。
    -   取名為 `MyFirstScript`。
4.  雙擊開啟它。

---

# 腳本解剖學 (Anatomy)

```csharp
using UnityEngine; // 1. 引用工具箱

// 2. 類別名稱 (必須跟檔名 MyFirstScript 一模一樣！)
public class MyFirstScript : MonoBehaviour 
{
    // 3. 變數與方法寫在大括號裡面
    
    void Start() // 4. 預設方法
    {
        
    }
}
```

---

# 讓電腦說話：Debug.Log

我們來測試一下。

1.  在 `Start()` 的大括號內輸入：
    ```csharp
    Debug.Log("Hello World");
    ```
2.  **注意分號 `;`**：C# 每行指令結束都要加分號。
3.  存檔 (Ctrl + S)。

---

# 掛載腳本 (Attach)

腳本寫好了，如果不給演員，它永遠不會被執行。

1.  回到 Unity。
2.  在場景中隨便選一個物件 (例如 Main Camera，或是自己建一個空物件)。
3.  把 `MyFirstScript` **拖曳** 到該物件的 Inspector 上。
4.  按下 **Play**。
5.  看 **Console** (控制台) 視窗 -> 應該會出現 "Hello World"。

---

# 變數 (Variables)

變數就是**裝資料的箱子**。

### 常用資料型態：
-   **int** (整數)：存放整數 (`10`, `-5`)。
-   **float** (浮點數)：存放小數 (`3.14f`)。**注意要把 `f` 加上去！**
-   **string** (字串)：存放文字 (`"Hello"` )。**要用雙引號**。
-   **bool** (布林值)：存放是非 (`true`, `false`)。

---

# 宣告變數

```csharp
public int score = 0;
public float speed = 5.5f;
public string playerName = "Hero";
public bool isDead = false;
```

### public (公開) 的魔力
-   只要加上 `public`，這個變數就會**顯示在 Unity Inspector 面板！**
-   你可以直接在 Unity 調整數值，不用改程式。

---

# 實作練習：我的個人檔案

1.  在腳本中宣告：
    ```csharp
    public string myName = "Horazon";
    public int age = 18;
    public float height = 175.5f;
    ```
2.  存檔，回到 Unity。
3.  看 Inspector，試著修改數值。

---

# 關於那個 PlayerController...

還記得上週我們用的 `PlayerController` 嗎？
它其實就是一個比較複雜的腳本。

裡面可能寫了：
-   `public float speed;` (走路速度)
-   `public float jumpForce;` (跳躍力道)

**因為它宣告了 public，所以你可以在 Inspector 調整主角跑多快！**
*(快去試試看！把主角改成超音速小子！)*

---

# 方法 (Method / Function)

方法是一連串指令的集合。
Unity 預設給我們兩個重要的方法：

### `void Start()`
-   當遊戲**開始的瞬間**執行一次。
-   適合：初始設定。

### `void Update()`
-   遊戲進行中**每一幀 (Frame)** 都執行 (約每秒 60 次)。
-   適合：偵測按鍵、持續移動。

---

# 條件判斷 (If Statement)

如果...就...。

```csharp
if (hp <= 0)
{
    Debug.Log("Game Over");
}
```

這就是遊戲邏輯的核心。
下週我們會用這個來做「吃到金幣就加分」的功能。

---

# 總結

今天我們打開了程式的大門：

1.  **Script** 也是 Component。
2.  **Debug.Log** 讓電腦說話。
3.  **變數 (Variable)** 是資料的箱子。
4.  **Public** 變數可以在 Inspector 調整。

雖然還沒寫很複雜的邏輯，但你已經知道怎麼跟 Unity 對話了。

---

# 下週預告

有了程式基礎，我們要來做遊戲機制了！

-   製作 **Prefab** (金幣)。
-   使用 **Trigger** (觸發器)。
-   寫程式判斷：**碰到金幣 -> 加分**。
-   寫程式判斷：**碰到陷阱 -> 死亡**。

---

# Q & A

-   VS 沒有變色 (沒有智慧提示)？
    -   Edit -> Preferences -> External Tools -> 檢查 Editor 有沒有選 Visual Studio。
-   Console 沒東西？
    -   檢查腳本有沒有**掛載**到場景物件上！(這是新手最常犯的錯)

*(助教巡堂協助)*
