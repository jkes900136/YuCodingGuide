# ?�Vue 3專�?中新�?jQuery 套件

?��?案目?��?下使?�npm安�?jQuery�?

```powershell
npm i jquery --save
```

並於vue.config.js?��?jQuery ?��?變數?��?�??�?

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

?��?�???��?夠�??��?讓tslint TypeScript語�?檢查?�能?�斷jQuery?�部變數?��?，�??��??�tsconfig.json?��??�jQuery?�部語�??��??��?義�?

```json
"types": [
      "webpack-env",
      "jquery"      
    ]
```

?�此就可以在專�?底�?任�???vue檔�?使用jQuery了。只要�??��??��?件即?��?

```typescript
import $ from 'jquery';
```
