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

### Midterm  Homework

# 期中作業
## 期中作業


---

# 繳交方式說明

### 請繳交一個 **專案壓縮檔**

- 遵照之前帶出專案的方式，將以下壓縮打包給我
    -   assets
    -   packages
    -   ProjectSettings
    -   其他在資料夾外的檔案

> 如果打包正確，檔案大小約在 5 ~ 10 MB
> 繳交期限請參考課程系統。逾期作業分數乘以 **80%**。


---

# 作業說明

使用老師提供的 GitHub 專案作為起點，完成以下地圖設計：

### 需求
1.   刪除我原有的地板
2.   使用 **Tilemap** 建構地形
3.   利用prefab，額外建立至少包含 **3 個以上的平台**。
4.   場景中放置 **至少 5 枚 金幣或地刺**（須製作成 Prefab）。
5.  簡易攝影機跟隨


---

# 題目4：金幣或地刺

1. 製作 金幣 & 地刺 的 prefab
2. 玩家碰觸到這兩種東西時，必須顯示不一樣的訊息
    - 玩家碰觸到金幣時，必須要獲得金幣 (金幣消失)
    - 玩家碰觸地刺時，地刺不能消失

---

# 題目5：簡易攝影機跟隨

-   請將攝影機拖曳到玩家身上，形成**子物件**
    - 調整攝影機位置
    - 此時玩家移動時，應該可以看到玩家會保持在畫面中心

-   如果你已經熟悉進階攝影機(Cinemachine)操作，也可以使用

--- 
# 額外補充

### 調整 TileMap、平台的 Layer 為 Ground
- 這個部分尚未正式說明，但為了讓大家的場景可以玩(跳躍)，所以請依照此方式修改 
- 我們等到人物操作時再說明
    

---

<style scoped>
  table {
    font-size: 25px;
  }
  th {
    font-size: 35px;
  }
  th, td {
    padding: 20px;
    text-align: left;
  }
  /* 每欄寬度設定 */
  th:nth-child(1), td:nth-child(1) { width: 20%; } /* 項目 */
  th:nth-child(2), td:nth-child(2) { width: 15%; } /* 配分 */
  th:nth-child(3), td:nth-child(3) { width: 60%; } /* 說明 */
</style>

# 評分標準

| 項目 | 配分 | 說明 |
| :--- | :---: | :--- |
| Tilemap | 40 分 | Tilemap相關設定正確 |
| 金幣與地刺 | 30 分 | 建立prefab與訊息正確 |
| 其他平台 | 10 分 | 放置其他平台 |
| 簡易攝影機跟隨 | 10 分 | 讓攝影機跟隨玩家(簡易版) |
| 關卡設計 | 20 分 | 其他關卡設計 |