---
name: slide-image-arrange
description: 用來為 md 檔案中包含單張或多張圖片且沒有 <style scoped> 排版標籤的投影片，自動插入最不干擾上方文字、不會互相重疊的絕對位置版型 CSS 設計。
---

# slide-image-arrange 技能

此技能會自動掃描指定的 Markdown 檔案或是目錄下所有 MD 檔案。
它會逐張解析被 `---` 切割的投影片，如果發現投影片中含有一般圖片，但缺乏專用的獨立排版樣式（`<style scoped>`），就會自動產生。

## 功能重點設計
1. **動態閃避上方文字與標題**：系統會估算文字區塊行數，自動算出合適的 `top` 位置基準點，預留足夠的空間給標題或清單，優先避免圖片遮蓋字體。
2. **多圖片網格佈局防重疊**：
   - 1 張圖：單一大圖橫跨，左右等距內縮放置。
   - 2 張圖：左右各一半對稱排開。
   - 3 張圖：自動切割為左、中、右三個寬度版型設定。
   - 4 張以上：自動切換為上半、下半 2xN 網格模式，保證所有圖片都有明確的空間不交叉。
3. **智慧排除**：會精確閃掉由 Marp 宣告的背景圖片（如 `![bg right]()`），以防破壞原本就具備版型的特殊宣告頁面。

## 觸發方式
當使用者提到「自動排版圖片」、「加入 style scoped」或是輸入指令 `/slide-image-arrange` 時即可使用。

## 使用方式
使用 `run_command` 來執行底下的 Python 腳本即可為指定範圍追加自動排版的 CSS：

```bash
python .agent/skills/slide-image-arrange/scripts/slide_image_arrange.py <target_path>
```

支援的形式有三種：
- **單一檔案執行**：
  ```bash
  python .agent/skills/slide-image-arrange/scripts/slide_image_arrange.py "e:\弘光\課程\114.2\MD\Special\Japan2026.md"
  ```
- **處理單一資料夾（及其子資料夾）下的 .md 檔**：
  ```bash
  python .agent/skills/slide-image-arrange/scripts/slide_image_arrange.py "e:\弘光\課程\114.2\MD\Special"
  ```
- **全部套用 (批次更新整個專案)**：
  ```bash
  python .agent/skills/slide-image-arrange/scripts/slide_image_arrange.py all
  ```
