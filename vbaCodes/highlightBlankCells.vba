Sub HighlightBlankCells()
' Hooson nuduudiig unguur yalgah 
' Credit to: https://www.automateexcel.com/vba-code-examples/
    Dim rng As Range
    
    Set rng = Selection
    rng.SpecialCells(xlCellTypeBlanks).Interior.Color = vbCyan
    
End Sub