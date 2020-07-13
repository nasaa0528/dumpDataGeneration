Sub InsertAlternateColumns()
' Baganuudiin urd hooson bagana nemeh
' Credit to: https://www.automateexcel.com/vba-code-examples/ 

Dim rng As Range
Dim CountCol As Integer
Dim i As Integer
Set rng = Selection
CountCol = rng.EntireColumn.Count
For i = 1 To CountCol
ActiveCell.EntireColumn.Insert
ActiveCell.Offset(0, 2).Select
Next i
End Sub
