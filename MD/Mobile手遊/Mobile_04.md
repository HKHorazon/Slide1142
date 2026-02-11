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

# Chapter 04
# 程式基礎入門 (C# for Unity)

## Horazon
## 手機遊戲開發

---

# 複習：上週重點

-   [x] 建立了 Tilemap 關卡。
-   [x] 學會了切割素材與繪製地圖。
-   [x] 理解了 Layer 與 Sorting Layer。

但是... 這個地圖是死的，沒有任何反應。
今天要來賦予它靈魂！

---

# 本章目標

這堂課我們不畫圖，專注於**寫程式**。

1.  了解什麼是 **Script (腳本)**。
2.  學會創建與掛載 C# 腳本。
3.  認識基本語法：變數、方法、判斷式。
4.  在 Unity Console 印出 `Hello World`。

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

# 建立腳本的規則

1.  在 Project 視窗 (建議在 Scripts 資料夾) 按右鍵。
2.  **Create** -> **C# Script**。
3.  **立刻命名！** (不要點別的地方)。
    -   ❌ `NewBehaviourScript` (預設名，是大忌)
    -   ❌ `player movement` (不要有空白)
    -   ❌ `123Script` (不要數字開頭)
    -   ⭕ `PlayerController` (**大寫開頭**，駝峰式命名)

---

# 掛載腳本 (Attach)

腳本寫好了，要交給演員。

### 方法一：拖曳法
直接把腳本從 Project 拉到場景中的 GameObject 身上。

### 方法二：按鈕法
選取 GameObject，在 Inspector 最下方按 **Add Component**，搜尋腳本名稱。

---

# 開啟腳本

雙擊腳本檔案，會開啟 **Visual Studio** (或 VS Code)。

*(等待開啟中... 第一次會比較慢)*

---

# 腳本解剖學 (Anatomy)

```csharp
using UnityEngine; // 1. 引用工具箱

// 2. 類別名稱 (必須跟檔名一模一樣！)
public class MyScript : MonoBehaviour 
{
    // 3. 變數與方法寫在大括號裡面
    
    void Start() // 4. 預設方法
    {
        
    }
}
```

---

# 重要觀念：Class 與 檔名

<style scoped>
section { font-size: 30px; }
</style>

在 Unity 中，這件事經常導致新手卡關：

`public class Player : MonoBehaviour`
這邊的 `Player` **必須** 等於檔名 `Player.cs`。

如果你改了檔名，忘了改裡面的 Class 名稱...
**Unity 會報錯，且無法掛載腳本！**

> **Tip**: 如果要改名，在 VS 裡面按 F2 改名比較保險。

---

# 預設方法：Start()與Update()

Unity 預設會給你兩個 Magic Methods：

### `void Start()`
-   當遊戲**開始的瞬間**執行一次。
-   適合：初始化、設定血量、拿武器。

### `void Update()`
-   遊戲進行中**每一幀 (Frame)** 都執行。
-   約每秒 60 次 (60 FPS)。
-   適合：偵測按鍵、移動角色、持續扣血。

---

# 哈囉世界 (Hello World)

我們來讓電腦講話。

1.  在 `Start()` 的大括號內輸入：
    ```csharp
    Debug.Log("Hello World");
    ```
2.  **注意分號 `;`**：C# 每行指令結束都要加分號。
3.  存檔 (Ctrl + S)。
4.  回到 Unity 按 Play。
5.  看 **Console** (控制台) 視窗。

---

# 變數 (Variables)

變數就是**或是資料的箱子**。
每個箱子有不同的形狀，只能裝特定的東西。

### 常用資料型態：
-   **int** (整數)：存放整數 (`10`, `-5`, `0`)。
-   **float** (浮點數)：存放小數 (`3.14f`, `0.5f`)。**注意要把 `f` 加上去！**
-   **string** (字串)：存放文字 (`"Hello"`, `"Player1"` )。**要用雙引號包起來**。
-   **bool** (布林值)：存放是非 (`true`, `false`)。

---

# 宣告變數 (Declaration)

語法：`修飾詞 資料型態 變數名稱 = 初始值;`

```csharp
public int score = 0;
public float speed = 5.5f;
public string playerName = "Hero";
public bool isDead = false;
```

---

# Public vs Private

### **public** (公開)
-   允許其他腳本存取。
-   **最重要：會顯示在 Unity Inspector 面板！**
-   你可以直接在 Unity 調整數值，不用改程式。

