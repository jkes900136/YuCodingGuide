# EFCore ???字串?��??�到之�?�?

## ?��?

Named connection strings are only supported when using 'IConfiguration' and a service provide

## �??

?�Startup.cs?��?AddDbContext?��?

```text
 public void ConfigureServices(IServiceCollection services)
    {
        ........
        services.AddDbContext<StipContext>(options =>
            options.UseSqlServer(Configuration.GetConnectionString("NameOfYourConnectionStringParameter")));
    }
```

