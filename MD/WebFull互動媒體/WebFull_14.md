---
marp: true
theme: HoraStyle
paginate: true
style: |
  :root {
    --title-bg: linear-gradient(90deg, #ea580c, #f97316);
    --title-text-color: #ffffff;
  }
  section.lead {
    background: linear-gradient(135deg, #431407 0%, #000000 100%);
  }
---

<!-- _class: lead -->
<!-- _paginate: false -->

### Chapter 14
# 進階無程式碼平台 - Wix

## Horazon
## 互動媒體設計 (一學期)

---

# 什麼是 No-Code / Low-Code？

<br>

**No-Code (無程式碼)** 運動正在席捲全球。
它讓不懂寫程式的人，也能運用工具做出專業的應用程式或網站。

-   **Google Sites**：超簡單，但太陽春。
-   **Wix**：功能強大，設計自由度高，外掛多。
-   **Webflow**：給設計師用的，產出的 Code 很乾淨 (學習門檻高)。
-   **WordPress**：全球市佔率最高 (40%)，但需要主機維護。

> **Wix 是目前最適合初學者的全方位平台。**

---

# 為什麼選 Wix？

<br>

1.  **所見即所得**：滑鼠拖到哪，網頁就長那樣。
2.  **海量模版**：不用從零開始，幾百個設計師做好的版型任你選。
3.  **App Market**：想要預約系統？購物車？聊天機器人？一鍵安裝。
4.  **免費方案**：雖然有廣告且網址不漂亮，但功能幾乎全開。

---

# Step 1: 註冊與選擇路徑

<br>

前往 [wix.com](https://wix.com) 註冊。
Wix 會問你很多問題，你可以選 **"Create a new site"**。

這時會有兩條路：
1.  **Wix ADI (人工智慧設計)**：回答幾個問題，AI 幫你生成網站 (太簡單，不推薦)。
2.  **Wix Editor (編輯器)**：**選這個！** 選擇一個 Template，然後進入編輯器自由修改。

---

# Step 2: 認識編輯器介面

<br>

介面有點像 PPT 或 Photoshop：

-   **左側工具列**：
    -   `+` (Add Elements)：新增圖片、文字、按鈕、形狀。
    -   `Pages & Menu`：管理網站頁面 (首頁、關於、聯絡)。
    -   `Site Design`：設定全站的主題色、字體。
    -   `App Market`：安裝外掛。
-   **上方工具列**：切換頁面、預覽 (Preview)、發布 (Publish)。
-   **右側工具列**：微調物件的大小、位置、對齊。

---

# Step 3: 新增元件 (Add Elements)

<br>

按下左上角的 `+` 號：

-   **Text**：標題、段落。
-   **Image**：上傳自己的圖，或用 Wix 提供的免費圖庫。
-   **Button**：各種樣式的按鈕，記得設定連結 (Link)。
-   **Strip (長條)**：**重要！** 這是網頁的「區塊」。
    -   建議把內容都放在 Strip 裡面，比較好管理背景圖和視差滾動效果。

---

# Step 4: 管理頁面 (Pages)

<br>

點擊左側的 **Pages & Menu**。

-   **新增頁面**：Home, About, Portfolio, Contact。
-   **調整順序**：拖拉改變導覽列的順序。
-   **隱藏頁面**：有些頁面不想出現在選單 (例如「感謝購買」頁)，可以設為 Hide。
-   **子選單**：把頁面往右拖一點，變成 Dropdown Menu。

---

# Step 5: 手機版優化 (Mobile Editor)

<br>

Wix 不是完全的 RWD (它不是用 % 計算)，它是**絕對定位**。
所以你需要手動調整手機版。

1.  點擊上方工具列的 **手機圖示**。
2.  進入 Mobile Editor 模式。
3.  **注意**：你在這裡的移動、隱藏，**不會影響電腦版**。
    -   字太大了？調小一點。
    -   圖片太佔位？按眼睛圖示隱藏 (Hide)。
4.  **千萬不要刪除元件** (Delete)，會連電腦版一起刪掉！只能用隱藏 (Hide)。

---

# Step 6: 發布上線 (Publish)

<br>

編輯時隨時可以按 **Preview** 預覽。
確認沒問題後，按右上角藍色的 **Publish**。

你的網址會長這樣：
`https://{你的帳號}.wixsite.com/{網站名稱}`

-   雖然有點長，但它是免費的且全球可存取！
-   你可以把它貼到 IG 自介或履歷表上。

---

# 常見問題

<br>

1.  **Wix 很慢？**
    -   因為它載入了很多功能 (JS)，初次開啟會慢一點點，但還在可接受範圍。
2.  **可以匯出成 HTML 嗎？**
    -   **不行**。Wix 是封閉系統，你不能把原始碼拿走放到自己的伺服器。
3.  **怎麼拿掉廣告？**
    -   付錢 (Upgrade to Premium)。(期末作業不需要付費)。

---

# 實作練習：Wix 初體驗

<br>

請登入 Wix，隨便選一個 Template 玩玩看：

1.  換掉大標題文字。
2.  換掉背景圖片。
3.  新增一個 "關於我" 的頁面。
4.  新增一顆按鈕，連到 Google。
5.  切換到手機版，把按鈕隱藏起來。
6.  按 Publish，把網址傳給旁邊的同學看。

---

# 下週預告

<br>

我們學了 Figma、HTML/CSS、也學了 Wix。
期末專案要來玩真的了！

**現代網頁製作 (期末專案啟動)**
-   期末要用 Wix 做一個完整的網站。
-   主題不限 (個人作品集、活動宣傳、線上商店...)。
-   我們會結合 **AI 生成素材** + **Figma 排版** + **Wix 實作**。

Start thinking about your final project topic!

---
