# ?��?ASP.NET Core 3.1??.0

1.將\*.csproj檔�??�目標�??��??�改?�net5.0

```
<Project Sdk="Microsoft.NET.Sdk.Web">

  <PropertyGroup>
-    <TargetFramework>netcoreapp3.1</TargetFramework>
+    <TargetFramework>net5.0</TargetFramework>
  </PropertyGroup>

</Project>
```

2.?�Visual Studio?�單之工??Tools)->NuGet 套件管�???Package Manager)->管�??��?之NuGet套件(Manage NuGet Packages for Solution)

?��???\_**?�新(Updates)**\_?�籤，勾?��?件並點選 _**?�新**_ (Update)?��?

![使用NuGet將�?件都?��??�v5.0.0](<assets/image (2).png>)

[https://docs.microsoft.com/zh-tw/aspnet/core/migration/31-to-50?view=aspnetcore-5.0\&tabs=visual-studio#update-net-core-sdk-version-in-globaljson](https://docs.microsoft.com/zh-tw/aspnet/core/migration/31-to-50?view=aspnetcore-5.0\&tabs=visual-studio#update-net-core-sdk-version-in-globaljson)

[https://docs.microsoft.com/zh-tw/dotnet/core/compatibility/3.1-5.0](https://docs.microsoft.com/zh-tw/dotnet/core/compatibility/3.1-5.0)
