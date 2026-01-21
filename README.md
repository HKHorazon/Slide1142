# 這是個人的教學投影片專案

## 關於此專案

此專案用於管理和匯出教學投影片，使用 Marp 框架製作 Markdown 格式的投影片。

## 使用方式

### 安裝依賴

```bash
pip install -r requirements.txt
```

### 匯出投影片

使用 `export.py` 腳本將 MD 目錄中的 Markdown 文件匯出為 PDF：

```bash
python export.py
```

## 專案結構

- `MD/` - Markdown 格式的投影片源文件
- `PDF/` - 匯出的 PDF 投影片
- `IMAGE/` - 投影片中使用的圖片
- `HoraStyle.css` - 自定義 Marp 主題樣式
- `export.py` - 投影片匯出腳本

## 貢獻

如需貢獻，請 fork 此專案並提交 pull request 至 `main` 分支。
