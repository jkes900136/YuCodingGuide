# 解決ASP.NET Self referencing loop detected 問題

 1. 移除 Entity Framework 模型不必要的關聯性。

2. 在 Entity Framework 產生的 Class檔案內，於特定屬性上方加入 \[JsonIgnore\] 屬性

 3. 使用 Partial Class 和 MetadataType 擴充預先產生Class之屬性

 4. 在 Global.asax.cs 中的 Application\_Start\(\)  function 內加入：

```text
GlobalConfiguration.Configuration.Formatters.JsonFormatter.SerializerSettings.ReferenceLoopHandling = Newtonsoft.Json.ReferenceLoopHandling.Ignore;
```

[https://blog.miniasp.com/post/2012/12/24/ASPNET-Web-API-Self-referencing-loop-detected-for-property-solutions](https://blog.miniasp.com/post/2012/12/24/ASPNET-Web-API-Self-referencing-loop-detected-for-property-solutions)

