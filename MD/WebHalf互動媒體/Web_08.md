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

程式設計師的角色正在轉變，從 **Coder (打字工)** 變成 **Architect (架構師)**。

---

# AI 寫程式工具盤點

現在主流的 AI 輔助工具：

1.  **ChatGPT / Gemini / Claude** (對話型)
    -   適合問問題、產生整段程式碼、解釋觀念。
    -   可以把錯誤訊息貼給它除錯。
2.  **Agent AI**
    -   基於 VS Code 修改，深度整合 AI。
    -   可以讀取整個專案的程式碼，給出更精準的建議。
3.  **v0.dev / Bolt.new** (Generative UI)
    -   用文字描述，直接生成精美的 UI 介面。


---
# 2. Agent AI: 你的 AI 數位代理

不再只是「問與答」，而是真正能「執行任務」的 AI。

-   **深度整合 VS Code**：
    -   AI 不只是個聊天視窗，它就像你的結對工程師，直接在編輯器中運作。
-   **具備環境感知與操作能力**：
    -   **讀取目錄**：它能看到整個專案的資料夾結構，理解代碼之間的關聯。
    -   **主動修改**：可以直接對檔案進行讀取、修改、甚至建立新檔案。
-   **實戰案例：Antigravity Codex**：
    -   這就是你現在正在體驗的工具！
    -   它能「聽懂」你的需求，並轉換成實際的程式碼變更與檔案操作。


---

# 3. v0.dev / Bolt.new: 生成式 AI 的魔法

連程式碼都不用寫了？

-   **v0.dev** (Vercel)：
    -   輸入 "一個科技感的 Dashboard"，它直接生成 **React + Tailwind CSS** 的程式碼。
    -   可以持續對話修改："把背景改成深色"。
-   [**Bolt.new**](https://bolt.new/)：
    -   瀏覽器裡的開發環境，可以生成完整的**全端應用程式**。
    -   適合快速製作原型 (Prototype)。


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

# 未來網站開發


### AI 會取代工程師嗎？
-   **Junior (初階)**：很危險，只會寫基本語法的人會被淘汰。
-   **Senior (資深)**：更強大，因為他們能指揮 AI 做瑣事，專注在架構設計。

> **AI 不會取代你，但「會用 AI 的人」會取代你。**

---

# 課程總結

在這幾週的課程中，我們體驗了：

1.  **網頁基礎** (HTML/CSS)。
2.  **開發工具** (VS Code)。
3.  **互動邏輯** (JavaScript)。
4.  **現代框架** (React/Vue 概念)。
5.  **AI 輔助** (Copilot/ChatGPT)。

這只是網頁開發的冰山一角，
希望這門課能開啟你對網頁設計的興趣！

---

# Keep Learning

網頁技術日新月異，保持好奇心是 key。

推薦資源：
-   **MDN Web Docs** (最權威的文件)
-   **W3Schools** (新手友善)
-   **YouTube** (很多免費教學)

**祝各位在未來的開發之路上，Bug 少一點，薪水多一點！**

