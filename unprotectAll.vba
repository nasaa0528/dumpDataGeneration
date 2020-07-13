Sub UnProtectAllSheets()
' protect hiisen buh sheet-uudiin protection-iig bhgu bolgoh
' Credit to: https://www.automateexcel.com/vba-code-examples/

    Dim ws As Worksheet
    Dim pwd as String 
    ' Password hesgiig dor solij bichih 
    pwd = "password"
    
    For Each ws In Worksheets
        ws.Unprotect pwd
    Next ws
    
End Sub