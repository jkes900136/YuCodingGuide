# 解決Vue.js中文亂碼之問題

當網頁以UTF-8編碼未加上BOM (Byte-Order Mark)時，常常會出現亂碼

![](../assets/image (17).png)

使用記事本開啟，可以發現右下角檔案編碼為UTF-8

![](../assets/image (14).png)

![以檔案->另存新檔更改文字編碼](../assets/image (16).png)

![將編碼改為 UTF-8 with BOM ](../assets/image (12).png)

![文字恢復正常](../assets/image (13).png)
