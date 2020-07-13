Sub ConvertToValues()
' Buh formula-g engiin constant utga bolgon huvirgah 
' Credit to: https://trumpexcel.com/excel-macro-examples/#Convert-All-Formulas-into-Values 

	With ActiveSheet.UsedRange
		.Value = .Value
	End With
End Sub