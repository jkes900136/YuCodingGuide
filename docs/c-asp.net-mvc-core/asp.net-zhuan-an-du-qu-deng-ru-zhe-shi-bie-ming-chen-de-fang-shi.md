# ASP.NET 專案讀取登入者識別名稱的方式

User.Identity.Name 定義於 System.Web.HttpContext.Current.User 的參考內

將ASP.NET 專案識別名稱寫入瀏覽器Session 的方式：

```aspnet
public static int GetUserId(this HttpContextBase context)
        {

            var userid = context.Session["userid"] as int?;

            if (userid == default)
            {
               
                userid = SetUserId(context.Session, context.User.Identity.Name);

            }

            return (int)userid;
        }
```

