# Importamos el módulo de tkinter
import tkinter as tk
# Importamos el módulo del tema de tkinter
from tkinter import ttk

# Creamos un objeto usando la clase Tk
ventana = tk.Tk()

# Establecemos el ícono de la ventana
# ventana.iconbitmap('prueba.ico')

# Modificamos el tamaño de la ventana (pixeles)
ventana.geometry('600x400')

# Cambiamos el nombre de la ventana
ventana.title('Hola Mundo')

# Evento del boton
def evento_click():
    boton1.config(text='Boton presionado')
    print('Ejecucion del boton')
    
    boton2 = ttk.Button(ventana, text='Nuevo boton')
    boton2.pack()
    
# Creamos un boton (widget), el objeto padre es ventana
boton1 = ttk.Button(ventana, text='Dar click', command=evento_click)


# Utilizamos el pack layout manager para mostrar el botón en la ventana
boton1.pack()

# Iniciamos la ventana (esta línea la ejecutamos al final)
# Si la ejecutamos antes, no se muestran los cambios anteriores
ventana.mainloop()
