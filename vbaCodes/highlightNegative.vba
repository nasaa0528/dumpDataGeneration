Public Sub highlightNegative()
' Surug utguudiig todruulj haruulah 
' Credit to: https://www.automateexcel.com/vba-code-examples/

    Dim myRange As Range
    Dim cell As Range
    ' criteria - g uur toogoor solisnoor todorhoi toonoos baga toog haih bolomjtoi 
    Dim criteria As Integer
    criteria = 0
    
    Set myRange = Selection
    
    For Each cell In myRange
        If cell.Value < criteria Then
            cell.Interior.ColorIndex = 36
        End If
    Next cell
End Sub