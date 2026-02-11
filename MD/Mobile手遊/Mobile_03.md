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

# Chapter 03
# 2D 世界建構 (Tilemap)

## Horazon
## 手機遊戲開發

---

# 複習：上週重點

-   [x] 熟悉了 Unity 五大視窗。
-   [x] 學會使用 **Sprite Renderer** 顯示圖片。
-   [x] 學會 **Transform** (移動、旋轉、縮放)。
-   [x] 了解 **Sorting Order** 的前後關係。

---

# 本章目標

今天我們要打造遊戲的舞台！

1.  理解為什麼需要 **Tilemap**。
2.  學會 **Sprite Editor** 切割圖片。
3.  建立 **Tile Palette** (瓦片調色盤)。
4.  使用 **Brush** (筆刷) 繪製關卡。
5.  掌握 **Sorting Layer** (圖層管理)。

---

# 問題：如果不用 Tilemap...

假設你要做一個瑪利歐的關卡。
地板由 1000 個磚塊組成。

### 傳統做法：
-   你拉了 1000 個 Sprite 到場景裡。
-   Hierarchy 會有 1000 個 GameObject。
-   **災難！** 電腦變慢，你也找不到東西。

### Tilemap 做法：
-   像畫家一樣，用「筆刷」在「畫布」上塗抹。
-   整張地圖只算一個物件。
-   **效能好，管理方便。**


---

# Tilemap 四大天王

要使用這套系統，你需要認識四個名詞：

1.  **Grid (網格)**：這是爸爸，負責定義格子的大小。
2.  **Tilemap (地圖)**：這是畫布，顯示畫面用的。
3.  **Tile Palette (調色盤)**：這是顏料盤，選你要畫什麼磚塊。
4.  **Tile (瓦片)**：這是顏料，把圖片轉成 Unity 看得懂的瓦片資料。

---

# 步驟 1：準備素材 (Sprite Sheet)

通常遊戲素材會把很多小圖塞在同一張大圖裡，我們稱為 **Sprite Sheet**。

1.  匯入一張充滿磚塊的圖片。
2.  如果不切開，它就是一張大圖。
3.  我們需要用 **Sprite Editor** 把它切成一塊塊。


---

# 步驟 2：切割圖片 (Slicing)

1.  點選圖片，看 Inspector。
2.  **Sprite Mode**：從 `Single` 改為 **`Multiple`**。
3.  按下 **Apply**。
4.  點擊 **Sprite Editor** 按鈕 (如果沒安裝 2D Sprite 套件會找不到，請去 Package Manager 裝)。

---

# Sprite Editor 操作

1.  點選左上角的 **Slice** 下拉選單。
2.  **Type**：
    -   **Automatic**：自動偵測邊緣 (適合不規則圖案)。
    -   **Grid By Cell Size**：固定大小切割 (適合標準磚塊，如 64x64)。
3.  設定好後按下 **Slice** 按鈕。
4.  你會看到圖片被切出白色的框線。
5.  記得按右上角的 **Apply** 存檔。

---

# 步驟 3：開啟瓦片調色盤

就像小畫家一樣，我們要先打開調色盤。

1.  上方選單 **Window** -> **2D** -> **Tile Palette**。
2.  這個視窗很重要，建議拖曳並排在 Inspector 旁邊。


---

# 步驟 4：建立 Palette

1.  在 Tile Palette 視窗中，點選 **Create New Palette**。
2.  **Name**：取名 `LevelPalette`。
3.  **Grid**：選擇 `Rectangle` (矩形)。
4.  **Cell Size**：選擇 `Automatic` 或 `Manual`。
5.  點選 **Create**，並選擇一個資料夾存放 (建議 `Assets/Tiles/`)。

---

# 步驟 5：製作瓦片 (Tile Assets)

現在我們有空的調色盤，要把顏料 (圖片) 放上去。

1.  打開 Project 視窗，找到剛剛切好的圖片。
2.  **直接拖曳**整張圖 (或是切開的小圖) 到 **Tile Palette** 視窗的灰色區域。
3.  Unity 會問你要把這些 Tile 檔案存在哪。
    -   存到 `Assets/Tiles/`。
4.  完成後，你就會在調色盤上看到一格格的磚塊了！

---

# 步驟 6：建立畫布 (Tilemap Object)

顏料有了，現在要準備畫布。

1.  在 Hierarchy 按右鍵 -> **2D Object** -> **Tilemap** -> **Rectangular**。
2.  你會看到出現一個 `Grid` 物件，底下有一個 `Tilemap` 物件。

-   **Grid**：控制格子多大。
-   **Tilemap**：真正顯示圖案的地方 (有 Tilemap Renderer)。

---

# 步驟 7：開始繪畫！

