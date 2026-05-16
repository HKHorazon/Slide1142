---
name: check-skill
description: 當使用者提到 skill 名稱時，自動搜尋 .agent/skills 與 .agent/workflows，確認是否可執行並詢問是否執行。觸發詞：skill、技能、workflow、/any-skill-name。
---

# Check-Skill：自動查找並確認執行

當使用者提到任何 skill 名稱或 workflow 名稱時，執行以下流程。

## 觸發條件

以下任一情況觸發：
- 使用者輸入 `/skill-name`（例如 `/all-slides`、`/export-slide`）
- 使用者說「執行 xxx skill」、「用 xxx 技能」
- 使用者輸入的指令名稱與 `.agent/skills/` 或 `.agent/workflows/` 中的檔案名稱相符

## Step 1 — 解析目標名稱

從使用者輸入中提取 skill/workflow 名稱（去掉 `/`、`skill`、`workflow` 等關鍵字後的核心名稱）。

例如：`/all-slides true` → 目標名稱 = `all-slides`，參數 = `true`

## Step 2 — 搜尋對應檔案

**同時**搜尋兩個位置：

1. `.agent/skills/<name>/SKILL.md` — 技能
2. `.agent/workflows/<name>.md` — 工作流程

使用 Glob 或 Read 工具搜尋，**不要**用 Bash find。

## Step 3 — 確認可執行性

讀取找到的檔案，判斷其中是否含有**可執行指令**：

- **Workflow 檔案**：尋找形如 `python ...` 或 `// turbo` 標記的指令行。
- **Skill 檔案**：尋找 `Command:` 或 `python` 開頭的指令說明。

若找到可執行指令，提取完整指令（含使用者傳入的參數）。

## Step 4 — 向使用者確認

以下列格式告知使用者找到的結果，並**詢問是否執行**：

```
找到：[類型：Workflow / Skill] `<name>`
說明：<description 欄位或第一行說明>
指令：<完整指令，含參數>

要執行嗎？
```

使用 AskUserQuestion 工具詢問：
- 選項 1：「執行」
- 選項 2：「取消」

## Step 5 — 執行或取消

- 若使用者選擇**執行**：在專案根目錄執行提取到的指令，並回報結果。
- 若使用者選擇**取消**：結束，不執行任何指令。

## 找不到時的處理

若兩個位置都找不到對應名稱：

```
找不到名為 `<name>` 的 skill 或 workflow。

.agent/skills/ 中的可用技能：<列出所有資料夾名稱>
.agent/workflows/ 中的可用流程：<列出所有 .md 檔名>
```

## 重要規則

- **不要**未經確認就直接執行指令。
- **不要**修改任何檔案，本 skill 只負責查找與執行。
- Workflow 執行時，工作目錄必須是專案根目錄（`e:\弘光\課程\114.2`）。
- 若指令含有 `{{1}}` 之類的佔位符，以使用者傳入的參數取代。
