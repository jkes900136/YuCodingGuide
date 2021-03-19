# 解決Vue.js中文亂碼之問題

當網頁以UTF-8編碼未加上BOM \(Byte-Order Mark\)時，常常會出現亂碼

![](../.gitbook/assets/image%20%2817%29.png)

使用記事本開啟，可以發現右下角檔案編碼為UTF-8

![](../.gitbook/assets/image%20%2814%29.png)

![&#x4EE5;&#x6A94;&#x6848;-&amp;gt;&#x53E6;&#x5B58;&#x65B0;&#x6A94;&#x66F4;&#x6539;&#x6587;&#x5B57;&#x7DE8;&#x78BC;](../.gitbook/assets/image%20%2816%29.png)

![&#x5C07;&#x7DE8;&#x78BC;&#x6539;&#x70BA; UTF-8 with BOM ](../.gitbook/assets/image%20%2812%29.png)

![&#x6587;&#x5B57;&#x6062;&#x5FA9;&#x6B63;&#x5E38;](../.gitbook/assets/image%20%2813%29.png)

