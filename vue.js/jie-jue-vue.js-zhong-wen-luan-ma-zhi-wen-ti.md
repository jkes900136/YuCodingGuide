# 解決Vue.js中文亂碼之問題

當網頁以UTF-8編碼未加上BOM (Byte-Order Mark)時，常常會出現亂碼

![](<../.gitbook/assets/image (12).png>)

使用記事本開啟，可以發現右下角檔案編碼為UTF-8

![](<../.gitbook/assets/image (14).png>)

![以檔案->另存新檔更改文字編碼](<../.gitbook/assets/image (15).png>)

![將編碼改為 UTF-8 with BOM ](<../.gitbook/assets/image (17).png>)

![文字恢復正常](<../.gitbook/assets/image (13).png>)
