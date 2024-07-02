from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

url = 'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/plain',
}

req = Request(url, headers=headers)

try:
    with urlopen(req) as mensaje:
        contenido = mensaje.read().decode('utf-8')
        #print(contenido)
except HTTPError as e:
    print(f"HTTP error occurred: {e}")
except URLError as e:
    print(f"Failed to reach the server: {e}")


with open('GlobalMentoring.txt', 'w', encoding='utf-8')as  archivo:
    archivo.write(contenido)

try:
    palabras = []
    with urlopen(req) as mensaje:
        for linea in mensaje:
            palabras_por_linea = linea.decode('utf-8').split()
            for palabra in palabras_por_linea:
                palabras.append(palabra)
    #print(palabras)
except HTTPError as e:
    print(f"HTTP error occurred: {e}")
except URLError as e:
    print(f"Failed to reach the server: {e}")


try:
    palabras = []
    with urlopen(req) as mensaje:
        contenido = mensaje.read().decode('utf-8')
    print(f'Aparece: {contenido.count('Universidad')} veces')
    #print(contenido.upper())
    #print(contenido.lower())
    mensaje = 'Hola mundo'
    print(mensaje.lower().islower())
    print(mensaje.upper().isupper())

    #Alinear cadenas
    titulo = 'Sitio web de GlobalMentory.com.mx'
    print(len(titulo))
    #centrado
    print(titulo.center(50,'*'))
    print(len(titulo.center(50,'*')))
    print(titulo.center(len(titulo)+10,'-'))
    # A la izquierda
    print(titulo.ljust(50, '-'))
    # A la derecha
    print(titulo.rjust(50,'-'))
    #Reemplazar contenido en unstring
    print(titulo.replace(' ','-'))
    #Eliminar caracteres
    titulo = ' *** GlobalMentory.co *** '
    print(f'Cdena original: {titulo}, {len(titulo)}')
    print(f'Nueva cadena: {titulo.strip()}, {len(titulo.strip())}')
    titulo = '***GlobalMentory.co***'.strip('*')
    print(f'Cadena modificada: {titulo}')
    titulo = '***GlobalMentory.co***'.lstrip('*')
    print(titulo)
    titulo = '***GlobalMentory.co***'.rstrip('*')
    print(titulo)
    titulo = ' *** GlobalMentory.co *** '.strip().strip('*').strip()
    print(titulo)


except HTTPError as e:
    print(f"HTTP error occurred: {e}")
except URLError as e:
    print(f"Failed to reach the server: {e}")
