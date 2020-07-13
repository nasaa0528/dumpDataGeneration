Sub SplitNames()
' Neg cell dotorh neruudiin 2 dahi ugiig daraagiin nudend salgaj hadgalah
Dim rng As Range: Set rng = Selection
Dim cel As Range
For Each cel In rng.Cells
    Range(cel, cel.Offset(0, 1)).Value = Split(cel.Value, " ")
Next cel

End Sub