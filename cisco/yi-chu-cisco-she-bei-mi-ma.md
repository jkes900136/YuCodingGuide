# 移除 Cisco 設備密碼

在嘗試設定Cisco設備多種參數的時候，常會須要多次重開機測試參數調整之效果，這時有密碼的情況，對於直接以實體 Console 線連接設備操作的人來說，易造成不便。

其實可以暫時移除密碼，待確定測試成功後再恢復

於全域設定模式\(global configuration mode\)執行以下指令： 

```text
no enable password

line con 0

no login

no password

end
```

