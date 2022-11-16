# 開發環境網站 SSL 憑證無效解決方式

ASP.NET Core 於localhost使用https連線時，會自動產生一個自我簽發的憑證，預設有效期為一年。

雖然剛開始設計的很周到，但憑證在過期後，ASP.NET Core 後端卻呆呆地跳出以下訊息：&#x20;

AuthenticationException: The remote certificate is invalid because of errors in the certificate chain: NotTimeValid&#x20;

解決方式：   刪除 C:\Users\\\[使用者名稱]\AppData\Roaming\ASP.NET\https\ 裡面所有檔案，然後重新啟動專案。若有搭配 Vue ，則連同 Vue 的CLI一同重啟，此時這些檔案會自動重新產生。![](<../.gitbook/assets/image (2).png>)

![](<../.gitbook/assets/image (1).png>)

