# HttpClient Authorization æ¨™é ­?å ±?¼å??¯èª¤ä¹‹è§£æ±ºæ–¹å¼?

```csharp
 client.BaseAddress = new Uri(endpointURL);
    client.DefaultRequestHeaders.Accept.Clear();
    client.DefaultRequestHeaders.Accept.Add(
        new MediaTypeWithQualityHeaderValue("application/json"));
    client.DefaultRequestHeaders.Add("Authorization","hugyguygu===");

    HttpResponseMessage response = await client.GetAsync(uri);

    var responseJson = await response.Content.ReadAsStringAsync();
```

?¶ä¸­DefaultRequestHeaders.Add\("Authorization","?ˆæ??§å®¹"\)?„ç?å¼ç¢¼?è¨­?ƒæª¢?¥æ?æ¬Šå…§å®¹æ˜¯?¦ç‚ºBearer?‹é ­?„JWT

```csharp
client.DefaultRequestHeaders.Add("Authorization","hugyguygu===");
```

?¥æ ¼å¼éŒ¯èª¤æ??¢ç??·è??¯èª¤

ä¸é??¥å?Add?¹ç‚ºTryAddWithoutValidationï¼Œå°±?¯ä»¥?¿å??™å€‹ç?æ³?

```csharp
client.DefaultRequestHeaders.TryAddWithoutValidation("Authorization", "hugyguygu===");
```

