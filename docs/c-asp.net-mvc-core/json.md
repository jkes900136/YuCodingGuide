# JSON

C\# 物件通常是資料型態為自定義Class 的變數，像是：

```csharp
 Student studentData = db.Student.Where(s => s.StudentId == studentId).FirstOrDefault();
```

```csharp
public class Student
{
    public int StudentId { get; set; }
    public string Name { get; set; }         
    public DateTime Birthday { get; set; }            
    public bool Gender { get; set; }         
    public int? CountryId { get; set; }  
}
```

可以使用

SerializeObject\(\)將C\#物件序列化為JSON

DeserializeObject\(\)將JSON反序列化為C\#物件

[https://dotblogs.com.tw/berrynote/2016/08/18/200338](https://dotblogs.com.tw/berrynote/2016/08/18/200338)

