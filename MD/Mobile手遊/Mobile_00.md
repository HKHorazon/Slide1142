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
<!--_paginate: false-->

### Mobile Game Development
# 手機遊戲程式設計

## 114學年度第2學期
## 課程地圖與教學大綱

---

# 課程核心目標

本課程目標為帶領同學**從零開始**，製作出一款完整的 **2D 橫向捲軸手機遊戲**。

我們將課程分為三個階段：
1.  **Level Designer (關卡設計)**：不寫程式，使用現成工具體驗遊戲開發。
2.  **Gameplay Programmer (遊戲程式)**：學習 C# 核心，撰寫角色與邏輯。
3.  **Mobile Optimizer (手機優化)**：UI、觸控操作與上架發布。

---

# Phase 1：關卡設計師 (Level Design)
<mark>目標：熟悉 Unity 編輯器與物理系統，產出可玩的關卡原型。</mark>

-   **Ch 01**: 手機遊戲開發概論 (iOS/Android 平台差異)
-   **Ch 02**: 專案建置與預製物 (Asset Store, Prefabs)
-   **Ch 03**: 地圖繪製 (Tilemap, Palette, Sorting Layer)
-   **Ch 04**: 物理與碰撞 (Rigidbody 2D, Collider 2D, Material)
-   **Ch 05**: 互動與邏輯 (Trigger, 預製機關應用)

> 🟢 **Milestone 1**: 完成一個使用現成素材搭建的遊戲關卡。

---

# Phase 2：遊戲程式設計師 (Programming)
<mark>目標：捨棄預製腳本，親手撰寫 C# 代碼控制遊戲。</mark>

-   **Ch 06**: C# 程式基礎入門 (Variable, Function, Start/Update)
-   **Ch 07**: 角色移動原理 (Input.GetAxis, Transform.Translate)
-   **Ch 08**: 跳躍與地面檢測 (AddForce, IsGrounded, Raycast)
-   **Ch 09**: 角色動畫系統 (Animator, Finite State Machine)
-   **Ch 10**: 遊戲管理與核心邏輯 (Singleton, OnTriggerEnter, Score)
    -   *與 Ch05 差異：Ch05 用現成黑盒子，Ch10 要自己寫出邏輯。*

> 🔵 **Milestone 2**: 角色可以跑跳、吃金幣、殺怪，且有分數計算。

---

# Phase 3：手機優化與發布 (Mobile & Publish)
<mark>目標：將電腦遊戲轉化為真正的手機 App。</mark>

-   **Ch 11**: UI 介面設計 (UGUI, Canvas, Anchor)
-   **Ch 12**: 遊戲體感優化 (AudioMixer, Particle System, Cinemachine)
-   **Ch 13**: 手機觸控操作 (OnScreen Controls, CrossPlatformInput)
-   **Ch 14**: 專案建置與發布 (Build Settings, Keystore, APK)

> 🟠 **Milestone 3**: 在自己的手機上執行遊戲。

---

# 課堂規約

-   **出席率**：雖然我不愛點名，但太久沒來會跟不上進度。
-   **作業繳交**：程式作業**嚴禁抄襲**。
    -   可以參考同學的邏輯，但請自己打一遍。
    -   Code 是騙不了人的。
-   **上課設備**：請愛惜電腦教室設備，離開時請登出並關機。
-   **手機使用**：上課可以滑手機，但請將聲音關閉，不要影響他人。
    -   (但在 Ch13 測試手機版時，請用力滑)

---

# 評分標準

-   **平時成績 (30%)**：
    -   課堂小練習、出席狀況。
-   **期中作業 (30%)**：
    -   Phase 1 + Phase 2 前半段成果。
    -   繳交一個 Unity 專案檔。
-   **期末專案 (40%)**：
    -   完整的手機遊戲 APK 安裝檔。
    -   需包含完整的關卡流程 (標題->遊戲->結算)。

---

# 關於使用的素材

本課程將使用 **Pixel Art (像素風格)** 的素材包。

-   **Sunny Land** (經典練習專案)
-   **Free Platform Game Assets**
-   (若同學有自己喜歡的素材，經老師確認規格後可使用)

<br>

**準備好了嗎？讓我們開始這學期的冒險吧！**
