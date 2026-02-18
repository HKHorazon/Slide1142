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

### Chapter 04
# 網頁內容準備

## Horazon
## 互動媒體設計 (一學期)

---

# 為什麼需要 AI 輔助？

<br>

在過去，製作一個網站最花時間的往往不是「架設」本身，而是「**準備內容**」。

-   **文案卡關**： "關於我們" 到底要寫什麼？標題怎麼下才吸引人？
-   **圖片難找**：圖庫的照片太假，找不到符合品牌風格的圖片。
-   **設計沒靈感**：配色怎麼配都覺得怪怪的。

> **AI 工具可以幫助我們快速產出高品質的內容素材。**

---

# AI 內容生成的三大領域

<br>

在本週課程，我們將專注於以下三個面向：

1.  **文字生成**
    -   ChatGPT, Claude, Gemini
    -   用途：撰寫網站文案、標語、SEO 關鍵字。
2.  **圖片生成**
    -   Midjourney, Bing Image Creator, Adobe Firefly
    -   用途：生成背景圖、插畫、Logo、情境照。
3.  **設計輔助**
    -   Huemint, Khroma
    -   用途：生成配色方案、字體搭配建議。

---

# 1. 文字生成：你的 AI 文案寫手

<br>

網站需要大量的文字：
-   **Hero Section**：一句強而有力的 Slogan。
-   **關於我們**：一段感人肺腑的品牌故事。
-   **服務介紹**：清楚條列的服務項目與優勢。
-   **CTA 按鈕**：讓人忍不住想點的文字。

---

# Prompt Engineering (提示工程) 基礎

<br>

如何讓 AI 寫出好文案？關鍵在於 **Prompt (提示詞)**。

### 萬用公式：
**[角色設定] + [任務描述] + [限制條件] + [風格語氣]**

> **範例**：
> "你是一位專業的網頁文案寫手 (角色)。
> 請幫我為一家『日式極簡風格的咖啡廳』撰寫網站首頁文案 (任務)。
> 需要包含一個 Slogan 和一段 50 字的品牌故事 (限制)。
> 語氣要溫暖、放鬆、帶有職人精神 (風格)。"

---

# 實戰演練：生成 Hero Section 文案

<br>

讓我們試著用 ChatGPT 來發想。

**輸入**：
> "我想做一個『原神 (Genshin Impact)』的粉絲推廣網站。請幫我發想 5 個吸引人的首頁大標題和副標題。風格要充滿冒險感、自由與元素之力。"

**AI 可能的輸出**：
1.  **標題**：踏入提瓦特，你的冒險由此開始。
    -   **副標題**：在七種元素交匯的大陸，與夥伴一同尋找失散的親人。
2.  **標題**：風帶領你，穿越自由的國度。
    -   **副標題**：探索廣闊的世界，解開古老的謎題，見證旅途的終點。

---

# 實戰演練：生成「角色介紹」

<br>

**輸入**：
> "請幫我寫一位葬送的芙莉蓮動畫角色的介紹。先給我芙莉蓮主角的

**AI 輸出**：
> "芙莉蓮 (Frieren)，那位傳說中打倒魔王的精靈魔法使。擁有千年的壽命與強大的魔力，卻總是一臉淡然。她在勇者逝世後，才察覺自己從未真正了解人類。如今，她背起行囊，踏上蒐集魔法與追尋回憶的旅程，試圖理解生命的短暫與珍貴。"

> **Tip**：AI 寫完後，記得加上具體的設定 (例如：喜歡蒐集奇怪的魔法、早上起不來)，讓角色更生動。

---

# SEO 優化

<br>

寫好文案後，還要讓 Google 搜尋引擎喜歡。

**Prompt**：
> "請幫我找出 10 個與『鬼滅之刃 模型專賣』相關的高流量 SEO 關鍵字。並將這些關鍵字自然地融入到上面的品牌故事中。"

AI 會幫你把「鬼滅之刃公仔」、「炭治郎模型」、「禰豆子周邊」等關鍵字塞進文章裡，增加網站被搜尋到的機會。

---

# 2. 圖片生成：你的 AI 畫家

<br>

找不到適合的圖片？自己「算」一張！

### 常用工具：
-   **Midjourney** (付費)：目前畫質最強，需在 Discord 操作。
-   **Bing Image Creator** (免費)：使用 DALL-E 3 模型，支援中文指令。
-   **Adobe Firefly** (部分免費)：版權最乾淨，適合商用，整合在 Photoshop。

---

# 圖片生成 Prompt 技巧

<br>

