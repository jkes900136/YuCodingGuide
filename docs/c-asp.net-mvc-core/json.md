# JSON

C\# ?�件?�常?��??��??�為?��?義Class ?��??��??�是�?

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

?�以使用

SerializeObject\(\)將C\#?�件序�??�為JSON

DeserializeObject\(\)將JSON?��??��??�C\#?�件

[https://dotblogs.com.tw/berrynote/2016/08/18/200338](https://dotblogs.com.tw/berrynote/2016/08/18/200338)

