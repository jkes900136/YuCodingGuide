# Exchange Server 2010 Management Console ?�現WinRM client?�誤

![](assets/2-27-2014-11-18-23-AM.jpg)

?��??�Exchange Server 2010?�伺?�器?��?Windows Server?�本?��??�更?��?後�??��?Exchange Management Console?�能?��??�以下�?況�?

_Connecting to remote server failed with the following error message : The WinRM client received an HTTP server error status (500), but the remote service did not include any other information about the cause fothe failure._&#x20;

_It was running the command 'Discover-ExchangeServer -UseWIA $true -SuppressError $true -CurrentVersion 'Version 14.X (Build XXX.X)''._

?�代表WinRM IIS Extension（擴?��?件�??��?級Windows?�被�?��安�?了�??�要到伺�??�管?�員->?��?角色?��??��?它�??�去�?

![](<assets/image (25).png>)![](<assets/image (26).png>)![](<assets/image (23).png>)![](<assets/image (27).png>)![](<assets/image (24).png>)![](<assets/image (22).png>)
