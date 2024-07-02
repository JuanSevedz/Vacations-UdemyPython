# Concatenacion

message = 'Hola ' 'Mundo'
variable = 'Hola' 'Mundo' + message
message += 'University' 'Python'
#print(message)
#help(str.capitalize)
#help(str.capitalize)

message1 = 'hola mundo'
message2 = message1.capitalize()
print(f'Mensaje 1: {message1}, Id: {hex(id(message1))} ')
print(f'Mensaje 2: {message2}, ID: {hex(id(message2))}' )
message1 += ' Adios'
print(f'Mensaje 1: {message1}, Id: {hex(id(message1))} ')

# Method Join
tupla_str = ('Hola', 'Mundo', 'Universidad', 'Python')
message3 = ' '.join(tupla_str)
print(f'Mensaje: {message3}, Id: {hex(id(message3))} ')

list_cursos = ['Java', 'Python', 'Spring']
message4 = ', '.join(list_cursos)
print(f'Mensaje : {message4}, Id: {hex(id(message4))} ')

cadena = 'Holamundo'
mensaje = '.'.join(cadena)
print(f'{mensaje}')

diccionario = {'Nombre':'Juan', 'apellido':'Perez', 'edad':'18'}
mensaje_dic = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print(f'Llaves: {mensaje_dic} de tipo: {type(mensaje_dic)}, valores: {valores} de tipo: {type(valores)} ')

# Split method
cursos = 'Java Python JavaScript Angular Spring'
lista_cursos = cursos.split()
print(f'Lisa cursos: {lista_cursos}')

cursos_separados_coma = 'Java,Python,Angular,JavaScript,Spring'
lista_cursos = cursos_separados_coma.split(',')#Se especifica el parametro que esta separando el mensaje
print(f'Lisa cursos: {lista_cursos}')
print(len(lista_cursos))

lista_cursos = cursos_separados_coma.split(',', 7)
print(f'Lisa cursos: {lista_cursos}')
print(len(lista_cursos))

#Dar formato a un str
nombre = 'Juan'
edad = 18
mensaje_con_formato = 'Mi nombre es %s y tengo %s años'%(nombre, edad)
print(f'Mensaje con formato: {mensaje_con_formato}')
#opcion 1
persona = ('Karla', 'Gomez', 50000)
mensaje_con_formato = 'Hola %s %s.Tu sueldo es: %.2f'%(persona)
print(f'{mensaje_con_formato}')
#opcion2
mensaje_con_formato = 'Hola %s %s.Tu sueldo es: %.2f'
print(mensaje_con_formato%persona)

#Usando format
#Opcion 1
nombre = 'Felipe'
edad = 15
sueldo = 12298
mensaje_con_formato = 'Nombre {} edad {} sueldo {:.2f}'.format(nombre, edad, sueldo)
print(mensaje_con_formato)
#Opcion 2
mensaje = 'Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre, edad, sueldo)
print(mensaje)
#Opcion 3
mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}'.format(n=nombre, s= sueldo, e= edad)
print(mensaje)

diccionario = {'nombre': 'Ivan', 'edad': '25', 'sueldo':121212}
mensaje = 'Nombre {persona[nombre]} Edad {dic[edad]} Sueldo {dic[sueldo]:.2f}'.format(persona=diccionario, dic=diccionario)
print(f'Mensaje en diccionario: {mensaje}')

#Usando f''
nombre = 'Felipe'
edad = 15
sueldo = 12298
mensaje_con_formato = f'Nombre {nombre} edad {edad} sueldo {sueldo:.2f}'
print(mensaje_con_formato)


#Multiplicacion de cadenas
resultado = 5*'Hola'
print(f'Resultado: {resultado}')
#tuplas
resultado = 5 * ('Hola', 10 )
print(f'Resultado: {resultado}')
#Listas
resultado = 10*[0]
print(f'Resultado: {resultado}, largo: {len(resultado)}')

#Caracteres de escape
resultado = 'Hola \'Mundo'
print(resultado)
resultado = 'Se va a eliminar el punto.\b'
print(resultado)
#caracter \
resultado = 'c:\\directorio\\juan'
print(f'Resultado: {resultado}')
#Raw string
resultado = r'Cadena con \n salto de linea' #Para invalidar saltos de linea
print(f'Resultado: {resultado}')

#Caracteres Unicode
print('Hola\u0020mundo')
print('Notacion simple:', ' \u0041')
print('Notacon extendida:', '\U00000041')
print('NOtacion en hexadecimal:','\x41')

# caracteres bytes
caracteres_en_bytes = b'Hola Mundo'
print(caracteres_en_bytes)

mensaje = b'Universidad Python'
print(mensaje[1])
print(chr(mensaje[1]))

lista_caracteres = mensaje.split()
print(lista_caracteres)

# Convertir str a bytes
string = 'Programación con Python'
print('string original:', string)
bytes = string.encode('UTF-8')
print('bytes codificado:', bytes)
# Convertir bytes a str
string2 = bytes.decode('UTF-8')
print('string decodificado:', string2)
print(string == string2)