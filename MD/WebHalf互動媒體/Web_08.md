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
<!--_paginate: false-->

### Chapter 08
# AI 輔助網頁開發體驗

## Horazon
## 互動媒體設計

---

# 寫程式的新時代

過去寫程式：
1.  買書看文件。
2.  上 Stack Overflow 找答案。
3.  複製貼上，然後修修改改。

現在寫程式：
1.  **問 AI**。
2.  **看 AI 寫**。
3.  **叫 AI 改**。

程式設計師的角色正在轉變，從 **Cader (打字工)** 變成 **Architect (架構師)**。

---

# AI 寫程式工具盤點

現在主流的 AI 輔助工具：

1.  **GitHub Copilot** (付費)
    -   直接整合在 VS Code 裡。
    -   你打註解，它幫你寫完程式碼。
2.  **ChatGPT / Gemini / Claude** (對話型)
    -   適合問問題、產生整段程式碼、解釋觀念。
    -   可以把錯誤訊息貼給它除錯。
3.  **Cursor** (AI 原生編輯器)
    -   基於 VS Code 修改，深度整合 AI。
    -   可以讀取整個專案的程式碼，給出更精準的建議。
4.  **v0.dev / Lovable** (Generative UI)
    -   用文字描述，直接生成精美的 UI 介面。

---

# 1. Cursor: AI 原生編輯器 (The AI-First Editor)

目前評價最高的 AI 寫程式工具，直接把 AI 裝進 VS Code 裡。

-   **Chat (Cmd+L)**：像 ChatGPT 一樣對話，但它**看得到你的整份程式碼**。
-   **Inline Edit (Cmd+K)**：選取一段程式碼，直接叫它「把這段改成置中對齊」。
-   **Composer (Cmd+I)**：多檔案編輯，叫它「幫我加一個登入頁面，包含 HTML/CSS/JS」，它會一次寫好三個檔案！
-   **Tab**：超級預測，甚至還沒打字它就猜到你要寫什麼。

---

# 2. GitHub Copilot: 你的結對工程師 (Pair Programmer)

微軟與 OpenAI 合作的強大助手 (付費)。

-   **Inline Suggestion**：你在打程式碼時，它會用灰色字體顯示建議，按 `Tab` 就寫完了。
-   **Chat**：也可以跟它聊天問問題。
-   **Workspace**：理解整個專案的上下文。
-   **Terminal**：在終端機遇到錯誤，直接問它怎麼修 (`gh copilot suggest`)。

---

# 3. v0.dev / Bolt.new: 生成式 UI 的魔法

連程式碼都不用寫了？

-   **v0.dev** (Vercel)：
    -   輸入 "一個科技感的 Dashboard"，它直接生成 **React + Tailwind CSS** 的程式碼。
    -   可以持續對話修改："把背景改成深色"。
-   **Bolt.new** (StackBlitz)：
    -   瀏覽器裡的開發環境，可以生成完整的**全端應用程式**。
    -   適合快速製作原型 (Prototype)。

---

# 4. 生成圖像素材 (AI Assets)

網頁需要圖片，不想用圖庫怎麼辦？

-   **Midjourney**：生成高品質、藝術感強的圖片 (付費)。
-   **Stable Diffusion**：開源、可安裝在本地端，控制力強。
-   **Recraft.ai**：專門生成 **向量圖 (SVG)** 與 **圖示 (Icon)**，網頁設計師必備！
-   **Adobe Firefly**：整合在 Photoshop 裡，可以**生成填色** (Generative Fill) 修補圖片。

---

# Prompt Engineering (提示工程)

如何讓 AI 寫出你要的程式碼？
關鍵在於 **Prompt (提示詞)** 的品質。

### ❌ 壞的 Prompt：
> "幫我寫一個網頁。"
(太籠統，AI 給你一個 Hello World)

### ✅ 好的 Prompt：
> "請幫我用 HTML5 和 CSS3 寫一個響應式 (RWD) 的咖啡廳 Landing Page。
> 風格要溫暖、使用大地色系。
> 包含一個置中的 Hero Section (滿版背景圖)、三欄式的特色介紹、以及頁尾。"

---

# 實用技巧 1: Context (上下文)

AI 沒有讀心術，你要給它足夠的資訊 (Context)。

-   **指定技術棧**： "請用 Bootstrap 5..." 或 "請用純 CSS Flexbox..."
-   **提供範例**： "像 Apple 官網那樣的導覽列..."
-   **角色扮演**： "你是一個資深前端工程師，請幫我優化這段程式碼..."

