# 從SQL資料庫儲存之HTML字串中擷取特定內容

## CHARINDEX

CHARINDEX\('f=','&lt;a href='\)為計算至「f」前（包含f）的字元數，所以執行以下查詢，結果會是7。：

```sql
SELECT CHARINDEX('f=','<a href=')
```

 假設要擷取「href」的話，可撰寫：

```sql
SELECT SUBSTRING('<a href=',CHARINDEX(' ','<a href=')+1,(CHARINDEX('=','<a href=')-1)-CHARINDEX(' ','<a href='))
```

由上面能類推，想從以下HTML字串中擷取網址（https://gitbook.com）：

```markup
<a target="_blank" href="https://gitbook.com">前往連結</a>
```

利用CHARINDEX尋找特殊字元是關鍵：

```sql
SUBSTRING([全文],CHARINDEX([特定字串前特殊字元]+[特殊字元數],[全文]),CHARINDEX(([特定字串後特殊字元]-[特殊字元數],[全文])-CHARINDEX([特定字串前特殊字元],[全文])
```

按照內容的不同，查詢語法會類似：

```sql
SELECT SUBSTRING([全文],CHARINDEX('f=',[全文])+3,(CHARINDEX('>前',[全文])-4)-CHARINDEX('f=',[全文]))
FROM [HTMLPageTable]
```



