Sub DeleteAllShapes()
' Buh shape-uud (chart, graphic etc.) ustgah 
' Credit to: https://www.automateexcel.com/vba-code-examples/

	Dim GetShape As Shape

	For Each GetShape In ActiveSheet.Shapes
  		GetShape.Delete
	Next

End Sub