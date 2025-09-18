# EFCore ???å­—ä¸²?¡æ??¾åˆ°ä¹‹å?é¡?

## ?€æ³?

Named connection strings are only supported when using 'IConfiguration' and a service provide

## è§??

?¨Startup.cs?°å?AddDbContext?½å?

```text
 public void ConfigureServices(IServiceCollection services)
    {
        ........
        services.AddDbContext<StipContext>(options =>
            options.UseSqlServer(Configuration.GetConnectionString("NameOfYourConnectionStringParameter")));
    }
```

