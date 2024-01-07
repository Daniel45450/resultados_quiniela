from flask import Flask, url_for, request, render_template
from flask import url_for
from scrap import obtener_quiniela

app = Flask("App Quiniela")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/revisar_jugada', methods=['POST'])
def revisar_jugada():
    numero = request.form.get('numero')
    opciones = request.form.getlist('opcion')

    print(request.form)

    # Haz lo que necesites con los datos del formulario
    print(f'Número: {numero}, Opciones: {opciones}')

    # Puedes redirigir a otra página o renderizar un nuevo template
    return 'Formulario procesado con éxito!'
