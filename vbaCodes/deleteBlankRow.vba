Sub DeleteBlankRows()
' Hooson moruudiig ustgah 
' Credit to: https://www.automateexcel.com/vba-code-examples/

	Dim x As Long

	With ActiveSheet
	    For x = .Cells.SpecialCells(xlCellTypeLastCell).Row To 1 Step -1
	        If WorksheetFunction.CountA(.Rows(x)) = 0 Then
	            ActiveSheet.Rows(x).Delete
	        End If
	    Next
	End With

End Sub