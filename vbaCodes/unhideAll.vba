Sub UnhideAllWoksheets()
    ' Nuugdsan sheet-uudiig il gargah
	' Credit to: https://www.automateexcel.com/vba-code-examples/

    Dim ws As Worksheet
    
    For Each ws In ActiveWorkbook.Worksheets
        ws.Visible = xlSheetVisible
    Next ws
    
End Sub
