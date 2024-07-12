import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.geometry("300x130")
ventana.title("Login")

entrada1_var = tk.StringVar(value="")
entrada1 = ttk.Entry(ventana, width=20, textvariable=entrada1_var)
entrada1.grid(row=0, column=1, padx=2, pady=5)

entrada2_var = tk.StringVar(value="")
entrada2 = ttk.Entry(ventana, width=20, textvariable=entrada2_var, show="*")
entrada2.grid(row=1, column=1, padx=2, pady=5)

etiqueta1 = tk.Label(ventana, text="User:")
etiqueta1.grid(row=0, column=0, padx=2, pady=5)

etiqueta2 = tk.Label(ventana, text="Password:")
etiqueta2.grid(row=1, column=0, padx=2, pady=5)


def login():

    print(
        f"""Credenciales de Usuario logeado:
User: {entrada1_var.get()}
Password: {entrada2_var.get()}  
          """
    )
    mensaje1 = entrada1_var.get()
    mensaje2 = entrada2_var.get()
    messagebox.showinfo("Datos Login", f"Usuario: {mensaje1}, Password: {mensaje2}")


boton1 = ttk.Button(ventana, text="Login", command=login)
boton1.grid(row=2, column=0, columnspan=2, padx=45, pady=12)

ventana.mainloop()
