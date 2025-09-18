# Line?�WeChat?��?轉�?

\
**一??   Line?�WeChat訊息?��?比�?**

**1.     ?�單?��?**

LINE?��??�單 \[1]

步�?一：登?�LINE@?�腦?��???

步�?二�?建�??��?影音?�容 > ?��??�單 > 建�??��???

?��??��??�以?��?製�??�樣?��??�接上傳一張�??��?並選?�想要�??��??��??�單?��?，可?��???\~6?��??�本（注?��?欲�??��??��?必�??��??�設計�?，就?�好?��?，符?�欲?�現?�格式�??�直?��??�整張�?�?

?�照?�面上�??�示，�??�選?��?�?��，填寫�??�選?��?塊�?觸發?��?�?action)?�內容�??�次?��?案設�??��?塊在點選後都?��??��?字」�?

![](assets/lineimgmap.png)

??一：Line 7種�??��??��??��??�選??

WeChat?��?義�???\[2]

1?�自定義?�單?�多�????��?級�??��?每個�?級�??��?多�????��?級�??��?

2?��?級�??��?�??�漢字�?二�??�單?��??�漢字�?多出來�??��?將�?以�?..?�代?��?

3?�創建自定義?�單後�??�單?�刷?��??�是，在?�戶?�入?�眾?��?話�??�公?��?profile?��?，�??�發?��?一次�??��??��?請�????��?以�?，就?��??��?下�??��?如�??�單?�更?��?就�??�新客戶端�??�單?�測試�??�以?�試?��??�注?�眾賬�?後�?次�?注�??�可以�??�創建�??��??��?

**?�於WeChat?�單?��??��?Line?��??�單?��?塊數如�????�話，�??��?2?��?級�??�。�??�單?�能以�?字�?形�??�現，�??�webhook** **?�能以click事件?��?觸發（�??�在Line點選?��??�單，使?�者�??�到?�己?�出?��?）�?*

?��?義�??�接?�click事件�?

點�??��?件用?��??�click類�??��?後�?微信?��??��??��?消息?�口?�送�??��??�為event?��??�給?�發?��??�考�??�接????��?，並且帶上�??�中?�發?�填寫�?key?��??�發?�可以通�??��?義�?key?��??�戶?��?交�?

{

&#x20;   "button": \[

&#x20;       {

&#x20;           "name": "?�入?��?",

&#x20;           "sub\_button": \[

&#x20;               {

&#x20;                   "type": "click",

&#x20;                   "name": "?�司資�?",

&#x20;                   "key": "introduction"

&#x20;               },

&#x20;               {

&#x20;                   "type": "click",

&#x20;                   "name": "保險?�司",

&#x20;                   "key": "company"

&#x20;               },

&#x20;               {

&#x20;                   "type": "click",

&#x20;                   "name": "主�??��?",

&#x20;                   "key": "product"

&#x20;               }

&#x20;           ]

&#x20;       },

&#x20;       {

&#x20;           "name": "幸�?滿�?",

&#x20;           "sub\_button": \[

&#x20;               {

&#x20;                   "type": "click",

&#x20;                   "name": "?�人績�?",

&#x20;                   "key": "performance"

&#x20;               },

&#x20;               {

&#x20;                   "type": "click",

&#x20;                   "name": "?��?行政",

&#x20;                   "key": "administrative"

&#x20;               },

&#x20;               {

&#x20;                   "type": "click",

&#x20;                   "name": "?��?競賽",

&#x20;                   "key": "training"

&#x20;               }

&#x20;           ]

&#x20;       }

&#x20;   ]

}

**2.  ?��?訊息**

**Line Text message \[3]**

**{**

&#x20;   **"type": "text",**

&#x20;   **"text": "Hello, world"**

**}**

�?一：Line?��?訊息?�件(Message object)之格式�??�數?��??��??��??��?

| **Property** | **Type** | **Required** | **Description**                                                                                                                                                                                                                                                               |
| ------------ | -------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type         | String   | Required     | text                                                                                                                                                                                                                                                                          |
| text         | String   | Required     | <p>Message text. You can include the following emoji:</p><ul><li>Unicode emoji</li><li>LINE original emoji (<a href="https://developers.line.me/media/messaging-api/emoji-list.pdf">Unicode codepoint table for LINE original emoji</a>)</li></ul><p>Max: 2000 characters</p> |

