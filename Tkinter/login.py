import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Login')
ventana.configure(background='#1d2d44')

#Grid de la app
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

# Creamos estilo para la app
estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure(ventana, background='#1d2d44', foreground='white',
                  fieldbackground='black')
estilos.configure('TButton', background='#005f73')
estilos.map('TButton', background=[('active', '#0a9396')])

# Frame o contenedor
frame = ttk.Frame(ventana)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=3)

# Titulo
etiqueta = ttk.Label(frame, text='Login', font=('Arial', 20))
etiqueta.grid(row=0, column=0, columnspan=2)


# Input De Usuario
usuario_etiqueta = ttk.Label(frame, text='Usuario: ')
usuario_etiqueta.grid(row=1,column=0, sticky=tk.W, padx=5, pady=5)

usuario_caja = ttk.Entry(frame)
usuario_caja.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

# Input De Password
password_etiqueta = ttk.Label(frame, text='Password: ')
password_etiqueta.grid(row=2,column=0, sticky=tk.W, padx=5, pady=5)

password_caja = ttk.Entry(frame, show='*')
password_caja.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

# Boton
login_boton = ttk.Button(frame, text='Enviar')
login_boton.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

def validar(event):
    usuario = usuario_caja.get()
    password = password_caja.get()
    if usuario == 'root' and password == 'admin':
        showinfo(title='login', message='Datos correctos')
        print('Valores correctos')
    else:
        showerror(title='Login', message='Datos incorrectos')
        print('valores incorrectos')

# Asociacion de eventos al boton
login_boton.bind('<Return>', validar) # Presionar enter
login_boton.bind('<Button-1>', validar) #Click izquierdo mouse




frame.grid(row=0, column=0)
ventana.mainloop()