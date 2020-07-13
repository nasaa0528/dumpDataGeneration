Sub InsertAlternateRows()
' Muruudiin araas hooson mur nemeh
' Credit to: https://www.automateexcel.com/vba-code-examples/ 

Dim rng As Range
Dim CountRow As Integer
Dim i As Integer
Set rng = Selection
CountRow = rng.EntireRow.Count
For i = 1 To CountRow
ActiveCell.EntireRow.Insert
ActiveCell.Offset(2, 0).Select
Next i
End Sub