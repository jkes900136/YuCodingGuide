# WeChat 群發比較

  
 **客服群發**：對於48小時內互動過的粉絲實現無限制推送，不僅是每天多條，形式也不局限於微信圖文消息（經測試，當粉絲互動後，公眾號可連續回復20條消息，超出粉絲收不到。期間如粉絲再次互動，則條數重置。）。此接口從發送的條數和消息類型上都具有極高的自由度。

**模板群發**：認證服務號隨時能主動觸達粉絲的利器，通過多次調用模板消息API的形式實現對粉絲的群發。其特點是有固定的樣式及標題，點擊模板可設置跳轉指定的url，可主動推送給粉絲，也沒有像客服消息那樣的48小時限制，每個認證服務號的模板消息的日調用上限至少為10萬次。不過使用之前須要注意微信[模板消息運營規範](https://link.zhihu.com/?target=https%3A//mp.weixin.qq.com/wiki%3Ft%3Dresource/res_main%26id%3Dmp1433751288)的限制。

參考資料：

1.      公众平台服务号、订阅号、企业微信、小程序的相关说明, [https://kf.qq.com/faq/170815aUZjeQ170815mU7bI7.html](https://kf.qq.com/faq/170815aUZjeQ170815mU7bI7.html)

2.      微信的订阅号和服务号如何区分？, [https://www.zhihu.com/question/21289814](https://www.zhihu.com/question/21289814)

3.      小程序API, [https://developers.weixin.qq.com/miniprogram/dev/api/](https://developers.weixin.qq.com/miniprogram/dev/api/)





