Sub LockCellsWithFormulas()
' Formula-tai buh cell-uudiig tugjih 
' Credit to: https://trumpexcel.com/excel-macro-examples/#Protect/Lock-Cells-with-Formulas
	With ActiveSheet
	   .Unprotect
	   .Cells.Locked = False
	   .Cells.SpecialCells(xlCellTypeFormulas).Locked = True
	   .Protect AllowDeletingRows:=True
	End With
End Sub