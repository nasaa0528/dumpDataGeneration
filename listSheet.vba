Sub ListSheets()
    ' Workbook dotorh buh sheet-uudiig idevhitei bgaa
    ' sheet-iinehnii baganad jagsaan bichne
    ' Warning: Absoulte Reference ashiglasan uchraas
    ' hervee tanii excel sheet deer data bgaa bol
    ' terhuu datag tani ustgaad orond ni shine data bichne
    ' Credit to: https://www.automateexcel.com/vba-code-examples/

    
    Dim ws As Worksheet
    Dim x As Integer
    
    x = 1
    
    ActiveSheet.Range("A:A").Clear
    
    For Each ws In Worksheets
        ActiveSheet.Cells(x, 1) = ws.Name
        x = x + 1
    Next ws
    
End Sub
