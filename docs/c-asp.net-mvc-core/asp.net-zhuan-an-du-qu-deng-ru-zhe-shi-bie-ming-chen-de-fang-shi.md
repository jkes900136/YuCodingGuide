# ASP.NET å°ˆæ?è®€?–ç™»?¥è€…è??¥å?ç¨±ç??¹å?

User.Identity.Name å®šç¾©??System.Web.HttpContext.Current.User ?„å??ƒå…§

å°‡ASP.NET å°ˆæ?è­˜åˆ¥?ç¨±å¯«å…¥?è¦½?¨Session ?„æ–¹å¼ï?

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

