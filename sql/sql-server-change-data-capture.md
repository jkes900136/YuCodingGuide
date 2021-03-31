# SQL Server Change Data Capture

SQL Server 從 2008 版本開始提供 Change Data Capture \(CDC\) 的功能，但只限於 Enterprise 和 Developer Edition 才提供。不過自 SQL Server 2016 開始這個好用的功能下放至 Standard Edition，為開發者帶來不少便利～

![](../.gitbook/assets/image%20%2820%29.png)

要判斷CDC 是否開啟，可以查詢 sys.databases 資料庫內每一個資料庫名稱對應之 is\_cdc\_enabled 欄位的值，0表示未開啟，1代表開啟。

執行 sp\_cdc\_enable\_db 這隻預儲程序能開啟 CDC，反之 sp\_cdc\_disable\_db 可以關閉它。

```sql
EXEC sp_cdc_enable_db 
```

![SQL Server &#x63D0;&#x4F9B; 20 &#x591A;&#x500B; CDC &#x76F8;&#x95DC;&#x7684;&#x7CFB;&#x7D71;&#x9810;&#x5132;&#x7A0B;&#x5E8F;](../.gitbook/assets/image%20%2819%29.png)

![&#x958B;&#x555F; CDC &#x5F8C;&#x53EF;&#x4EE5;&#x5728;&#x7CFB;&#x7D71;&#x8CC7;&#x6599;&#x8868;&#x5E95;&#x4E0B;&#x770B;&#x5230;&#x4E00;&#x7CFB;&#x5217; cdc &#x958B;&#x982D;&#x7684;&#x8CC7;&#x6599;&#x8868;](../.gitbook/assets/image%20%2818%29.png)

接著就要使用 sp\_cdc\_enable\_table 預儲程序設定要 CDC 紀錄的資料表

```sql
EXEC sp_cdc_enable_table
    @source_schema = 'dbo',
    @source_name = '/資料表名稱/',
    @role_name = 'cdc_admin'
```

![](../.gitbook/assets/image%20%2821%29.png)

藉由\_$start\_lsn 欄位，能判斷是同一批次修改之交易\(transaction\)紀錄。

 \_$seqval 欄位值相同則表示同一筆修改產生的紀錄。

 \_$updatemask欄位原本是以十六進位儲存，像是 0x000800，轉二進位100000000000，由右向左數1 在第12位置，就代表第12個欄位有異動。

\_$operation 欄位數字有以下含義：

\_$operation = 1，代表資料被刪除

 \_$operation = 2，表示資料被新增

\_$operation = 3 及 4，3 為異動前的資料，4 則是異動後的資料



