from wtforms import Form
from wtforms import StringField,TextField
from wtforms.fields.html5 import EmailField


class CommentForm(Form):
	name=StringField('name')
	email=EmailField('email')
	phone=StringField('phone')
	mensaje=StringField('mensaje')
	idcliente=StringField('idcliente')
	idcompania=StringField('idcompania')