1.  點選 Hierarchy 中的 **Tilemap** 物件 (這是你要畫的目標)。
2.  在 **Tile Palette** 選一個磚塊。
3.  使用上方工具列：
    -   **B (Pixel Paint)**：點選繪製單格。
    -   **U (Box Fill)**：拉框填滿一大片。
    -   **D (Erase)**：橡皮擦。
    -   **I (Picker)**：吸管，吸取場景上的圖案。

*(講師現場示範繪製過程)*

---

# 常見問題：格子對不準？

Q: 「老師，我畫上去的磚塊比格子小很多，或是大很多？」

A: 這是 **Pixels Per Unit (PPU)** 的設定問題。
-   檢查你的圖片 Inspector 設定。
-   如果你的磚塊是 64x64 像素，PPU 就該設為 **64**。
-   或者是調整 Grid 物件的 Cell Size (不推薦)。

**最佳解法**：確認素材規格，設定正確的 PPU。

---

# 進階技巧：圖層管理 (Sorting Layers)

場景變複雜後，你需要分層。
例如：背景的天空、中間的地板、前景的草叢。

Unity 預設只有 `Default` 圖層。我們來新增：
1.  Inspector 右上角 **Tag** 下方 -> **Layer** -> **Sorting Layer** -> **Add Sorting Layer...**
2.  這不是 Physics Layer，是 **Sorting Layer (渲染順序)**。

---

# 建議的圖層架構

點選 `+` 新增以下圖層 (順序越下面越前面)：

1.  **Background** (背景)
2.  **BackProps** (遠景裝飾)
3.  **Ground** (地板/主要遊玩層)
4.  **Props** (玩家會經過的裝飾)
5.  **ForeGround** (前景/遮擋物)
6.  **UI** (介面)

---

# 實戰應用：多層地圖

現在我們來做多層次關卡。

1.  在 Grid 下方，選取 Tilemap 按 Ctrl+D 複製一份，改名 `Background_Map`。
2.  Inspector -> Tilemap Renderer -> **Sorting Layer** 改為 `Background`。
3.  再複製一份 `Ground_Map`，Sorting Layer 改為 `Ground`。
4.  再複製一份 `Deco_Map`，Sorting Layer 改為 `Props`。

**現在你有三張透明片疊在一起，可以在不同層畫畫了！**

---

# Focus Mode (專注模式)

當你有好幾層 Tilemap 時，很容易畫錯層。

-   看 Scene 視窗右下角，有個 **Tilemap Focus** 下拉選單。
-   選擇你要畫的那一層。
-   其他層會變暗或隱藏，讓你專心畫當前這一層。

---

# 消除縫隙 (Fixing Gaps)

有時候你會發現磚塊之間有細微的縫隙。

### 原因：
這是貼圖濾鏡 (Filter Mode) 造成的。Unity 預設會做平滑處理 (Bilinear)。

### 解法：
1.  點選你的磚塊圖片素材。
2.  Inspector -> **Filter Mode** 改為 **Point (no filter)**。
3.  如果是像素風遊戲 (Pixel Art)，這步是必須的！
4.  **Compression** (壓縮) 改為 **None** 也會有幫助。

---

# 規劃你的第一個關卡

畫地圖不是亂塗鴉，要有邏輯。

1.  **起點**：玩家出生的地方 (要有平地)。
2.  **路徑**：引導玩家往右邊走。
3.  **跳躍挑戰**：挖洞，或是放高台。
4.  **邊界**：上下左右都要有牆壁或東西擋住 (除非是掉下去會死)。

---

# 什麼是 Palette Edit Mode？

如果你想整理調色盤 (把磚塊排整齊)...

1.  在 Tile Palette視窗上方點選 **Edit**。
2.  現在你可以用橡皮擦或移動工具來編輯「調色盤本身」了。
3.  整理完記得關閉 Edit 模式，不然會沒辦法畫到場景上。

---

# 總結

今天我們學會了：

1.  **Sprite Mode: Multiple** 切割圖片。
2.  **Tile Palette** 製作與管理。
3.  **Grid & Tilemap** 的父子關係。
4.  **Sorting Layers** 後製定圖層順序。
5.  使用筆刷繪製出多層次的遊戲場景。

---

# 下週預告

地圖畫好了，但還只是「畫」。
下週我們要開始寫程式，讓電腦聽你的話！

-   C# 程式語言入門。
-   變數 (什麼是 int, float?)。
-   方法 (Start, Update)。
-   讓電腦在 Console 說 "Hello World"。

---

# Q & A

-   找不到 Tile Palette？
-   畫不上去？(檢查有沒有選對 Tilemap 物件)
-   圖片切壞了？(Sprite Editor Reset 重切)

*(助教巡堂協助)*
