# ASP.NET 專�?讀?�登?�者�??��?稱�??��?

User.Identity.Name 定義??System.Web.HttpContext.Current.User ?��??�內

將ASP.NET 專�?識別?�稱寫入?�覽?�Session ?�方式�?

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

