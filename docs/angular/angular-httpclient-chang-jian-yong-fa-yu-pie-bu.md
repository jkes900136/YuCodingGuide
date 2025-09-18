# Angular HttpClient å¸¸è??¨æ??‡æ?æ­?

## ?¯å…¥ HttpClientModule

??import æ¨¡ç??„æ??™ï??†å?ä¹Ÿå??è?ï¼å??¹å»ºè­°HttpClientModuleè¦å¯«??BrowserModule ä¹‹å?ï¼Œä»¥?²å???„¡çª®ï?

```typescript
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  imports: [
    BrowserModule,
    // import HttpClientModule after BrowserModule.
    HttpClientModule,
  ],
  declarations: [
    AppComponent,
  ],
  bootstrap: [ AppComponent ]
})
export class AppModule {}
```

## æ³¨å…¥ HttpClient ?°å??ƒä»¶

??å»ºæ?å¼?\(constructor\) å¼•æ•¸?§æ³¨?¥HttpClient?å?ä½œç‚º ?‰ç”¨ç¨‹å?é¡åˆ¥?„ä?è³?\(dependency of an application class\)ï¼Œå?ä¸‹æ–¹ç¨‹å?ç¢¼é??¥ç??ç¨±?«å?ConfigService??

```typescript
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class ConfigService {
  constructor(private http: HttpClient) { }
}
```



## 1.ä»?HTTP GET ?–å?ä¼ºæ?ç«?JSON ?©ä»¶

 ?®ç??–å?ä¼ºæ??¨ç? JSON è³‡æ?ï¼Œget ?½æ•¸?¯ç”¨ any ?‹åˆ¥??

```typescript
this.http.get<any>(this.url).subscribe(data => {
  this.data = data;
});
```

 ä½†å??œå·²ç¶“é??¥ç‰©ä»¶æ?ç¢ºå±¬?§ç?è©±ï?å°±ç›´?¥æ›¿?å‚³?„ç‰©ä»¶å»ºç«‹ç›¸å°æ??„ä??¢\(interface\) ??

HttpClient?è¨­?é? subscribe ?¥æ”¶?„è??™æ??ˆå? JSON ?å??—å?\(deserialization\)ï¼Œå??¤ä»¥ JSON.parse\(\) ?æ¬¡è§????

## 2.ä»?HTTP GET ?–å?ä¼ºæ?ç«?JSON ?©ä»¶å®Œæ•´??HTTP ?æ?

?¥è?å¾—çŸ¥?®æ¬¡HTTPè«‹æ????€?‹ç¢¼???æ?æ¨™é ­ç­‰è?è¨Šï?å°±è??¦å?? å…¥ options ?ƒæ•¸?‚ä»¥ä¸‹ç?ä¾‹æ??¨æ¥?¶å??‰è??™æ?ï¼Œå?å¾—ä???HttpResponse&lt;any&gt;?‹æ??„è??™ï?

```typescript
this.http.get<any>(this.url, { observe: 'response' }).subscribe(res => {
  this.data = res.body;
  let response: HttpResponse<any> = res;  
  let status: number = res.status;
  let statusText: string = res.statusText;
  let headers: HttpHeaders = res.headers;  
});
```

## 3.ä»?HTTP GET ?–å?ä¼ºæ?ç«¯å??‰è??™ç??Ÿå??§å®¹

?¶API ?æ??„å…§å®¹ç‚º?JSON ?©ä»¶?„æ?æ³ï??ƒå???HttpClient ä¸è??ªå???JSON åºå????‚æ­¤?‚è???options ?ƒæ•¸? ä? responseType å±¬æ€§ï??Šè¨´?å‚³?¼æ???text \(ç´”æ?å­—\)??

```typescript
this.http.get(this.url, {observe: 'response', responseType: 'text'})
  .subscribe((res) => {
    this.data = res.body;
    let response: HttpResponse<any> = res;    
  });
```

## 4. ä»?HTTP POST ?Šç‰©ä»¶å‚³?°ä¼º?ç«¯

?™ç¨®?…æ?ä¸‹ï?post\(\)?„ç¬¬äºŒå€‹å??¸è??¯è?æ±?Body ?„è??™ã€‚HttpClient ?è¨­?ƒè‡ª?•æ??©ä»¶??JSON åºå??–ï?ä¸¦å???Content-Type??application/json ??æ¨™é ­\(header\)ï¼Œè€Œæ¥?¶å??‰æ?ä¹Ÿæ??šJSON åºå?????

```typescript
this.http.post<any>(this.url, { key: value }).subscribe(res => {
  this.data = res;
});
```

## 4. ä»?HTTP POST ?Šå?ä¸²å‚³?°ä¼º?ç«¯

post\(\)ç¬¬ä??‹å??¸æ˜¯å­—ä¸²?„è©±ï¼ŒHttpClient å°‡ä???JSON åºå??–ï?ä¸”ç™¼?ºè?æ±‚æ?ï¼Œæ??…å« Content-Type ??text/plain ?„æ??­ï?ä¸”æ??‰è?æ±‚ç?Content-Type ?•ç??å‚³?¼ã€?

```typescript
let headers = new HttpHeaders({
  'Content-Type': 'text/json'
});
this.http.post<any>(this.url, JSON.stringify('text'), { headers: headers })
  .subscribe((data) => {
    this.data = data;
  });
```

## Reference

{% embed url="https://angular.io/guide/http" %}

{% embed url="https://blog.miniasp.com/post/2019/01/20/Angular-HttpClient-Pitfall-and-Tricks" %}



