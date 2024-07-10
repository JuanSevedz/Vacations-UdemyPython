import urllib.request
import json

# URL del JSON
url = 'http://globalmentoring.com.mx/api/clima.json'

# Crear la petición con los cabeceros necesarios
peticion = urllib.request.Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

# Realizar la petición y obtener la respuesta
respuesta = urllib.request.urlopen(peticion)

cuerpo_respuesta = respuesta.read()


# Procesar la respuesta JSON
json_respuesta = json.loads(cuerpo_respuesta.decode("utf-8"))

# Extraer la descripción y la temperatura máxima
descripcion = json_respuesta['clima'][0]['descripcion']
temp_min = json_respuesta['principal']['temp_min']
temp_max = json_respuesta['principal']['temp_max']

# Imprimir los resultados
print(f"Descripción: {descripcion}")
print(f"Temperatura Minima: {temp_min}°C")
print(f'Temperatura MAX: {temp_max}° C')
