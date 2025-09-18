# IANA 與 Windows 時區名稱之間互換

IANA是一家網際網路位址的分配機構，管理全球網際網路中使用的IP位址、域名和許多其它參數。此時區資訊資料庫由David Olson創立，目前資料庫由ICANN贊助、Paul Eggert進行維護。

IANA資料庫時區名稱是按「區域/位置」規則命名，例如「America/NewYork」。英文地名中的空格用底線「」代替，連詞符「-」只在英文地名本身包含時使用。

而Windows 則是以「相同時間計算方法」為名稱，即與UTC相同時差、日光節約時間的位置，都算在同一個時區。像是「Eastern Standard Time」對應到IANA 名稱會有「America/NewYork」、「America/Toronto」等。

在撰寫.NET 程式的時候，可以安裝以下套件轉換兩種不同的時區表示法：

```bash
PM> Install-Package TimeZoneConverter
```

IANA 轉  Windows 時區名稱：

```aspnet
using TimeZoneConverter;

string tz = TZConvert.IanaToWindows("America/New_York");
// Result:  "Eastern Standard Time"
```

Windows 轉 IANA 時區名稱：

```aspnet
using TimeZoneConverter;

string tz = TZConvert.WindowsToIana("Eastern Standard Time");
// result:  "America/New_York"
```

也可以標註國家、地區縮寫，以轉換成正確的IANA 時區名稱：

```aspnet
using TimeZoneConverter;

string tz = TZConvert.WindowsToIana("Eastern Standard Time", "CA");
// result:  "America/Toronto"
```

