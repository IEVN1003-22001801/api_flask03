from flask import Flask, render_template, request

from flask import make_response, jsonify
import json
from datetime import date
import forms
import pizza

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, Worldl"

@app.route("/pedido", methods=['GET', 'POST'])
def pedido():
    nombre = ""
    direccion = ""
    telefono = ""
    carrito = []
    ventas = []
    mensaje = ""
    total = 0
    total_dia = 0

    # Obtener cookies
    carrito_str = request.cookies.get('carrito')
    ventas_str = request.cookies.get('cookie_ventas')
    
    if carrito_str:
        carrito = json.loads(carrito_str)
    if ventas_str:
        ventas = json.loads(ventas_str)

    pedido_clase = pizza.PedidoForm(request.form)

    if request.method == 'POST' and pedido_clase.validate():
        nombre = pedido_clase.nombre.data
        direccion = pedido_clase.direccion.data
        telefono = pedido_clase.telefono.data
        tamanio = pedido_clase.tamanio.data
        num_pizzas = pedido_clase.num_pizzas.data

        ingredientes = request.form.getlist('ingredientes')

        if 'agregar' in request.form:

            if tamanio == 'Chica':
                precio_base = 40
            elif tamanio == 'Mediana':
                precio_base = 80
            else:  # Grande
                precio_base = 120


            precio_ing = 0
            for ing in ingredientes:
                precio_ing += 10
            
            subtotal = (precio_base + precio_ing) * num_pizzas

            pizza_dic = {
                "tamanio": tamanio,
                "ingredientes": ingredientes,
                "num_pizzas": num_pizzas,
                "subtotal": subtotal
            }
            carrito.append(pizza_dic)

        elif 'quitar' in request.form:

            index = request.form.get('index')
            if index and 0 <= int(index) < len(carrito):
                carrito.pop(int(index))

        elif 'terminar' in request.form:
            if len(carrito) > 0:

                total = 0
                for p in carrito:
                    total += p['subtotal']
                

                venta = {
                    "nombre": nombre,
                    "direccion": direccion,
                    "telefono": telefono,
                    "fecha": date.today().strftime("%d-%m-%Y"),
                    "total": total
                }
                ventas.append(venta)
                carrito = [] 


    total_dia = 0
    for v in ventas:
        total_dia += v['total']

    response = make_response(render_template(
        "pedido.html",
        form=pedido_clase,
        nombre=nombre,
        direccion=direccion,
        telefono=telefono,
        carrito=carrito,
        ventas=ventas,
        total_dia=total_dia,
        mensaje=mensaje
    ))

    response.set_cookie('carrito', json.dumps(carrito))
    response.set_cookie('cookie_ventas', json.dumps(ventas))
    return response

@app.route("/ventas_totales")
def ventas_totales():
    ventas_str = request.cookies.get('cookie_ventas')
    if not ventas_str:
        return "No hay ventas registradas"
    
    ventas = json.loads(ventas_str)
    return jsonify(ventas)

@app.route("/Alumnos", methods=['GET','POST'])
def alumnos():
    mat=0
    nom=""
    ape=""
    em=""
    estudiantes=[] #Listas
    tem=[]
    datos={} #Diccionarios


    alumnos_clase=forms.UserForm(request.form)
    if request.method=='POST' and alumnos_clase.validate():
        mat=alumnos_clase.matricula.data
        nom=alumnos_clase.nombre.data
        ape=alumnos_clase.apellido.data
        em=alumnos_clase.correo.data
        datos={"matricula":mat,"nombre":nom,"apellido":ape,"correo":em}

        datos_str=request.cookies.get('estudiante')
        if not datos_str:
            return "No hay cookie"
        tem=json.loads(datos_str)
        estudiantes=tem
        print(type(estudiantes))
        estudiantes.append(datos)

    response=make_response(render_template('Alumnos.html', form=alumnos_clase, mat=mat, nom=nom, ape=ape, em=em))

    response.set_cookie('estudiante',json.dumps(estudiantes))

    return response


@app.route("/get_cookie")
def get_cookie():
    datos_str=request.cookies.get('estudiante')
    if not datos_str:
        return "No hay cookie"
    datos=json.loads(datos_str)

    return jsonify(datos)

@app.route('/index')
def index():
    titulo="IEVN1003 - PWA"
    listado=["Opera 1","Opera 2", "Opera 3", "Opera 4"]
    return render_template('index.html', titulo=titulo, listado=listado) 


@app.route('/operas',methods=['GET','POST'])
def operas():

    if request.method=='POST':
        x1=request.form.get('x1')
        x2=request.form.get('x2')
        resultado=x1+x2
        return render_template('operas.html', resultado=resultado)


    return render_template('operas.html') 
    

@app.route('/distancia')
def distancia():
    return render_template('distancia.html') 


@app.route('/about')
def about():
    return "<h1>This is the about page.<h1>"

@app.route('/user/<string:user>')
def user(user):
    return "Hola" + user

@app.route('/numero/<int:n>')
def numero(n):
    return "Numero: {}".format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return "ID: {} nombre {}".format(id,username)

@app.route("/suma/<float:n1>/<float:n2>")
def func(n1,n2):
    return "La suma es: {}".format(n1+n2)

@app.route("/prueba")
def prueba():
    return '''
    <h1>Prueba de HTML</h1>
    <p>Esto es un parrafo</p>
    <ul>
        <li>Elemento 1</li>
        <li>Elemento 2</li>
        <li>Elemento 3</li>
    </ul>

    '''


if __name__ == '__main__':
    app.run(debug=True)