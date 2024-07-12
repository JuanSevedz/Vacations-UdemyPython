import tkinter as tk
from tkinter import ttk, messagebox, Menu
import sys

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de componentes')

entrada1 = ttk.Entry(ventana, width=30)
entrada1.grid(row=0, column=0)

etiqueta1 = tk.Label(ventana, text='Aquí se mostrará el contenido de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)

def enviar():
    etiqueta1.config(text=entrada1.get())
    mensaje1= entrada1.get()
    
    if mensaje1:
        messagebox.showinfo('Mensaje Informativo', mensaje1 + ' Informativo')

def salir():
    ventana.quit()
    ventana.destroy()
    print('Salimos de la aplicacion')
    sys.exit()
        
def crear_menu():
    
    # Configuracion del menu
    menu_principal = Menu(ventana)
    # tearoff = False
    submenu_archivo = Menu(menu_principal, tearoff=0)
    # Agregamos una nueva opcion
    submenu_archivo.add_command(label='Nuevo')
    submenu_archivo.add_separator()
    submenu_archivo.add_command(label='Salir', command=salir)
    
    # Submenu de 'Ayuda'
    submenu_submenu = Menu(menu_principal, tearoff=0)
    submenu_submenu.add_command(label='Acerca de')
    
    
    # Agregamos el submenu al menu
    menu_principal.add_cascade(menu=submenu_archivo, label='Archivo')
    
    menu_principal.add_cascade(menu=submenu_submenu, label='Ayuda')
    # MOstrar el menu el la ventana del programa
    ventana.config(menu=menu_principal)
    
    
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

crear_menu()

ventana.mainloop()