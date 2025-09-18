# 在Vue 3專案中新增 jQuery 套件

在專案目錄底下使用npm安裝jQuery：

```powershell
npm i jquery --save
```

並於vue.config.js新增jQuery 全域變數相關宣告：

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

有了宣告還不夠～為了讓tslint TypeScript語法檢查器能判斷jQuery內部變數型態，還須要在tsconfig.json內引用jQuery內部語法的型態定義：

```json
"types": [
      "webpack-env",
      "jquery"      
    ]
```

至此就可以在專案底下任一個.vue檔案使用jQuery了。只要事先引入套件即可：

```typescript
import $ from 'jquery';
```
