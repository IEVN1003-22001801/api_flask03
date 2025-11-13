from wtforms import Form
from wtforms import StringField, FloatField, EmailField, PasswordField, IntegerField
from wtforms import validators

class UserForm(Form):
    matricula=IntegerField('Matricula',
    [validators.DataRequired(message="La matricula es obligatoria")])

    nombre=StringField('Nombre',
    [validators.DataRequired(message="El campo es requerido")])

    apellido=StringField('Apellido',
    [validators.DataRequired(message="El campo es requerido")])

    correo=EmailField('Correo',
    [validators.DataRequired(message="Ingrese Correo Valido")])

class FigurasForm(Form):
    
    valor1 = FloatField('valor 1', [validators.DataRequired(message="Valor 1 si es necesari")])
    
    valor2 = FloatField('valor 2?', [validators.DataRequired(message="Valor 2 no es necesario")])