**WeChat?�送�??��???\[4]**

{

&#x20;   "touser":"OPENID",

&#x20;   "msgtype":"text",

&#x20;   "text":

&#x20;   {

&#x20;        "content":"Hello, World"

&#x20;   }

}

�?二�?WeChat?�本消息之格式�??�於WeChat將接?�方?�ID設�??��??�JSON?�件?��??��?，�?以�??��?了touser

| **?�數**  | **?�否必�?** | **?�述**                                 |
| ------- | -------- | -------------------------------------- |
| ToUser  | ??       | ?�收?�帳?��??�到?�OpenID�?                      |
| MsgType | ??       | text                                   |
| Content | ??       | ?�復?��??�內容�??��?：在content中能夠�?行�?微信客戶端就?��??��?顯示�?|

**3.  影�??��?訊息**

**Line Imagemap message**

Imagemap 訊息範�? with tappable regions

{

&#x20;   "type": "imagemap",

&#x20;   "baseUrl": "https://storage.googleapis.com/goldeninsurancebroker-4392f.appspot.com/imageMap/training\_0629",

&#x20;   "altText": "?��?競賽",

&#x20;   "baseSize": {

&#x20;       "width": 1040,

&#x20;       "height": 530

&#x20;   },

&#x20;   "actions": \[

&#x20;       {

&#x20;           "type": "uri",

&#x20;           "area": {

&#x20;               "x": 0,

&#x20;               "y": 201,

&#x20;               "width": 335,

&#x20;               "height": 410

&#x20;           },

&#x20;           "linkUri": \`${config.uriName}#/trainingCases/{lineId}\`

&#x20;       },

&#x20;       {

&#x20;           "type": "uri",

&#x20;           "area": {

&#x20;               "x": 335,

&#x20;               "y": 192,

&#x20;               "width": 345,

&#x20;               "height": 419

&#x20;           },

&#x20;           "linkUri": \`${config.uriName}#/achievements/{lineId}\`

&#x20;       },

&#x20;       {

&#x20;           "type": "uri",

&#x20;           "area": {

&#x20;               "x": 680,

&#x20;               "y": 189,

&#x20;               "width": 356,

&#x20;               "height": 422

&#x20;           },

&#x20;           "linkUri": hostName + "/broker\_system/views/lineLogin/personal.html?page=course"

&#x20;       }

&#x20;   ]

}

�?三�?Line 影�??��?訊息?��?，可以�??�imagemap ?��??�件?�以?�件???形�?表現

