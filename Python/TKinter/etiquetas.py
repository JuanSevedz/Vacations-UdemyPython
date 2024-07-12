import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de componentes')

# Definimos una variable
in_var1 = tk.StringVar(value= 'Valor por default')
entrada1 = ttk.Entry(ventana, width=30, textvariable=in_var1)
entrada1.grid(row=0, column=0)

# Etiqueta (label)
etiqueta1 = tk.Label(ventana, text='Aquí se mostrará el contenido de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)

def enviar():
    
    # Modificamos el texto del Label
    etiqueta1.config(text=in_var1.get())
    
    
    
    
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)


ventana.mainloop()