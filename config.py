from datetime import datetime


# Obtiene la fecha actual
fecha_actual = datetime.now()

# Formatea la fecha en el formato deseado
fecha_formateada = fecha_actual.strftime("%Y-%m-%d")

url_prov = 'https://www.nacionalquiniela.com/quiniela-de-la-provincia.php?del-dia='
url_prov_completa = f"{url_prov}{fecha_formateada}"

url_nac = "https://www.nacionalquiniela.com/quiniela-nacional.php?del-dia="
url_nac_completa = f"{url_nac}{fecha_formateada}"

url_cordoba = "https://www.nacionalquiniela.com/quiniela-cordoba.php?del-dia="
url_cordoba_completa = f"{url_cordoba}{fecha_formateada}"


urls = {
    "provincia": url_prov_completa,
    "nacion": url_nac_completa,
    "cordoba": url_cordoba_completa
}

