import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from time import sleep

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.geometry('700x400+450+200')
        self.root.title('Componentes')
        self.crear_tabs()
    
    def crear_tabs(self):
        control_tab = ttk.Notebook(self.root)
        
        tab1 = ttk.Frame(control_tab)
        control_tab.add(tab1, text='Tabulador 1')
        self.crear_componentes_tab1(tab1)
        
        tab2 = ttk.LabelFrame(control_tab, text='Contenido')
        control_tab.add(tab2, text='Tabulador 2')
        self.componentes_tab2(tab2)
        
        tab3 = ttk.Frame(control_tab)
        control_tab.add(tab3, text='Tabulador 3')
        self.componentes_tab3(tab3)
        
        tab4 = ttk.LabelFrame(control_tab, text='Imagen')
        control_tab.add(tab4, text='Tabulador 4')
        self.componentes_tab4(tab4)
        
        tab5 = ttk.LabelFrame(control_tab, text='Progress Bar')
        control_tab.add(tab5, text='Tabulador 5')
        self.componentes_tab5(tab5)
        
        control_tab.pack(fill='both')
    
    def crear_componentes_tab1(self, tabulador):
        etiqueta1 = ttk.Label(tabulador, text='Nombre:')
        etiqueta1.grid(row=0, column=0, sticky=tk.E)
        
        self.entrada1 = ttk.Entry(tabulador, width=30)
        self.entrada1.grid(row=0, column=1, padx=5, pady=5)
        
        boton1 = ttk.Button(tabulador, text='Enviar', command=self.enviar)
        boton1.grid(row=1, column=0, columnspan=2)
    
    def enviar(self):
        messagebox.showinfo('Mensaje', f'Nombre: {self.entrada1.get()}')
        print(f'Mensaje: {self.entrada1.get()}')
    
    def componentes_tab2(self, tabulador2):
        contenido = """
        La tecnología ha avanzado a pasos agigantados en las últimas décadas, transformando la manera en que vivimos, trabajamos y nos comunicamos...
        """
        scroll = scrolledtext.ScrolledText(tabulador2, width=50, height=10, wrap=tk.WORD)
        scroll.insert(tk.INSERT, contenido)
        scroll.grid(row=0, column=0)
    
    def componentes_tab3(self, tabulador3):
        datos = [x+1 for x in range(10)]
        self.combobox = ttk.Combobox(tabulador3, width=15, values=datos)
        self.combobox.grid(row=0, column=0, padx=10, pady=10)
        self.combobox.current(0)
        
        boton2 = ttk.Button(tabulador3, text='Mostrar valor seleccionado', command=self.evento2)
        boton2.grid(row=0, column=2, padx=10, pady=10)
    
    def evento2(self):
        messagebox.showinfo('Valor seleccionado', f'Valor seleccionado: {self.combobox.get()}')
    
    def componentes_tab4(self, tabulador4):
        self.imagen = tk.PhotoImage(file='python-logo.png')
        boton3 = ttk.Button(tabulador4, image=self.imagen, command=self.evento3)
        boton3.grid(row=0, column=0)
    
    def evento3(self):
        messagebox.showinfo('Más info de la imagen', f'Nombre de la imagen: {self.imagen.cget("file")}')
    
    def componentes_tab5(self, tabulador5):
        self.barra_progreso = ttk.Progressbar(tabulador5, orient='horizontal', length=550)
        self.barra_progreso.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
        
        boton_inicio = ttk.Button(tabulador5, text='Ejecutar Barra de Progreso', command=self.evento4)
        boton_inicio.grid(row=1, column=0)
        
        boton_ciclo = ttk.Button(tabulador5, text='Ejecutar ciclo', command=self.evento5)
        boton_ciclo.grid(row=1, column=1)
        
        boton_detener = ttk.Button(tabulador5, text='Detener ejecucion', command=self.detener)
        boton_detener.grid(row=1, column=2)
        
        boton_despues = ttk.Button(tabulador5, text='Detener ejecucion después', command=self.despues)
        boton_despues.grid(row=1, column=3)
    
    def evento4(self):
        self.barra_progreso['maximum'] = 100
        for valor in range(101):
            sleep(0.05)
            self.barra_progreso['value'] = valor
            self.barra_progreso.update()
        self.barra_progreso['value'] = 0
    
    def evento5(self):
        self.barra_progreso.start()
    
    def detener(self):
        self.barra_progreso.stop()
    
    def despues(self):
        espera_ms = 1000
        self.root.after(espera_ms, self.barra_progreso.stop)

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
