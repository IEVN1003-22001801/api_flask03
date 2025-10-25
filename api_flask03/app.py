from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World :)"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/operas')
def operas():
    return render_template('operas.html')

@app.route('/distancia')
def distancia():
    return render_template('distancia.html')



@app.route('/about')
def about():
    return "<h1>This is the about page.<h1>"

@app.route("/user/<string:user>")
def user(user):
    return "Hola "+ user

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return "ID: {}".format(id,username)

@app.route("/suma/<float:n1>/<float:n2>")
def funt(n1,n2):
    return "La suma es: {}".format(n1+n2)

@app.route("/prueba")
def prueba():
    return """
    <h1>Prueba de HTML</h1>
    <p>Esto es un parrafo</p>
    <ul>
    <li>Elemento 1</li>
    <li>Elemento 2</li>
    <li>Elemento 3</li>
    </ul>
        """
if __name__ == '__main__':
    app.run(debug=True)