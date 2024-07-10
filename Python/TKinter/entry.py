import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de "Entry"')

# entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, show='*')
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.NORMAL)
entrada1.grid(row=0, column=0)
entrada1.insert(0,'Introduce una cadena')
entrada1.insert(tk.END, '.')
# entrada1.config(state='readonly')

def evento1():
    print(entrada1.get())
    boton1.config(text=entrada1.get())
    # Eliminar el contenido
    # entrada1.delete(0, tk.END)
    entrada1.select_range(0, tk.END)
    entrada1.focus()
    
    
boton1 = ttk.Button(ventana, text='Enviar', command=evento1)
boton1.grid(row=0, column=1)


ventana.mainloop()