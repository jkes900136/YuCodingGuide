# �?��ASP.NET Self referencing loop detected ?��?

&#x20;1\. 移除 Entity Framework 模�?不�?要�??�聯?��?

2\. ??Entity Framework ?��???Class檔�??��??�特定屬?��??��???\[JsonIgnore] 屬�?

&#x20;3\. 使用 Partial Class ??MetadataType ?��??��??��?Class之屬??

&#x20;4\. ??Global.asax.cs 中�? Application\_Start()  function ?��??��?

```
GlobalConfiguration.Configuration.Formatters.JsonFormatter.SerializerSettings.ReferenceLoopHandling = Newtonsoft.Json.ReferenceLoopHandling.Ignore;
```

[https://blog.miniasp.com/post/2012/12/24/ASPNET-Web-API-Self-referencing-loop-detected-for-property-solutions](https://blog.miniasp.com/post/2012/12/24/ASPNET-Web-API-Self-referencing-loop-detected-for-property-solutions)
