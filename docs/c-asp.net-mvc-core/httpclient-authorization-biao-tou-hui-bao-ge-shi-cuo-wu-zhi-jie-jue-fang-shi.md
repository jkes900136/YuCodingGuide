# HttpClient Authorization 標頭?�報?��??�誤之解決方�?

```csharp
 client.BaseAddress = new Uri(endpointURL);
    client.DefaultRequestHeaders.Accept.Clear();
    client.DefaultRequestHeaders.Accept.Add(
        new MediaTypeWithQualityHeaderValue("application/json"));
    client.DefaultRequestHeaders.Add("Authorization","hugyguygu===");

    HttpResponseMessage response = await client.GetAsync(uri);

    var responseJson = await response.Content.ReadAsStringAsync();
```

?�中DefaultRequestHeaders.Add\("Authorization","?��??�容"\)?��?式碼?�設?�檢?��?權內容是?�為Bearer?�頭?�JWT

```csharp
client.DefaultRequestHeaders.Add("Authorization","hugyguygu===");
```

?�格式錯誤�??��??��??�誤

不�??��?Add?�為TryAddWithoutValidation，就?�以?��??�個�?�?

```csharp
client.DefaultRequestHeaders.TryAddWithoutValidation("Authorization", "hugyguygu===");
```

