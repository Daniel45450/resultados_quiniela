@app.route('/revisar_jugada', methods=['POST'])
def revisar_jugada():

    if request.method != 'POST':
        return render_template('index.html')
    
    numero = request.form.get('numero')
    opciones = request.form.getlist('opcion')

    numero_jugado = str(numero)
    cifras = get_cadenas(numero_jugado)

    dos_cifras = '1' in opciones
    tres_cifras = '2' in opciones

    quniela_provincial = obtener_quiniela(urls.get('provincia')) if 'provincia' in opciones else []
    quiniela_nacional = obtener_quiniela(urls.get('nacion')) if 'nacion' in opciones else []
    quiniela_cordoba = obtener_quiniela(urls.get('cordoba')) if 'cordoba' in opciones else []

    quinielas = {
        'provincia': quniela_provincial,
        'nacional' : quiniela_nacional,
        'cordoba'  : quiniela_cordoba
    }
    premios_globales = {}
    for quiniela, listas_resultados in quinielas.items():
        b = []
        for lista_resultado in listas_resultados:
            for horario, resultados in lista_resultado.items():
                premios = {}
                premio = []
                if resultados:
                    print(resultados)
                    if len(numero_jugado) >= 2 and dos_cifras:
                        print('verificando a las 2 cifras')
                        premio = verificar_premios(cifras[1], resultados)
                        premios.update({
                            'dos_cifras': premio
                        })
                    if len(numero_jugado) >= 3 and tres_cifras :
                        print('verificando a las 3 cifras')
                        premio = verificar_premios(cifras[2], resultados)
                        premios.update({
                            'tres_cifras': premio
                        })
                    if len(numero_jugado) >= 4:
                        print('verificando a las 4 cifras')
                        premio = verificar_premios(cifras[3], resultados)
                        premios.update({
                            'cuatro_cifras': premio
                        })

                a = {horario: premios}
                b.append(a)
            premios_globales.update({
                quiniela: b
            })

    print(premios_globales)
    # Puedes redirigir a otra página o renderizar un nuevo template
    return render_template('index.html', premios_globales = premios_globales)
