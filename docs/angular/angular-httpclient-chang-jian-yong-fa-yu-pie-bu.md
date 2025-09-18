# Angular HttpClient 常�??��??��?�?

## ?�入 HttpClientModule

??import 模�??��??��??��?也�??��?！�??�建議HttpClientModule要寫??BrowserModule 之�?，以?��???��窮�?

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

## 注入 HttpClient ?��??�件

??建�?�?\(constructor\) 引數?�注?�HttpClient?��?作為 ?�用程�?類別?��?�?\(dependency of an application class\)，�?下方程�?碼�??��??�稱?��?ConfigService??

```typescript
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class ConfigService {
  constructor(private http: HttpClient) { }
}
```



## 1.�?HTTP GET ?��?伺�?�?JSON ?�件

 ?��??��?伺�??��? JSON 資�?，get ?�數?�用 any ?�別??

```typescript
this.http.get<any>(this.url).subscribe(data => {
  this.data = data;
});
```

 但�??�已經�??�物件�?確屬?��?話�?就直?�替?�傳?�物件建立相對�??��??�\(interface\) ??

HttpClient?�設?��? subscribe ?�收?��??��??��? JSON ?��??��?\(deserialization\)，�??�以 JSON.parse\(\) ?�次�????

## 2.�?HTTP GET ?��?伺�?�?JSON ?�件完整??HTTP ?��?

?��?得知?�次HTTP請�????�?�碼???��?標頭等�?訊�?就�??��??�入 options ?�數?�以下�?例�??�接?��??��??��?，�?得�???HttpResponse&lt;any&gt;?��??��??��?

```typescript
this.http.get<any>(this.url, { observe: 'response' }).subscribe(res => {
  this.data = res.body;
  let response: HttpResponse<any> = res;  
  let status: number = res.status;
  let statusText: string = res.statusText;
  let headers: HttpHeaders = res.headers;  
});
```

## 3.�?HTTP GET ?��?伺�?端�??��??��??��??�容

?�API ?��??�內容為?�JSON ?�件?��?況�??��???HttpClient 不�??��???JSON 序�????�此?��???options ?�數?��? responseType 屬性�??�訴?�傳?��???text \(純�?字\)??

```typescript
this.http.get(this.url, {observe: 'response', responseType: 'text'})
  .subscribe((res) => {
    this.data = res.body;
    let response: HttpResponse<any> = res;    
  });
```

## 4. �?HTTP POST ?�物件傳?�伺?�端

?�種?��?下�?post\(\)?�第二個�??��??��?�?Body ?��??�。HttpClient ?�設?�自?��??�件??JSON 序�??��?並�???Content-Type??application/json ??標頭\(header\)，而接?��??��?也�??�JSON 序�?????

```typescript
this.http.post<any>(this.url, { key: value }).subscribe(res => {
  this.data = res;
});
```

## 4. �?HTTP POST ?��?串傳?�伺?�端

post\(\)第�??��??�是字串?�話，HttpClient 將�???JSON 序�??��?且發?��?求�?，�??�含 Content-Type ??text/plain ?��??��?且�??��?求�?Content-Type ?��??�傳?��?

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



