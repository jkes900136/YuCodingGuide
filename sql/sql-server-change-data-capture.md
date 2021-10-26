# SQL Server Change Data Capture

SQL Server 從 2008 版本開始提供 Change Data Capture (CDC) 的功能，但只限於 Enterprise 和 Developer Edition 才提供。不過自 SQL Server 2016 開始這個好用的功能下放至 Standard Edition，為開發者帶來不少便利～

![](<../.gitbook/assets/image (18).png>)

要判斷CDC 是否開啟，可以查詢 sys.databases 資料庫內每一個資料庫名稱對應之 is\_cdc\_enabled 欄位的值，0表示未開啟，1代表開啟。

執行 sp\_cdc\_enable\_db 這隻預儲程序能開啟 CDC，反之 sp\_cdc\_disable\_db 可以關閉它。

```sql
EXEC sp_cdc_enable_db 
```

![SQL Server 提供 20 多個 CDC 相關的系統預儲程序](<../.gitbook/assets/image (19).png>)

![開啟 CDC 後可以在系統資料表底下看到一系列 cdc 開頭的資料表](<../.gitbook/assets/image (20).png>)

接著就要使用 sp\_cdc\_enable\_table 預儲程序設定要 CDC 紀錄的資料表

```sql
EXEC sp_cdc_enable_table
    @source_schema = 'dbo',
    @source_name = '/資料表名稱/',
    @role_name = 'cdc_admin'
```

![](<../.gitbook/assets/image (21).png>)

藉由\_$start\_lsn 欄位，能判斷是同一批次修改之交易(transaction)紀錄。

&#x20;\_$seqval 欄位值相同則表示同一筆修改產生的紀錄。

&#x20;\_$updatemask欄位原本是以十六進位儲存，像是 0x000800，轉二進位100000000000，由右向左數1 在第12位置，就代表第12個欄位有異動。

\_$operation 欄位數字有以下含義：

\_$operation = 1，代表資料被刪除

&#x20;\_$operation = 2，表示資料被新增

\_$operation = 3 及 4，3 為異動前的資料，4 則是異動後的資料

