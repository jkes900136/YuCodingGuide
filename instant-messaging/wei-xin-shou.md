# 微信網頁授權

[https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140842&t=0.4622491167403\#0](https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140842&t=0.4622491167403%230)

一、 前置作業

1、在微信公眾號請求用戶網頁授權之前，開發者需要先到公眾平臺官網中的“開發 - 接口權限 - 網頁服務 - 網頁帳號 - 網頁授權獲取用戶基本信息”的配置選項中，修改授權回調域名。請注意，這裡填寫的是域名（是一個字符串），而不是URL，因此請勿加 http:// 等協議頭；

2、授權回調域名配置規範為全域名，比如需要網頁授權的域名為：www.qq.com，配置以後此域名下面的頁面[http://www.qq.com/music.html](http://www.qq.com/music.html) 、 [http://www.qq.com/login.html](http://www.qq.com/login.html) 都可以進行OAuth2.0鑒權。但[http://pay.qq.com](http://pay.qq.com) 、 [http://music.qq.com](http://music.qq.com) 、 [http://qq.com無法進行OAuth2.0鑒權](http://qq.com無法進行OAuth2.0鑒權)

![](../.gitbook/assets/wechatoauth.png)

圖一

對於以snsapi\_base為scope的網頁授權，就靜默授權的，用戶無感知；

二、 具體而言，網頁授權snsapi\_base流程分為三步：

1、引導用戶進入授權頁面，以獲取code

redirect\_uri 可以使用[https://meyerweb.com/eric/tools/dencoder/](https://meyerweb.com/eric/tools/dencoder/) 進行編碼

範例：

[https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx94d45a495b558000&redirect\_uri=https%3A%2F%2Flife-academy-ca18f.firebaseapp.com&response\_type=code&scope=snsapi\_base&state=STATE\#wechat\_redirect](https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx94d45a495b558000&redirect_uri=https%3A%2F%2Flife-academy-ca18f.firebaseapp.com&response_type=code&scope=snsapi_base&state=STATE#wechat_redirect)

尤其注意：跳轉回調redirect\_uri，應當使用https鏈接來確保授權code的安全性。

參數說明

| **參數** | **是否必須** | **說明** |  |
| :--- | :--- | :--- | :--- |
| appid | 是 | 公眾號的唯一標識 |  |
| redirect\_uri | 是 | 授權後重定向的回調鏈接地址， 請使用 urlEncode 對鏈接進行處理 |  |
| scope | 是 | 應用授權作用域，snsapi\_base （不彈出授權頁面，直接跳轉，只能獲取用戶openid），snsapi\_userinfo （彈出授權頁面，可通過openid拿到昵稱、性別、所在地。並且， 即使在未關注的情況下，只要用戶授權，也能獲取其信息 ） |  |
| state | 否 | 重定向後會帶上state參數，開發者可以填寫a-zA-Z0-9的參數值，最多128字節 |  |
|  |  |  |  |

用戶在微信開啟上方連結後

如果用戶同意授權，頁面將跳轉至 redirect\_uri/?code=0215P6z10OzbBE1GcyC10ivcz105P6zG &state=STATE。

CODE說明 ： code作為換取access\_token的票據，每次用戶授權帶上的code將不一樣，code只能使用一次，5分鐘未被使用自動過期。

STATE說明：重定向後會帶上state參數，開發者可以填寫a-zA-Z0-9的參數值，最多128字節

2、通過code換取網頁授權access\_token（與基礎支持中的access\_token不同）

首先請注意，這裡通過code換取的是一個特殊的網頁授權access\_token,與基礎支持中的access\_token（該access\_token用於調用其他接口）不同。公眾號可通過下述接口來獲取網頁授權access\_token。當網頁授權的作用域為snsapi\_base時，則本步驟中獲取到網頁授權access\_token的同時，也獲取到了openid，snsapi\_base式的網頁授權流程即到此為止。

獲取code後，請求以下鏈接獲取access\_token： [https://api.weixin.qq.com/sns/oauth2/access\_token?appid=wx94d45a495b558000&secret=2d982455b25f2be4c92e4ba2de2800g3&code=0215P6z10OzbBE1GcyC10ivcz105P6zG&grant\_type=authorization\_code](https://api.weixin.qq.com/sns/oauth2/access_token?appid=wx94d45a495b558000&secret=2d982455b25f2be4c92e4ba2de2800g3&code=0215P6z10OzbBE1GcyC10ivcz105P6zG&grant_type=authorization_code)

參數說明

| **參數** | **是否必須** | **說明** |
| :--- | :--- | :--- |
| appid | 是 | 公眾號的唯一標識 |
| secret | 是 | 公眾號的appsecret |
| code | 是 | 填寫第一步獲取的code參數 |

返回說明

正確時返回的JSON數據包如下：

{"access\_token":"11\_jhA9cRwh951E5u7PStNzG5QnSO025D5oQPOW4lLPYTHunmgKRam6QPHH5XKg2IPLyhSUqKURmJ9DGS2SlIUIIFLWRMk\_LV0jYp-GFDHGNi0",

"expires\_in":7200,

"refresh\_token":"11\_ajetRUV6GJPJsli\_II9gzJBGRe8W0QtJnw85fdniWK0l2dEd\_zbV245W34MiyOciCUiDBVpjdWeDPtFDBHPKKiYqrGo1jzfOuQYetZXa9Qo",

"openid":"ov3qV1fHPnVuEihyiKTVODNofGF4",

"scope":"snsapi\_base"}

| **參數** | **描述** |
| :--- | :--- |
| access\_token | 網頁授權接口調用憑證,注意：此access\_token與基礎支持的access\_token不同 |
| expires\_in | access\_token接口調用憑證超時時間，單位（秒） |
| refresh\_token | 用戶刷新access\_token |
| openid | 用戶唯一標識，請注意，在未關注公眾號時，用戶訪問公眾號的網頁，也會產生一個用戶和公眾號唯一的OpenID |

3、如果需要，開發者可以刷新網頁授權access\_token，避免過期

由於access\_token擁有較短的有效期，當access\_token超時後，可以使用refresh\_token進行刷新，refresh\_token有效期為30天，當refresh\_token失效之後，需要用戶重新授權。

**請求方法**

獲取第二步的refresh\_token後，請求以下鏈接獲取access\_token：  
[https://api.weixin.qq.com/sns/oauth2/refresh\_token?appid=wx94d45a495b558000&grant\_type=refresh\_token&refresh\_token=11\_ajetRUV6GJPJsli\_II9gzJBGRe8W0QtJnw85fdniWK0l2dEd\_zbV245W34MiyOciCUiDBVpjdWeDPtFDBHPKKiYqrGo1jzfOuQYetZXa9Qo](https://api.weixin.qq.com/sns/oauth2/refresh_token?appid=wx94d45a495b558000&grant_type=refresh_token&refresh_token=11_ajetRUV6GJPJsli_II9gzJBGRe8W0QtJnw85fdniWK0l2dEd_zbV245W34MiyOciCUiDBVpjdWeDPtFDBHPKKiYqrGo1jzfOuQYetZXa9Qo)

| **參數** | **是否必須** | **說明** |
| :--- | :--- | :--- |
| appid | 是 | 公眾號的唯一標識 |
| refresh\_token | 是 | 填寫通過access\_token獲取到的refresh\_token參數 |

返回說明

正確時返回的JSON數據包如下：

{"openid":"ov3qV1fHPnVuEihyiKTVODNofGF4",

"access\_token":"11\_jhA9cRwh951E5u7PStNzG5QnSO025D5oQPOW4lLPYTHunmgKRam6QPHH5XKg2IPLyhSUqKURmJ9DGS2SlIUIIFLWRMk\_LV0jYp-GFDHGNi0",

"expires\_in":7200,

"refresh\_token":"11\_ajetRUV6GJPJsli\_II9gzJBGRe8W0QtJnw85fdniWK0l2dEd\_zbV245W34MiyOciCUiDBVpjdWeDPtFDBHPKKiYqrGo1jzfOuQYetZXa9Qo",

"scope":"snsapi\_base,"}

