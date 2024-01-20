from bs4 import BeautifulSoup

import requests
from config import urls

def obtener_quiniela(url):
    # Realiza la solicitud HTTP a la página
    response = requests.get(url)
    # Verifica que la solicitud sea exitosa (código de estado 200)
    if response.status_code == 200:
        # Parsea el contenido HTML de la página con BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Realiza operaciones de scraping, por ejemplo, imprimir los títulos de los enlaces
        tablas = soup.find_all('table', class_="table table-bordered table-condensed")

        quiniela = []

        # Itera sobre cada tabla encontrada
        for tabla in tablas:

            encabezado = tabla.find_all('th')

            nombre_quiniela = encabezado[0].text.lower()

            cabeza = encabezado[1].text

            cuerpo = tabla.find_all('tbody')

            # Encuentra las filas con los datos de los resultados
            filas = cuerpo[0].find_all('tr')
            resultados = []
            for fila in filas:
                    datos = fila.find_all('td')
                    if(len(datos) >=2):
                        resultados.append(datos[1].text)
            
            quiniela.append({
                 nombre_quiniela : resultados
            })

        return quiniela
    else:
        print(f"Error al realizar la solicitud. Código de estado: {response.status_code}")
        return []
    
    

