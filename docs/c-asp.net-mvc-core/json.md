# JSON

C\# ?©ä»¶?šå¸¸?¯è??™å??‹ç‚º?ªå?ç¾©Class ?„è??¸ï??æ˜¯ï¼?

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

?¯ä»¥ä½¿ç”¨

SerializeObject\(\)å°‡C\#?©ä»¶åºå??–ç‚ºJSON

DeserializeObject\(\)å°‡JSON?å??—å??ºC\#?©ä»¶

[https://dotblogs.com.tw/berrynote/2016/08/18/200338](https://dotblogs.com.tw/berrynote/2016/08/18/200338)

