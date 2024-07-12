import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de "Entry"')

# entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, show='*')

# Definimos una variable
in_var1 = tk.StringVar(value= 'Valor por default')

entrada1 = ttk.Entry(ventana, width=30, textvariable=in_var1)
entrada1.grid(row=0, column=0)
# entrada1.insert(0,'Introduce una cadena')
# entrada1.insert(tk.END, '.')
# entrada1.config(state='readonly')

def evento1():
    # print(entrada1.get())
    # boton1.config(text=entrada1.get())
    # Eliminar el contenido
    # entrada1.delete(0, tk.END)
    # entrada1.select_range(0, tk.END)
    # entrada1.focus()
    
    # Se recupera la informacion a partir de 'in_var1'
    boton1.config(text=in_var1.get())
    # Modificar usando la variable
    in_var1.set('Cambio....')
    # Recuperar informacion
    print(entrada1.get())
    
    
boton1 = ttk.Button(ventana, text='Enviar', command=evento1)
boton1.grid(row=0, column=1)


ventana.mainloop()