描述越具體，圖片越精準。

### 結構：
**[主體] + [環境/背景] + [藝術風格] + [光影/視角] + [畫面比例]**

> **範例**：
> "一隻橘色的貓咪 (主體)，坐在陽光灑落的窗台上 (環境)，窗外是巴黎鐵塔 (背景)。水彩畫風格 (風格)，柔和的光線 (光影)。Aspect Ratio 16:9 (比例)。"

---

# 實戰演練：生成網頁背景圖 (Hero Image)

<br>

網頁的首頁大圖通常需要**留白**，方便壓上文字。

**Prompt (Midjourney)**：
> `/imagine prompt: a minimalist desk setup with a laptop and a coffee cup, white background with negative space on the right side, high quality, 4k, photorealistic --ar 16:9`

-   **Negative Space (負空間)**：告訴 AI 留白，不要把畫面填滿。
-   **--ar 16:9**：設定圖片比例為寬螢幕 (預設是正方形)。

---

# 實戰演練：生成圖示 (Icon) 與 Logo

<br>

雖然有 Recraft.ai 這種專門工具，通用型 AI 也能做。

**Prompt**：
> "flat vector icon of a coffee bean, minimal design, white background, orange color scheme"

> "simple logo design for a flower shop, letter 'F', elegant, pastel colors, vector style"

> **Tip**：生成的 Logo 通常是點陣圖 (JPG/PNG)，需要用 Illustrator 或線上工具轉成向量圖 (SVG) 才會清晰。

---

# 3. 設計輔助：AI 配色與排版

<br>

你是設計苦手嗎？讓 AI 幫你找靈感。

### 配色工具：
-   **Huemint**：AI 會根據你的設定，自動生成一組配色，並直接套用到網頁 Mockup 給你看。
-   **Khroma**：先挑選 50 個你喜歡的顏色，AI 會訓練出你的個人喜好模型，推薦無限種配色組合。

### Prompt 詢問配色：
> "請為我的『海洋生態保護』網站推薦 3 組配色方案，每組包含主色、輔助色、強調色，並附上 Hex Code。"

---

# 版權與法律問題

<br>

使用 AI 素材必須注意的紅線：

1.  **著作權歸屬**：目前美國法院判決，**純 AI生成的作品沒有著作權** (因為不是人類創作的)。這意味著別人也可以免費使用你生成的圖片。
2.  **商用限制**：
    -   **Midjourney**：付費會員擁有商用權。
    -   **Bing / Firefly**：請詳閱使用條款 (通常個人使用沒問題，商用要小心)。
3.  **肖像權**：盡量不要生成名人的臉 (Deepfake 風險)。

> **建議**：AI 用於提案、發想、或個人作業沒問題。若要用於大型商業專案，建議僅作為參考，最終還是由設計師繪製。

---

# 準備你的網站素材包

<br>

在開始製作網站前，請建立一個資料夾，整理好以下東西：

`/MyWebsiteAssets`
  ├── `/Images`
  │     ├── `hero-bg.jpg` (首頁大圖)
  │     ├── `about-me.jpg` (個人照)
  │     └── `logo.png`
  ├── `/Icons` (favicon.png, feature-icons...)
  └── `content.txt` (包含所有文案、Slogan、色碼)

> **這就是所謂的「素材準備」，是專業開發者的好習慣。**

---

# 作業說明：AI 素材準備

<br>

請為你上週規劃的網站，準備好素材：

1.  **文案**：使用 ChatGPT 生成 3 組 Slogan，選出一組最好的。
2.  **圖片**：使用 Bing Image Creator 生成一張首頁大圖 (Hero Image)。
3.  **配色**：確定你的網站主色碼 (Hex Code)。
4.  **整理**：將文案與圖片存檔，下週 Figma 實作課會用到！

---

# 推薦工具清單

<br>

### 文字
-   [ChatGPT](https://chat.openai.com/)
-   [Claude](https://claude.ai/)

### 圖片
-   [Bing Image Creator](https://www.bing.com/images/create) (免費，推薦)
-   [Adobe Firefly](https://firefly.adobe.com/)

### 設計
-   [Coolors](https://coolors.co/) (配色)
-   [Huemint](https://huemint.com/) (AI 配色)

---

# 下週預告

<br>

素材都準備好了嗎？
下週我們將進入專業 UI 設計工具：

**UI/UX 設計導論 - Figma 基礎**

-   註冊 Figma 帳號。
-   認識 Frame, Group, Component。
-   把我們今天生成的圖片和文案，拼湊成一張精美的網頁設計圖。



