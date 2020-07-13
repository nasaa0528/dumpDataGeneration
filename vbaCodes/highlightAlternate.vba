Sub HighlightAlternateRows()
' Alternate row-uudiig unguur yalgah 
' Credit to: https://trumpexcel.com/excel-macro-examples/#Sort-Worksheets-Alphabetically-Using-VBA
	Dim Myrange As Range
	Dim Myrow As Range
	Set Myrange = Selection
	For Each Myrow In Myrange.Rows
	   If Myrow.Row Mod 2 = 1 Then
	      Myrow.Interior.Color = vbCyan
	   End If
	Next Myrow
End Sub