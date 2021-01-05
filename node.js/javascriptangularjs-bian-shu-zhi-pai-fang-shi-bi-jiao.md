# JavaScript/AngularJS 變數指派方式比較

## Pass-by-Value

| 變數類型 | 預設指派方式 |
| :--- | :--- |
| 原始型別\(strings, numbers, booleans\) | passed by value |
| 物件\(objects\) | passed by reference |

## Pass-by-Reference

指派給目標變數的值，其實是來源變數的隱式參照，而不是來源變數值的副本。通常目標變數被修改時，來源參數也會同時修改。因此傳參照指派提供了一種來源變數和目標變數交換資料的方法。傳參照指派的語言中追蹤目標變數值變動的過程比較難，易產生不易察覺的bug。

來源變數被指派至對應的目標變數上（通常是把值複製到新記憶體區域）。來源變數只是被複製，來源變數的值不會變。

{% embed url="https://stackoverflow.com/questions/31548412/angularjs-data-binding-when-passing-a-reference" %}

{% embed url="https://stackoverflow.com/questions/48583501/pass-by-value-in-json-in-angular" %}

{% embed url="https://zh.wikipedia.org/wiki/%E6%B1%82%E5%80%BC%E7%AD%96%E7%95%A5" %}



