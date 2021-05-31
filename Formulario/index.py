from types import MethodType
from flask import Flask,render_template,request
import form
from smart_api import Add_Rows

token_1='h9wH1CcjKraGxstdsL9QdyYsOHLpN4Av4EqMl'
hoja_1=6424629934876548
columna_Nombre=4773529437661060
columna_Email=2521729623975812
columna_Telefono=7025329251346308
columna_Mensaje=1395829717133188
columna_id_cliente=5899429344503684
columna_id_compania=3647629530818436
columnas=[columna_Nombre,columna_Email,columna_Telefono,columna_Mensaje,columna_id_cliente,columna_id_compania]

#ayuda para crear rutas
app=Flask(__name__) 

datos=[]

#ruta para accesar aña formulario


@app.route('/',methods=["GET","POST"]) 

def index():
	comment_form= form.CommentForm(request.form) ## datos de form.html

	if request.method=='POST':
		nombres=comment_form.name.data
		correo=comment_form.email.data
		phone=comment_form.phone.data
		mensajes= comment_form.mensaje.data
		cliente=comment_form.idcliente.data
		compania=comment_form.idcompania.data
		datos=[nombres,correo,phone,mensajes,cliente,compania]
		Add_Rows(token_1,hoja_1,columnas,datos)


	return render_template('form.html',form=comment_form)


#validacion de archivo de arranque
if __name__ == '__main__':
	#app.run()
	app.run(debug=True)  #M modo de prueba para reiniciar a cada cambio


