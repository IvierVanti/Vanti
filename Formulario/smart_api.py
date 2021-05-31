import smartsheet



def Add_Rows(token,hoja,columnas,Datos):
	smartsheet_client = smartsheet.Smartsheet(token)
	smartsheet_client.errors_as_exceptions(True)
		
	# Specify cell values for one row
	row_a = smartsheet.models.Row()
	row_a.to_top = True

	for i in range(0,len(columnas)):
		row_a.cells.append( {
	  	'column_id': columnas[i],
	  	'value': Datos[i],
	}
	)

	# Add rows to sheet
	response = smartsheet_client.Sheets.add_rows(hoja,[row_a]) 




