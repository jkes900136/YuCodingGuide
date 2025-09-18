# HttpClient Authorization 標頭回報格式錯誤之解決方式

```csharp
 client.BaseAddress = new Uri(endpointURL);
    client.DefaultRequestHeaders.Accept.Clear();
    client.DefaultRequestHeaders.Accept.Add(
        new MediaTypeWithQualityHeaderValue("application/json"));
    client.DefaultRequestHeaders.Add("Authorization","hugyguygu===");

    HttpResponseMessage response = await client.GetAsync(uri);

    var responseJson = await response.Content.ReadAsStringAsync();
```

其中DefaultRequestHeaders.Add\("Authorization","授權內容"\)的程式碼預設會檢查授權內容是否為Bearer開頭的JWT

```csharp
client.DefaultRequestHeaders.Add("Authorization","hugyguygu===");
```

若格式錯誤會產生執行錯誤

不過若將Add改為TryAddWithoutValidation，就可以避免這個狀況

```csharp
client.DefaultRequestHeaders.TryAddWithoutValidation("Authorization", "hugyguygu===");
```

