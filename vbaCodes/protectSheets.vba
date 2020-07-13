Sub ProtectAllSheets()
' Buh worksheet-uudiig protect hiih 
' Credit to: https://www.automateexcel.com/vba-code-examples/ 
    Dim ws As Worksheet
    Dim pwd as String
    ' Password hesgiig dor solij bichih 
    pwd = "password"
    
    For Each ws In Worksheets
        ws.protect pwd
    Next ws
    
End Sub