---

# 實用技巧 2: Debugging (除錯)

程式跑不動？別怕！

1.  把 Console 的 **紅色錯誤訊息** 複製起來。
2.  把你的 **程式碼** 複製起來。
3.  貼給 AI：
    > "我的程式碼出現這個錯誤，請幫我找出原因並修正："
    > [貼上錯誤訊息]
    > [貼上程式碼]

AI 通常能在一秒內告訴你錯在哪 (例如少一個分號)。

---

# 實用技巧 3: Explain Code (解釋程式碼)

看到一段看不懂的 Code (可能是網路上抄來的)？

> "請逐行解釋這段 JavaScript 在做什麼？特別是第 5 行的邏輯。"

AI 是最好的 **私人透過家教**，24小時待命，而且不會嫌你笨。

---

# AI 的侷限與風險

雖然 AI 很強，但它不是完美的：

1.  **幻覺 (Hallucinations)**：
    -   一本正經地胡說八道。
    -   可能會創造出不存在的函式庫或語法。
2.  **安全性 (Security)**：
    -   **千萬不要把 API Key 或密碼貼給 AI！**
    -   生成的程式碼可能有資安漏洞。
3.  **依賴性 (Dependency)**：
    -   如果你完全看不懂 AI 寫的東西，一旦出錯你就修不好。
    -   **你必須要是能審查 (Review) 程式碼的人！**

---

# Generative UI (生成式介面)

現在有更進階的工具，不用寫 Code 也能產出 UI。

例如 **v0.dev** (Vercel 開發)：
1.  輸入 "一個科技感的登入畫面，背景要有粒子特效"。
2.  它直接生成 React/Tailwind 程式碼給你。
3.  你可以複製貼上到專案裡。

還有 **Screenshot to Code**：
-   把這張網頁截圖丟給 AI。
-   AI 自動轉成 HTML/CSS 程式碼。

---

# 實作練習 Step 1: HTML 結構 (Structure)

現在我們來玩個遊戲：**「只出一張嘴寫網頁」**。
目標：建立一個 **個人作品集網站**。

**Prompt 提示詞：**
> "請幫我寫一個個人作品集網站的 HTML 結構，包含 Hero 區塊、關於我、作品集網格 (Grid)、聯絡表單。請使用語意化標籤。"

-   **觀察重點**：AI 是否使用了 `<header>`, `<main>`, `<section>`, `<footer>`？

---

# 實作練習 Step 2: CSS 樣式 (Style)

有了骨架，來幫它穿衣服。

**Prompt 提示詞：**
> "請幫上面的 HTML 加上 CSS 樣式。風格要極簡 (Minimalist)，黑白配色，字體用無襯線體。作品集區塊在手機上要變成單欄 (Mobile First)。"

-   **觀察重點**：
    -   是否使用了 Flexbox 或 Grid？
    -   是否寫了 Media Queries 做響應式？

---

# 實作練習 Step 3: JS 互動 (Interaction)

最後，加點靈魂。

**Prompt 提示詞：**
> "請幫我加一個 '回到頂端' 的按鈕，滑動超過 300px 時出現，點擊後平滑捲動回頂部 (Smooth Scroll)。"

-   **觀察重點**：
    -   是否使用了 `window.addEventListener('scroll')`？
    -   是否使用了 `window.scrollTo()`？

---

# 道德與未來

### 程式碼版權是誰的？
-   目前法律還在模糊地帶。
-   通常視為開發者的輔助產出。

### AI 會取代工程師嗎？
-   **Junior (初階)**：很危險，只會寫基本語法的人會被淘汰。
-   **Senior (資深)**：更強大，因為他們能指揮 AI 做瑣事，專注在架構設計。

> **AI 不會取代你，但「會用 AI 的人」會取代你。**

---

# 課程總結

在這 8 週的課程中，我們體驗了：

1.  **網頁基礎** (HTML/CSS)。
2.  **開發工具** (VS Code)。
3.  **互動邏輯** (JavaScript)。
4.  **現代框架** (React/Vue 概念)。
5.  **AI 輔助** (Copilot/ChatGPT)。

這只是網頁開發的冰山一角，
希望這門課能開啟你對程式設計的興趣！

---

# Keep Learning

網頁技術日新月異，保持好奇心是 key。

推薦資源：
-   **MDN Web Docs** (最權威的文件)
-   **W3Schools** (新手友善)
-   **YouTube** (很多免費教學)

**祝各位在未來的開發之路上，Bug 少一點，薪水多一點！**

