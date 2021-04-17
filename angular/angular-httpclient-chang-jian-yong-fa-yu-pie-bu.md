# Angular HttpClient 常見用法與撇步

## 匯入 HttpClientModule

在 import 模組的時候，順序也很重要！官方建議HttpClientModule要寫在 BrowserModule 之後，以防後患無窮～

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

## 注入 HttpClient 到各元件

在 建構式 \(constructor\) 引數內注入HttpClient服務作為 應用程式類別的依賴 \(dependency of an application class\)，像下方程式碼類別的名稱叫做ConfigService。

```typescript
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class ConfigService {
  constructor(private http: HttpClient) { }
}
```



## 1.以 HTTP GET 取得伺服端 JSON 物件

 單純取得伺服器的 JSON 資料，get 函數可用 any 型別。

```typescript
this.http.get<any>(this.url).subscribe(data => {
  this.data = data;
});
```

 但如果已經預知物件明確屬性的話，就直接替回傳的物件建立相對應的介面\(interface\) 。

HttpClient預設透過 subscribe 接收的資料會先做 JSON 反序列化\(deserialization\)，免除以 JSON.parse\(\) 再次解析。

## 2.以 HTTP GET 取得伺服端 JSON 物件完整的 HTTP 回應

若要得知單次HTTP請求的 狀態碼、 回應標頭等資訊，就要另外加入 options 參數。以下範例會在接收回應資料時，取得一個 HttpResponse&lt;any&gt;型態的資料：

```typescript
this.http.get<any>(this.url, { observe: 'response' }).subscribe(res => {
  this.data = res.body;
  let response: HttpResponse<any> = res;  
  let status: number = res.status;
  let statusText: string = res.statusText;
  let headers: HttpHeaders = res.headers;  
});
```

## 3.以 HTTP GET 取得伺服端回應資料的原始內容

當API 回應的內容為非JSON 物件的情況，會希望 HttpClient 不要自動做 JSON 序列化 。此時要在 options 參數加上 responseType 屬性，告訴回傳值應為 text \(純文字\)。

```typescript
this.http.get(this.url, {observe: 'response', responseType: 'text'})
  .subscribe((res) => {
    this.data = res.body;
    let response: HttpResponse<any> = res;    
  });
```

## 4. 以 HTTP POST 把物件傳到伺服端

這種情況下，post\(\)的第二個參數要是請求 Body 的資料。HttpClient 預設會自動把物件做 JSON 序列化，並包含 Content-Type為 application/json 的 標頭\(header\)，而接收回應時也會做JSON 序列化 。

```typescript
this.http.post<any>(this.url, { key: value }).subscribe(res => {
  this.data = res;
});
```

## 4. 以 HTTP POST 把字串傳到伺服端

post\(\)第二個參數是字串的話，HttpClient 將不做 JSON 序列化，且發出請求時，會包含 Content-Type 為 text/plain 的標頭，且會按請求的Content-Type 處理回傳值。

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



