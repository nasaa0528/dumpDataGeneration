Sub HighlightDuplicateValues()
' Idevhitei hesguudees davhardsan cell-uudiig yalgaj haruulah 
' Credit to: https://www.automateexcel.com/vba-code-examples/

    Dim myRange As Range
    Dim cell As Range
    
    Set myRange = Selection
    
    For Each cell In myRange
        If WorksheetFunction.CountIf(myRange, cell.Value) > 1 Then
            cell.Interior.ColorIndex = 36
        End If
    Next cell
End Sub