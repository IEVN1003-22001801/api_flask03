from wtforms import Form, StringField, RadioField, IntegerField, validators

class PedidoForm(Form):
    nombre = StringField("Nombre", [validators.DataRequired(message="Campo obligatorio")])
    direccion = StringField("Dirección", [validators.DataRequired(message="Campo obligatorio")])
    telefono = StringField("Teléfono", [validators.DataRequired(message="Campo obligatorio")])
    tamanio = RadioField("Tamaño Pizza", choices=[
        ('Chica', 'Chica $40'),
        ('Mediana', 'Mediana $80'), 
        ('Grande', 'Grande $120')
    ], validators=[validators.DataRequired(message="Selecciona un tamaño")])
    num_pizzas = IntegerField("Número de pizzas", [
        validators.DataRequired(message="Campo obligatorio"), 
        validators.NumberRange(min=1, message="Mínimo 1pizza")
])