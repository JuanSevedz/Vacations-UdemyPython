import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')

# Configurar el Grid
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=5)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)


def evento1():
    boton1.config(text='Botón 1 presionado')

def evento2():
    # boton2.config(text='Botón 2 presionado')
    pass
def evento3():
    # boton3.config(text='Se presionó el boton 3')
    pass
def evento4():
    # boton4.config(text='Se presionó el boton 4', fg='Blue', relief=tk.GROOVE, bg='yellow')
    pass 
boton1 = ttk.Button(ventana, text= 'Botón 1', command=evento1)
boton1.grid(row=0, column=0, sticky='NSWE', padx=40, pady=30, ipadx=20, ipady=50, columnspan=2, rowspan=2)

# boton2 = ttk.Button(ventana, text='Botón 2', command=evento2)
# boton2.grid(row=1, column=0, sticky='NSWE')

# boton3 = ttk.Button(ventana, text='Botón 3', command=evento3)
# boton3.grid(row=0, column=1, sticky='NSWE')

# boton4 = tk.Button(ventana, text='Botón 4', command=evento4)
# boton4.grid(row=1, column=1, sticky='NSWE')

ventana.mainloop()