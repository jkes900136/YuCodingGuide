# 在Vue.js內擷取網址查詢參數

當網頁開發者要以HTTP Get，取得即將載入頁面的特定資訊時，會在網址後方加上查詢參數(query parameters)。「?」後方會接著「Key=Value」一對值，並用「&」接續下去。

```
https://bootstrap-vue.org/docs?page=1&action=read
```

其實Vue跟Angular.js類似，可以在component中使用「$route.query」這個物件取得查詢參數：

```
console.log(this.$route.query.action) // 輸出「read」
```

參考資料：[https://router.vuejs.org/en/api/route-object.html](https://router.vuejs.org/en/api/route-object.html)