### **private** (私有)
-   只有這個腳本自己看得到。
-   不會顯示在 Inspector (除非加 `[SerializeField]`)。
-   如果沒寫修飾詞，預設就是 private。

---

# 實作練習：我的個人檔案

1.  建立腳本 `MyProfile`。
2.  宣告變數：
    ```csharp
    public string myName = "Horazon";
    public int age = 18;
    public float height = 175.5f;
    public bool isStudent = true;
    ```
3.  掛載到場景上隨便一個物件。
4.  觀察 Inspector，試著修改數值。

---

#運算子 (Operators)

電腦最擅長算數學。

-   **算術**：`+`, `-`, `*`, `/`, `%` (取餘數)
-   **賦值**：`=` (把右邊給左邊)
-   **複合賦值**：
    -   `score += 10;` (等同 `score = score + 10;`)
    -   `hp -= 5;`
    -   `count++;` (加 1)

---

# 方法 (Method / Function)

方法是一連串指令的集合 (Function)。

```csharp
// 定義方法
void Jump()
{
    Debug.Log("跳起來！");
    // 這裡還可以寫施加力道...
}

// 呼叫方法 (Call)
void Update()
{
    Jump(); // 執行跳躍
}
```

---

# 條件判斷 (If Statement)

如果...就...。這是遊戲邏輯的核心。

```csharp
if (條件)
{
    // 這裡會在條件為 true 時執行
}
else
{
    // 這裡會在條件為 false 時執行
}
```

---

# 比較運算子

用來放在 `if` 的括號裡。

-   `==`：等於 (注意是兩個等號！)
-   `!=`：不等於
-   `>`：大於
-   `<`：小於
-   `>=`：大於等於
-   `<=`：小於等於

```csharp
if (hp <= 0)
{
    Debug.Log("Game Over");
}
```

---

# 邏輯運算子

組合多個條件。

-   `&&` (AND)：且 (兩邊都要對，才算對)。
-   `||` (OR)：或 (只要有一邊對，就算對)。
-   `!` (NOT)：相反。

```csharp
// 沒死 且 按下空白鍵
if (isDead == false && Input.GetKeyDown(KeyCode.Space))
{
    Jump();
}
```

---

# 實作練習：超速警告

1.  在 `Update()` 裡寫一個簡單邏輯。
2.  宣告 `public float speed;`。
3.  當 `speed > 100` 時，印出「太快了！」。
4.  回到 Unity，按 Play。
5.  在 Inspector 手動調整 Speed 數值，觀察 Console 變化。

---

# Unity 常用 API 簡介

`Debug.Log` 只是冰山一角。

-   `transform.Translate(x, y, z)`：移動物件。
-   `transform.Rotate(x, y, z)`：旋轉物件。
-   `Destroy(gameObject)`：自我毀滅。
-   `Input.GetKey(...)`：偵測按鍵。

*這些我們在後面的章節會詳細介紹。*

---

# 除錯指南 (Troubleshooting)

### 1. 紅色波浪線 (VS 裡)
-   語法錯誤。通常是忘了分號 `;`，或是括號不對稱。
-   滑鼠移過去看提示。

### 2. 紅色驚嘆號 (Unity Console 裡)
-   執行錯誤。雙擊錯誤訊息，會跳到程式碼出錯的那一行。

### 3. 未將物件參考設定為物件的執行個體 (NullReferenceException)
-   大魔王。表示你試圖去用一個「空的」變數。

---

# 總結

今天我們進入了程式設計的領域：

1.  **Script** 也是一種 Component。
2.  **Start** (一次) vs **Update** (每幀)。
3.  **變數** (int, float, string, bool)。
4.  **if / else** 邏輯判斷。

雖然還沒讓角色動起來，但這些是讓它動起來的地基！

---

# 下週預告

有了程式基礎，下週我們要加入物理學。

-   Rigidbody (剛體)：增加重力。
-   Collider (碰撞器)：這道牆過不去。
-   Physics Material：彈跳球與溜冰鞋。

---

# Q & A

-   VS 沒有智慧提示 (變色)？
    -   Edit -> Preferences -> External Tools -> 檢查是否有選 Visual Studio。
-   Console 沒東西？
    -   檢查 Collapse 有沒有按掉，或者有沒有按下 Play。

*(助教巡堂協助)*
