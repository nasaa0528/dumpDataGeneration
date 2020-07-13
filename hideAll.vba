Sub HideAllExceptActiveSheet()
' Active sheet-ees busad buh sheet-iig nuuh 
' Credit to: https://www.automateexcel.com/vba-code-examples/

    Dim ws As Worksheet
    
    For Each ws In ThisWorkbook.Worksheets
        If ws.Name <> ActiveSheet.Name Then ws.Visible = xlSheetHidden
    Next ws
    
End Sub