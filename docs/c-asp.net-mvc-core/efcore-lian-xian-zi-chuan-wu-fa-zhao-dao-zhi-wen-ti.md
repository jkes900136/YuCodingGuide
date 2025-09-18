# EFCore 連線字串無法找到之問題

## 狀況

Named connection strings are only supported when using 'IConfiguration' and a service provide

## 解法

在Startup.cs新增AddDbContext函式

```text
 public void ConfigureServices(IServiceCollection services)
    {
        ........
        services.AddDbContext<StipContext>(options =>
            options.UseSqlServer(Configuration.GetConnectionString("NameOfYourConnectionStringParameter")));
    }
```

