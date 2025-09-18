# è§?±ºASP.NET Self referencing loop detected ?é?

&#x20;1\. ç§»é™¤ Entity Framework æ¨¡å?ä¸å?è¦ç??œè¯?§ã€?

2\. ??Entity Framework ?¢ç???Classæª”æ??§ï??¼ç‰¹å®šå±¬?§ä??¹å???\[JsonIgnore] å±¬æ€?

&#x20;3\. ä½¿ç”¨ Partial Class ??MetadataType ?´å??å??¢ç?Classä¹‹å±¬??

&#x20;4\. ??Global.asax.cs ä¸­ç? Application\_Start()  function ?§å??¥ï?

```
GlobalConfiguration.Configuration.Formatters.JsonFormatter.SerializerSettings.ReferenceLoopHandling = Newtonsoft.Json.ReferenceLoopHandling.Ignore;
```

[https://blog.miniasp.com/post/2012/12/24/ASPNET-Web-API-Self-referencing-loop-detected-for-property-solutions](https://blog.miniasp.com/post/2012/12/24/ASPNET-Web-API-Self-referencing-loop-detected-for-property-solutions)
