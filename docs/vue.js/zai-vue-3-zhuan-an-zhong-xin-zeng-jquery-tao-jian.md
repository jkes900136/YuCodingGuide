# ?¨Vue 3å°ˆæ?ä¸­æ–°å¢?jQuery å¥—ä»¶

?¨å?æ¡ˆç›®?„å?ä¸‹ä½¿?¨npmå®‰è?jQueryï¼?

```powershell
npm i jquery --save
```

ä¸¦æ–¼vue.config.js?°å?jQuery ?¨å?è®Šæ•¸?¸é?å®??ï¼?

```json
configureWebpack: {
        plugins: [
            new webpack.ProvidePlugin({
                $: 'jquery',
                jquery: 'jquery',
                'window.jQuery': 'jquery',
                jQuery: 'jquery'
            })
        ]
    }
```

?‰ä?å®???„ä?å¤ ï??ºä?è®“tslint TypeScriptèªæ?æª¢æŸ¥?¨èƒ½?¤æ–·jQuery?§éƒ¨è®Šæ•¸?‹æ?ï¼Œé??ˆè??¨tsconfig.json?§å??¨jQuery?§éƒ¨èªæ??„å??‹å?ç¾©ï?

```json
"types": [
      "webpack-env",
      "jquery"      
    ]
```

?³æ­¤å°±å¯ä»¥åœ¨å°ˆæ?åº•ä?ä»»ä???vueæª”æ?ä½¿ç”¨jQueryäº†ã€‚åªè¦ä??ˆå??¥å?ä»¶å³?¯ï?

```typescript
import $ from 'jquery';
```
