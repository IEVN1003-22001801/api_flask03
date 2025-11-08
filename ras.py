import math
from flask import Flask, render_template, request

# Inicialización de la aplicación Flask
app = Flask(__name__)

# --- Funciones de Cálculo de Área ---

def calcular_area_triangulo(base, altura):
    """Área del triángulo: 0.5 * base * altura"""
    return 0.5 * base * altura

def calcular_area_rectangulo(longitud, anchura):
    """Área del rectángulo: longitud * anchura"""
    return longitud * anchura

def calcular_area_circulo(radio):
    """Área del círculo: π * radio²"""
    return math.pi * (radio ** 2)

def calcular_area_pentagono(lado):
    """
    Área del pentágono regular: 
    Area = (5 * lado^2) / (4 * tan(π/5))
    """
    return (5 * (lado ** 2)) / (4 * math.tan(math.pi / 5))

# --- Ruta Principal ---

@app.route('/', methods=['GET', 'POST'])
def index():
    # Inicializamos las variables que se pasan a la plantilla
    resultado = None
    forma_seleccionada = None

    # Si el formulario fue enviado (POST)
    if request.method == 'POST':
        # Captura la forma seleccionada (siempre presente en POST)
        forma_seleccionada = request.form.get('forma')
        
        # Solo intentamos el cálculo si los campos de dimensión están presentes
        try:
            area = 0.0
            
            if forma_seleccionada == 'triangulo':
                base = request.form.get('base')
                altura = request.form.get('altura')
                
                if base and altura: # Se verifica que ambos valores no sean None ni cadenas vacías
                    base = float(base)
                    altura = float(altura)
                    area = calcular_area_triangulo(base, altura)
                    resultado = f"El área del Triángulo (Base: {base}, Altura: {altura}) es: {area:.2f}"
                
            elif forma_seleccionada == 'rectangulo':
                longitud = request.form.get('longitud')
                anchura = request.form.get('anchura')
                
                if longitud and anchura:
                    longitud = float(longitud)
                    anchura = float(anchura)
                    area = calcular_area_rectangulo(longitud, anchura)
                    resultado = f"El área del Rectángulo (Largo: {longitud}, Ancho: {anchura}) es: {area:.2f}"
                
            elif forma_seleccionada == 'circulo':
                radio = request.form.get('radio')
                
                if radio:
                    radio = float(radio)
                    area = calcular_area_circulo(radio)
                    resultado = f"El área del Círculo (Radio: {radio}) es: {area:.2f}"
                
            elif forma_seleccionada == 'pentagono':
                lado = request.form.get('lado')
                
                if lado:
                    lado = float(lado)
                    area = calcular_area_pentagono(lado)
                    resultado = f"El área del Pentágono Regular (Lado: {lado}) es: {area:.2f}"
            
        except (ValueError, TypeError) as e:
            # Este bloque se activa si el usuario ingresa texto en lugar de números.
            resultado = "Error: Por favor, asegúrate de que todas las dimensiones ingresadas sean números válidos."
            
    # Renderiza la plantilla figuras.html con los resultados y la forma actual
    # Si fue un POST de selección, forma_seleccionada tendrá un valor (ej: 'triangulo')
    # pero resultado será None, por lo que se mostrarán los campos de entrada.
    return render_template('figuras.html', resultado=resultado, forma_seleccionada=forma_seleccionada)

# Configuración para ejecutar la aplicación
if __name__ == '__main__':
    # Ejecutamos la aplicación en modo debug
    app.run(debug=True)