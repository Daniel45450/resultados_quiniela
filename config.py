from datetime import datetime, timedelta
import locale

# Obtiene la fecha actual
fecha_actual = datetime.now()

fecha_valida = fecha_actual

if fecha_actual.weekday() == 6:
    fecha_valida = fecha_actual - timedelta(days=1)


# Formatea la fecha en el formato deseado
fecha_formateada = fecha_valida.strftime("%Y-%m-%d")

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
