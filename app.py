from flask import Flask, url_for, request, render_template
from flask import url_for
from scrap import obtener_quiniela
from config import urls, fecha_valida
from datetime import datetime


app = Flask("App Quiniela")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiniela/<id_quiniela>')
def mostrar_resultado(id_quiniela):
    resultados = obtener_quiniela(urls.get(id_quiniela))
    quiniela = {
        'resultados' : resultados,
        'nombre': id_quiniela,
        'fecha' : fecha_valida.strftime('%d/%m/%Y')
    }
    return render_template('index_resultados.html', quiniela = quiniela)

@app.route('/revisar_jugada', methods=['POST'])
def revisar_jugada():

    if request.method != 'POST':
        return render_template('index.html')
    
    numero = request.form.get('numero')
    opciones = request.form.getlist('opcion')


    numero_jugado = str(numero)


    quniela_provincial = obtener_quiniela(urls.get('provincia')) if 'provincia' in opciones else []
    quiniela_nacional = obtener_quiniela(urls.get('nacion')) if 'nacion' in opciones else []
    quiniela_cordoba = obtener_quiniela(urls.get('cordoba')) if 'cordoba' in opciones else []

    quinielas = {
        'provincia': quniela_provincial,
        'nacional' : quiniela_nacional,
        'cordoba'  : quiniela_cordoba
    }

    return render_template('index.html', quinielas = quinielas, numero_jugado = numero_jugado, opciones = opciones, verificar_premios= verificar_premios, get_cadenas = get_cadenas)



def verificar_premios(numero_jugado, resultados):
    
    premios = []
    for indice, valor in enumerate(resultados):
        aux = get_cadenas(valor)
        for i in aux:
            if i == numero_jugado:
                premios.append(
                    {indice:valor}
                )
    return premios

def get_cadenas(palabra):
    cadenas = []
    for c in reversed(palabra):
        if not cadenas:
            cadenas.append(c)
        else:
            cadenas.append(c + cadenas[len(cadenas) -1])
    return cadenas 


