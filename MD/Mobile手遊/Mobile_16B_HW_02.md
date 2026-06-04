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

### Homework 02

# 平台動作遊戲進階作業
## Horazon
## 手機程式設計


---

# 繳交方式說明

### 請繳交一個 **專案壓縮檔**

- 遵照之前帶出專案的方式，將以下壓縮打包給我
    -   assets
    -   packages
    -   ProjectSettings
    -   其他在資料夾外的檔案

> 如果打包正確，檔案大小約在 5 ~ 10 MB
> 打包錯誤(如1GB大小)，計算完總分後酌量扣分


---

# 作業項目總覽

1. CineMachine
2. 視差背景
3. 人物左右翻轉
4. 修改人物重力 (約 3~5 倍)
5. 跳躍力量調整
6. 降低平台摩擦力
7. 動畫 (idle / run / jump)
8. 可操作的按鈕 (虛擬 D-pad)


---

<style scoped>
  table {
    font-size: 20px
  }
  th {
    font-size: 20px;
  }
  th, td {
    padding: 12px;
    text-align: left;
  }
  th:nth-child(1), td:nth-child(1) { width: 50px; }
  th:nth-child(2), td:nth-child(2) { width: 320px; }
  th:nth-child(3), td:nth-child(3) { width: 50px; }
  th:nth-child(4), td:nth-child(4) { width: 500px; }
  th:nth-child(5), td:nth-child(5) { width: 110px; }
</style>

# 評分標準

| 序號 | 項目 | 章節 | 說明 | 配分 |
| :---: | :--- | :---: | :--- | :---: |
| 1 | CineMachine | Ch.07 | 攝影機正確跟隨玩家 | 20 分 |
| 2 | 視差背景 | Ch.08 | 多層背景產生景深 | 20 分 |
| 3 | 人物左右翻轉 | Ch.10 | 朝向與移動方向一致 | 10 分 |
| 4 | 人物重力 (3~5 倍) | Ch.11 | Gravity Scale 調整 | 5 分 |
| 5 | 跳躍力量調整 | Ch.11 | 跳躍手感合理 | 5 分 |
| 6 | 降低平台摩擦力 | Ch.09 | 平台 Physics Material 設定 | 10 分 |
| 7 | 動畫 (idle/run/jump) | Ch.12 | 三組動畫與狀態切換 | 30 分 |
| 8 | 虛擬 D-pad | Ch.14 | 觸控按鈕驅動玩家 | 20 分 |
| |  | | **總計** | **120 分** |
