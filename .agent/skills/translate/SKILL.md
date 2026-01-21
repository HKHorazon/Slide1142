---
name: translate
description: 專門負責中英翻譯的技能，包含主動偵測與指令觸發功能。
---

# 翻譯技能 (Translation Skill)

此技能旨在協助使用者快速將英文內容翻譯為流暢的**繁體中文 (台灣)**。

## 觸發規則 (Trigger Rules)

### 1. 顯式觸發 (Explicit Trigger)
-   **條件**: 當使用者的訊息以 **「翻譯」** (或 "Translate") 開頭，後接任何文字。
-   **動作**: 直接將該段文字翻譯成繁體中文。
-   **範例**:
    -   User: "翻譯 Artificial Intelligence is transforming the world."
    -   Agent: "人工智慧正在改變世界。"

### 2. 隱式觸發 (Implicit Trigger / Proactive Check)
-   **條件**: 當使用者貼上一段**長篇或完整的英文文字**，且該文字顯然**不是**給 AI 的指令 (Prompt) 時。
    -   *非指令特徵*: 純敘述性文章、新聞段落、程式錯誤訊息、文件內容。
    -   *指令特徵*: 包含 "Write code", "Explain", "Help me", "Fix this" 等動詞開頭的句子。
-   **動作**:
    -   **不要**直接翻譯。
    -   **詢問使用者**: "這段文字看起來像是參考資料，請問是否需要我將其翻譯成中文(繁體)？"
-   **範例**:
    -   User: (Pastes a paragraph about Quantum Computing)
    -   Agent: "收到關於量子運算的內容。請問是否需要將這段文字翻譯成中文？"

## 翻譯準則 (Translation Guidelines)

1.  **目標語言**: 
    -   **預設**: **繁體中文 (Traditional Chinese, Taiwan)**。
    -   **例外**: 若使用者明確指定其他語言 (如「翻譯成英文」)，則依指示翻譯。
2.  **語氣**: 
    -   預設為**專業、學術或商務**語氣，適合大學課程或專案報告。
    -   若原文為輕鬆對話，則調整為口語。
3.  **專有名詞**:
    -   保留關鍵的英文技術術語 (如: Unity, C#, Instance ID)，或採用台灣通用的譯名 (如: Project -> 專案, Interface -> 介面)。
