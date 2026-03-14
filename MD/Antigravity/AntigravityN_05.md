---
marp: true
theme: HoraStyle
paginate: true
style: |
  :root {
    --title-bg: linear-gradient(90deg, #581c87, #64748b);
    --title-text-color: #ffffff;
  }
  section.lead {
    background: linear-gradient(135deg, #1e1b4b 0%, #000000 100%);
  }
---

<!-- _class: lead -->
<!-- _paginate: false -->
### Chapter 4
# Getting Started: Google Antigravity
## 從零開始的開發者指南
## Tutorial & Google Cloud Integration

---

# 本章大綱 (Agenda)

本章將帶領你完成 Antigravity 的安裝與基礎設置：

1.  **Antigravity 簡介**：核心概念回顧
2.  **環境準備**：下載與安裝
3.  **首次啟動**：驗證與授權流程
4.  **工作區設置**：初始化你的開發環境
5.  **介面導覽**：熟悉操作面板
6.  **實際演練**：第一個 AI 協作任務
7.  **雲端整合**：Google Cloud 連動

---

# 1. Antigravity 簡介

### 什麼是 Antigravity?
- **Agent-First Platform**：不僅僅是 IDE，而是以 AI 代理為核心的開發環境。
- **免費預覽 (Preview)**：目前提供個人 Gmail 帳戶免費使用。
- **實驗性質**：由 Google Labs 推出，快速迭代中。

### 為什麼選擇它？
- 深度整合 **Google Cloud Platform (GCP)**。
- 內建強大的 **Gemini 模型**。
- 支援 **Agentic Workflow** (自主規劃與執行)。

---

# 2. 環境準備：硬體與系統

在安裝之前，請確認你的電腦符合基本要求：

### 支援的作業系統
- **macOS**：支援 Apple Silicon (M1/M2/M3) 與 Intel 晶片。
- **Windows**：支援 Windows 10/11 (需安裝 WSL2)。
- **Linux**：支援主流發行版 (Ubuntu, Debian)。

### 建議規格
- **RAM**：至少 16GB (AI 運算與 IDE 需佔用記憶體)。
- **Disk**：至少 10GB 可用空間。

---

# 3. 下載安裝程式

### Step 1: 前往官網
請開啟瀏覽器，前往 Antigravity 官方下載頁面：
> **[antigravity.google/download](https://antigravity.google/download)**

### Step 2: 選擇版本
- 網頁會自動偵測你的作業系統。
- 點擊 **Download for [Your OS]** 按鈕。
- 檔案大小約 **150MB - 200MB**。

---

# 4. 安裝過程：macOS 注意事項

### 安全性警告
如果你是 macOS 使用者，首次開啟可能會遇到：
> *"Antigravity is an app downloaded from the internet. Are you sure you want to open it?"*

### 解決方法
1.  點擊 **Open** (開啟)。
2.  若被系統阻擋，請前往 **System Settings (系統設定)**。
3.  找到 **Privacy & Security (隱私權與安全性)**。
4.  在下方點擊 **Open Anyway (仍要開啟)**。

---

# 5. 安裝過程：Windows 注意事項

### 安裝 WSL (Windows Subsystem for Linux)
- Antigravity 的部分後端功能依賴 Linux 環境。
- 如果你的電腦尚未安裝 WSL，安裝程式會提示你安裝。

### 防火牆設定
- 首次啟動時，Windows 防火牆可能會跳出詢問。
- 請勾選 **Private networks (私人網路)** 並允許存取。
- 這是為了讓 Agent 能與本地伺服器通訊。

---

# 6. 首次啟動 (First Launch)

### 啟動應用程式
- 完成安裝後，從應用程式列表啟動 **Antigravity**。
- 你會看到一個極簡的歡迎畫面。

### 等待初始化
- 系統會自動下載必要的 AI 模型元件與依賴套件。
- 此過程可能需要 **2-3 分鐘**，請保持網路連線。

---

# 7. 帳號驗證 (Authentication)

### 登入 Google 帳號
1.  應用程式會彈出瀏覽器視窗。
2.  請使用你的 **個人 Gmail 帳號** 登入。
    > 目前企業帳號 (Workspace) 可能會有存取限制。

### redirect
- 登入成功後，瀏覽器會詢問是否將控制權轉回 Antigravity。
- 請點擊 **Open Antigravity**。

---

# 8. 授權與權限 (Permissions)

### 授予核心權限
AI Agent 需要實際操作你的電腦，因此需要較高的權限：

1.  **File System (檔案系統)**：讀寫專案檔案、建立資料夾。
2.  **Network (網路)**：下載套件、查詢文件、連線 GCP。

> **注意**：請務必點擊 **Allow (允許)**，否則 Agent 將無法執行任何任務。

---

# 9. 使用者條款與隱私 (Terms)

### 條款確認
- 畫面會顯示 **Terms of Use** (使用條款)。
- 這是實驗性產品，內容可能包含數據收集條款 (用於改善模型)。

### Opt-in 選項
- 你可以選擇是否分享使用數據與崩潰報告。
- 勾選或取消勾選後，點擊 **Next** 繼續。

---

# 10. 建立工作區 (Workspace Setup)

### 選擇專案路徑
- 系統會詢問你要在哪裡開始工作。
- 建議建立一個新的資料夾，例如：`~/Projects/Antigravity_Demo`。

### 初始化結構
Antigravity 會在該目錄下建立隱藏資料夾 `.antigravity/` 或 `.agent/`：
- 用於存放記憶 (Memory)。
- 用於存放設定檔 (Config)。
- **請勿手動刪除此資料夾**。

---

# 11. 介面導覽：主視窗

### 1. Activity Bar (左側)
- **Explorer**：檔案總管。
- **Search**：全域搜尋。
- **Antigravity**：Agent 控制中心 (機器人圖示)。

### 2. Editor Area (中間)
- 基於 VS Code 的編輯體驗。
- 支援 Syntax Highlighting、Intellisense。

### 3. Chat Panel (右側/底部)
- 與 Agent 溝通的主要介面。

---

# 12. 介面導覽：Agent 面板

當你點擊左側的 **Robot Icon**，會進入 Agent 專屬面板：

- **Chat History**：與 AI 的對話紀錄。
- **Task List**：AI 目前生成的任務清單。
- **Artifacts**：AI 產出的計畫書或文件。
- **Tools Status**：顯示 AI 正在使用的工具 (讀檔、寫檔)。

---

# 13. 設定：繁體中文介面

為了讓學習更順暢，我們先將介面中文化：

1.  按下 `Ctrl+Shift+X` (macOS: `Cmd+Shift+X`) 開啟 Extensions。
2.  搜尋 **"Chinese (Traditional)"**。
3.  點擊 **Install**。
4.  安裝完成後，右下角會提示 **Restart** 重啟。
5.  重啟後介面即變為繁體中文。

---

# 14. 第一次對話：Hello World

讓我們試著下達第一個指令：

### 輸入指令
在 Chat Panel 輸入：
> *"請幫我建立一個 Python 的 Hello World 程式，並寫一個簡單的說明檔 README.md"*

### 觀察 AI 行為
1.  AI 會**思考** (Reasoning)。
2.  AI 會**執行工具** (Create File)。
3.  你會看到檔案列表中出現 `hello.py` 和 `README.md`。

---

# 15. Agentic Mode 實戰

### 切換模式
- 點擊輸入框旁邊的 **模式切換按鈕** (通常是 Robot 圖示)。
- 邊框變色 (通常是紫色或金色)，代表進入 **Agentic Mode**。

### 任務：Git Commit
試著修改 `README.md`，然後輸入：
> *"幫我把這些變更 Commit 起來，訊息要符合 Conventional Commits 規範"*

### 結果
- Agent 會自動偵測變更 (`git status`)。
- Agent 會自動執行 Commit (`git commit -m "..."`)。

---

# 16. 雲端整合：Google Cloud

Antigravity 的強項在於與 GCP 的無縫接軌。

### 是否需要信用卡？
- 基礎功能 (本地開發) **不需要**。
- 若要部署到 Cloud Run 或使用 Vertex AI API，則需綁定 **GCP Billing Account**。

### 免費額度
- Google Cloud 通常提供新用戶 **$300 美金** 的試用額度。
- Cloud Run 與 Cloud Functions 均有永久免費額度 (Free Tier)。

---

# 17. 連接 Google Cloud 專案

### 指令連接
在 Chat Panel 輸入：
> *"請幫我登入 Google Cloud，並設定目前的專案 ID 為 [你的專案ID]"*

### 自動化流程
1.  Agent 會呼叫 `gcloud auth login` (若已安裝 SDK)。
2.  若無 SDK，Agent 會引導你或嘗試使用 built-in 工具。
3.  設定完成後，Agent 即可直接操作你的雲端資源。

---

# 18. 部署應用程式 (Deployment)

想像一下，傳統部署需要寫 Dockerfile、設定 YAML...
在 Antigravity，你只需要說：

> *"請幫我把目前的 Python 程式部署到 Google Cloud Run，設為公開存取。"*

### Agent 的動作
1.  檢查程式碼與依賴 (requirements.txt)。
2.  生成 `Dockerfile` (如果沒有)。
3.  執行 `gcloud run deploy` 指令。
4.  回傳部署完成的 **URL** 給你。

---

# 19. Vertex AI 整合

### 什麼是 Vertex AI?
- Google 的一站式 AI 開發平台。
- 可以訓練模型、部署模型。

### Antigravity 的角色
- 你可以告訴 Agent：
  > *"寫一段程式碼，呼叫 Vertex AI 的 Gemini Pro API 來分析圖片。"*
- Agent 會自動幫你引入正確的 Client Library，並寫好範例程式碼。

---

# 20. Skill System (技能系統)

我們在第二章提過 Skill，現在是時候安裝它了。

### 內建 Skills
- Antigravity 預設搭載了基礎的文件處理與終端機操作 Skills。

### 擴充 Skills
- 你可以告訴 Agent：
  > *"請幫我建立一個 Skill，用來檢查專案中的 TODO 註解，並整理成報告。"*
- Agent 會在 `.agent/skills/` 下生成對應的腳本。

---

# 21. 常見問題 (Troubleshooting)

### Q1: Agent 卡住了怎麼辦？
- 點擊對話框旁的 **Stop (停止)** 按鈕。
- 嘗試重新輸入指令，或切換回 **Fast Mode**。

### Q2: 權限錯誤 (Permission Denied)
- 檢查是否在安裝時拒絕了某些權限。
- macOS 使用者請檢查 **系統設定 > 隱私權 > Full Disk Access**。

---

# 22. 最佳實踐 (Best Practices)

### 1. 小步迭代
- 不要一次叫 AI 做整個系統。
- 拆解任務：先建立架構 -> 實作功能 -> 補充測試。

### 2. 隨時 Review
- 雖然 Agent 很強，但仍會犯錯 (幻覺)。
- 重要程式碼請務必親自 Review。

### 3. 版控優先
- **永遠在 Git Repository 中工作**。
- 讓 Agent 亂搞前，先 Commit 一次，隨時可以 Revert。

---

# 23. 資源與社群

### 官方文件
- **Documentation**: [antigravity.google/docs](https://antigravity.google/docs)

### 社群支援
- **Discord / Slack**: 官方通常會有使用者社群。
- **GitHub Issues**: 回報 Bug 的最佳管道。

### 教學文章
- **Medium**: 搜尋 "Google Antigravity Tutorial"。

---

# 24. 總結 (Summary)

今天我們完成了：

1.  成功安裝並啟動 Antigravity。
2.  完成了帳號驗證與環境設置。
3.  體驗了第一次的 Agent 協作 (Hello World)。
4.  了解如何連接 Google Cloud 進行部署。

**現在，你已經準備好用「未來的方式」寫程式了！**

---

# 25. Workshop 作業

### 請完成以下任務：
1.  安裝 Antigravity。
2.  建立一個新專案，包含一個 `index.html`。
3.  要求 Agent：*"幫我把背景改成深藍色，並在中間顯示 'Antigravity Start!' "*。
4.  截圖成果並上傳。

---

<!-- _class: lead -->
<!-- _paginate: false -->

# Thank You
## Any Questions?

### Horazon / Antigravity Lesson 04