| **Property**    | **Type**                                                                                                           | **Required** | **Description**                                                                                                                                          |
| --------------- | ------------------------------------------------------------------------------------------------------------------ | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type            | String                                                                                                             | Required     | imagemap                                                                                                                                                 |
| baseUrl         | String                                                                                                             | Required     | <p><a href="https://developers.line.me/en/reference/messaging-api/#base-url">Base URL</a> of image (Max: 1000 characters)<br> <strong>HTTPS</strong></p> |
| altText         | String                                                                                                             | Required     | <p>Alternative text<br> Max: 400 characters</p>                                                                                                          |
| baseSize.width  | Number                                                                                                             | Required     | Width of base image (set to 1040px)                                                                                                                      |
| baseSize.height | Number                                                                                                             | Required     | Height of base image (set to the height that corresponds to a width of 1040px)                                                                           |
| actions         | Array of [imagemap action objects](https://developers.line.me/en/reference/messaging-api/#imagemap-action-objects) | Required     | <p>Action when tapped<br> Max: 50</p>                                                                                                                    |

**Line Imagemap URI action object**

�??��??��? actions，imagemap action object

| **Property** | **Type**                                                                                            | **Required** | **Description**                                                                                                                                                               |
| ------------ | --------------------------------------------------------------------------------------------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type         | String                                                                                              | Required     | uri                                                                                                                                                                           |
| label        | String                                                                                              | Optional     | <p>Label for the action. Spoken when the accessibility feature is enabled on the client device.<br> Max: 50 characters<br> Supported on LINE iOS version 8.2.0 and later.</p> |
| linkUri      | String                                                                                              | Required     | <p>Webpage URL<br> Max: 1000 characters</p>                                                                                                                                   |
| area         | [Imagemap area object](https://developers.line.me/en/reference/messaging-api/#imagemap-area-object) | Required     | Defined tappable area                                                                                                                                                         |

**WeChat?��?消息（�??�跳轉到外�?�?*

?��?消息條數?�制??條以?��?注�?，�??��??�數超�?8，�?將�??�響?��?

{

&#x20;   "touser":"OPENID",

&#x20;   "msgtype":"news",

&#x20;   "news":{

&#x20;       "articles": \[

&#x20;        {

&#x20;            "title":"課�??��?",

&#x20;            "description":"?��?競賽",

&#x20;            "url":\`${config.uriName}#/trainingCases/{lineId}\`,

&#x20;            "picurl":"?�示網�?"

&#x20;        },

&#x20;        {

&#x20;            "title":"競賽?�勵",

&#x20;            "description":"?��?競賽",

&#x20;            "url":\`${config.uriName}#/achievements/{lineId}\`,

&#x20;            "picurl":"?�示網�?"

&#x20;        },

&#x20;        {

&#x20;            "title":"?��?專�?",

&#x20;            "description":"?��?競賽",

&#x20;            "url": hostName + "/broker\_system/views/lineLogin/personal.html?page=course",

&#x20;            "picurl":"?�示網�?"

&#x20;        }

&#x20;        ]

&#x20;   }

}

**Line?�ImageMap action object?�數?��???條以?��?且�?一?��???��?要另外填寫�?字�?製�??�示，�??�直?��??�單一WeChat?��?消息?�否?��?要改以�??��??��??��?網�??�形式�??��??��?*

�?五�? WeChat?��?訊息?��?

| ?�數           | ?�否必�? | 說�?                                           |
| ------------ | ---- | -------------------------------------------- |
| ToUserName   | ??   | ?�收?�帳?��??�到?�OpenID�?                            |
| MsgType      | ??   | news                                         |
| ArticleCount | ??   | ?��?消息?�數，�??�為8條以??                              |
| Articles     | ??   | 多�??��?消息信息，�?認第一?�item?�大??注�?，�??��??�數超�?8，�?將�??�響??    |
| Title        | ??   | ?��?消息標�?                                       |
| Description  | ??   | ?��?消息?�述                                       |
| PicUrl       | ??   | ?��??�接，支?�JPG?�PNG?��?，�?好�??��??�大??60\*200，�???00\*200 |
| Url          | ??   | 點�??��?消息跳�??�接                                   |

**4.  ?��?�?��訊息**

**Line Buttons template**

{

&#x20;                   type: "template",

&#x20;                   altText: \`${companyName}資�??�詢\`,

&#x20;                   template: {

&#x20;                       type: "buttons",

&#x20;                       title: \`?��?iSmart?�能秘書\`,

&#x20;                       text: \`${companyName}繳費資�?\`,

&#x20;                       actions: \[

&#x20;                           {

&#x20;                               type: "uri",

&#x20;                               label: "?��?資�?",

&#x20;                               uri: \`${config.uriName}#/paymentInfo/${actionMessage.lineId}/${index}\`

&#x20;                           }

&#x20;                       ]

&#x20;                   }

&#x20;               }

Template with an image, title, text, and multiple action buttons.

�??��??��?�?��訊息?��?

| **Property**      | **Type**                                                                                         | **Required** | **Description**                                                                                                         |
| ----------------- | ------------------------------------------------------------------------------------------------ | ------------ | ----------------------------------------------------------------------------------------------------------------------- |
| type              | String                                                                                           | Required     | `buttons`                                                                                                               |
| thumbnailImageUrl | String                                                                                           | Optional     | <p>Image URL (Max: 1000 characters)<br> <strong>HTTPS</strong><br> JPEG or PNG<br> Max width: 1024px<br> Max: 1 MB</p>  |
| title             | String                                                                                           | Optional     | <p>Title<br> Max: 40 characters</p>                                                                                     |
| text              | String                                                                                           | Required     | <p>Message text<br> Max: 160 characters (no image or title)<br> Max: 60 characters (message with an image or title)</p> |
| actions           | Array of [action objects](https://developers.line.me/en/reference/messaging-api/#action-objects) | Required     | <p>Action when tapped<br> Max: 4</p>                                                                                    |

WeChat?�送�??��??��?點�?跳�??��??��? ?��?消息條數?�制??條以?��?注�?，�??��??�數超�?8，�?將�??�響?��?

{

&#x20;   "touser":"OPENID",

&#x20;   "msgtype":"news",

&#x20;   "news":{

&#x20;       "articles": \[

&#x20;        {

&#x20;            "title":\`?�Confirm template�?actions?�第一?�label\`,

&#x20;            "description": "?�Confirm template?�text",

&#x20;            "url":\`${config.uriName}#/paymentInfo/${actionMessage.lineId}/${index}\`,

&#x20;            "picurl":"?�示網�?"

&#x20;        }

&#x20;        ]

&#x20;   }

}

**轉�??�WeChat?��?消息?��?要另外�?供�?示即?��?*

**5.  ?�確認」樣?��???*

**Confirm template**

{

&#x20; "type": "template",

&#x20; "altText": "?�Confirm template ?�text ",

&#x20; "template": {

&#x20;     "type": "confirm",

&#x20;     "text": "?��?人壽\_人身保險要�???,

&#x20;     "actions": \[

&#x20;         {

&#x20;           "type": "uri",

&#x20;           "label": "檢�?",

&#x20;           "uri": "?�件網�?"

&#x20;         },

&#x20;         {

&#x20;            "type": "uri",

&#x20;           "label": "轉傳",

&#x20;           "uri": \`${config.uriName}#/forward/${lineId}/${fileId}/${type}\`

&#x20;         }

&#x20;     ]

&#x20; }

}

Template with two action buttons.

�?�?

| **Property** | **Type**                                                                                         | **Required** | **Description**                                               |   |   |
| ------------ | ------------------------------------------------------------------------------------------------ | ------------ | ------------------------------------------------------------- | - | - |
| type         | String                                                                                           | Required     | `confirm`                                                     |   |   |
| text         | String                                                                                           | Required     | <p>Message text<br> Max: 240 characters</p>                   |   |   |
| actions      | Array of [action objects](https://developers.line.me/en/reference/messaging-api/#action-objects) | Required     | <p>Action when tapped<br> Set 2 actions for the 2 buttons</p> |   |   |
|              |                                                                                                  |              |                                                               |   |   |

WeChat?�送�??��??��?點�?跳�??��??��? ?��?消息條數?�制??條以?��?注�?，�??��??�數超�?8，�?將�??�響?��?

{

&#x20;   "touser":"OPENID",

&#x20;   "msgtype":"news",

&#x20;   "news":{

&#x20;       "articles": \[

&#x20;        {

&#x20;            "title":"?�Confirm template ?�text \n?�Confirm template�?actions?�第一?�label ",

&#x20;            "description":" ?�Confirm template ?�text",

&#x20;            "url":"?�Confirm template�?actions?�第一?�uri ?�件網�? ",

&#x20;            "picurl":"?�示網�?"

&#x20;        },

&#x20;        {

&#x20;            "title":"?�Confirm template�?actions?�第二個label ",

&#x20;            "description":"??Confirm template ?�text",

&#x20;            "url":\`${config.uriName}#/forward/${lineId}/${fileId}/${type}\`,

&#x20;            "picurl":"?�示網�?"

&#x20;        }

&#x20;        ]

&#x20;   }

}

**轉�??�WeChat?��?消息?��??��??��??�示，�?news articles之第一?�title要�??�Confirm template ?�text，以?��??�description沒�?顯示?��?使用?��????辨該?��?消息?�用?��?*

?�WeChat?��?消息?��?一條�?，news articles之title?�description?��?�?

?�WeChat?��?消息?�兩條�??��?以�??��??��?news articles之title?�顯示出�?
