# Yu's Coding Guide

這是一個使用 MkDocs 建立的技術文件網站，包含各種程式設計相關的指南和解決方案。

## 本地開發

### 安裝依賴

```bash
pip install -r requirements.txt
```

### 本地預覽

```bash
mkdocs serve
```

訪問 http://localhost:8000 來預覽網站。

### 建置網站

```bash
mkdocs build
```

產生的靜態文件會放在 `site/` 目錄下。

## 部署

### GitHub Pages

```bash
mkdocs gh-deploy
```

### 其他平台

執行 `mkdocs build` 後，將 `site/` 目錄下的文件部署到您的網站伺服器。

## 內容結構

- `docs/` - 文件來源
- `mkdocs.yml` - MkDocs 配置文件
- `requirements.txt` - Python 依賴套件

## 技術文件分類

- **Instant Messaging** - 即時通訊 API 相關
- **Javascript/Node.js** - JavaScript 和 Node.js 開發
- **Angular** - Angular 框架相關
- **Vue.js** - Vue.js 框架相關
- **C#/ASP.NET** - .NET 開發相關
- **SQL** - 資料庫相關
- **其他** - 各種系統管理和工具使用指南