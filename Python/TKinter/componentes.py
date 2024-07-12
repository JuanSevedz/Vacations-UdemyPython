import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from time import sleep

ventana = tk.Tk()
ventana.geometry('700x400+450+200')
ventana.title('Componentes')

def crear_componentes_tab1(tabulador):
    
    # Asi se agregan elementos...
    # 1.Etiqueta
    etiqueta1 = ttk.Label(tabulador, text='Nombre:')
    etiqueta1.grid(row=0, column=0, sticky=tk.E)
    # 2.Componente de entrada
    entrada1 = ttk.Entry(tabulador, width=30)
    entrada1.grid(row=0, column=1, padx=5, pady=5)        
    # 3.Botón
    def enviar():
        messagebox.showinfo('Mensaje', f'Nombre: {entrada1.get()}')
        print(f'Mensaje: {entrada1.get()}')
        
    boton1 = ttk.Button(tabulador, text='Enviar', command=enviar)
    boton1.grid(row=1, column=0, columnspan=2)
    
def componentes_tab2(tabulador2):
    
    contenido = """
La tecnología ha avanzado a pasos agigantados en las últimas décadas, transformando la manera en que vivimos, trabajamos y nos comunicamos. Desde la invención de la computadora hasta la llegada de Internet y los dispositivos móviles, los cambios han sido asombrosos y continúan evolucionando rápidamente. En el mundo de hoy, la tecnología es omnipresente y afecta casi todos los aspectos de nuestras vidas.

Uno de los avances más significativos en la tecnología ha sido el desarrollo de Internet. Este ha revolucionado la forma en que accedemos a la información, interactuamos con otras personas y realizamos negocios. Antes de Internet, la comunicación a larga distancia se limitaba a las cartas y las llamadas telefónicas, y el acceso a la información requería visitas a bibliotecas o consultas en enciclopedias físicas. Hoy en día, con un clic, podemos conectarnos con personas en cualquier parte del mundo, acceder a vastos recursos de información y realizar transacciones comerciales en línea.

La aparición de los dispositivos móviles ha llevado la conectividad a un nivel completamente nuevo. Los teléfonos inteligentes y las tabletas nos permiten estar conectados en todo momento y en cualquier lugar. No solo usamos estos dispositivos para hacer llamadas o enviar mensajes, sino que también los utilizamos para navegar por Internet, tomar fotografías, jugar, y gestionar nuestras vidas diarias. Las aplicaciones móviles han transformado industrias enteras, desde el entretenimiento y la educación hasta la banca y la salud.

Otro avance importante en la tecnología ha sido el desarrollo de la inteligencia artificial (IA). La IA está cambiando la forma en que interactuamos con las máquinas y está creando nuevas oportunidades y desafíos en una variedad de campos. Desde asistentes virtuales como Siri y Alexa hasta vehículos autónomos y sistemas de recomendación, la IA está haciendo que las máquinas sean más inteligentes y capaces de realizar tareas que antes eran exclusivas de los seres humanos. Sin embargo, este avance también plantea preguntas sobre el futuro del trabajo y la ética de las decisiones automatizadas.

La tecnología también ha tenido un impacto significativo en la medicina. Los avances en las tecnologías médicas han mejorado los diagnósticos, los tratamientos y la atención al paciente. Las imágenes médicas, la telemedicina y los dispositivos portátiles de monitoreo de la salud son solo algunos ejemplos de cómo la tecnología está transformando la medicina. Estos avances no solo están salvando vidas, sino que también están haciendo que la atención médica sea más accesible y eficiente.

En el ámbito educativo, la tecnología ha abierto nuevas posibilidades para el aprendizaje y la enseñanza. Las plataformas de educación en línea, los recursos digitales y las herramientas de colaboración están cambiando la forma en que los estudiantes acceden a la educación y cómo los profesores imparten sus clases. La educación ya no se limita a las aulas tradicionales; ahora, los estudiantes pueden aprender a su propio ritmo y desde cualquier lugar del mundo.

A pesar de todos estos avances, también hay desafíos y preocupaciones asociados con la tecnología. La privacidad y la seguridad son temas importantes, ya que la cantidad de datos que compartimos en línea sigue creciendo. Las brechas de seguridad y los ataques cibernéticos pueden tener consecuencias graves para individuos y organizaciones. Además, la adicción a la tecnología y el impacto en la salud mental son cuestiones que necesitan ser abordadas.

En conclusión, la tecnología ha transformado nuestras vidas de maneras inimaginables hace solo unas décadas. Nos ha brindado oportunidades increíbles, mejorado nuestra calidad de vida y cambiado la forma en que interactuamos con el mundo. Sin embargo, también es importante ser conscientes de los desafíos y trabajar para garantizar que la tecnología se utilice de manera ética y responsable. A medida que avanzamos hacia el futuro, la tecnología seguirá siendo un motor de cambio y progreso, y depende de nosotros aprovechar sus beneficios al máximo mientras mitigamos sus riesgos.
"""
    
    # Componente scroll
    scroll = scrolledtext.ScrolledText(tabulador2, width= 50, height = 10, wrap = tk.WORD)
    scroll.insert(tk.INSERT, contenido)
    scroll.grid(row=0, column=0)    
    
def componentes_tab3(tabulador3):
    
    # Creamos una lista con DataList comprehensions
    datos = [x+1 for x in range(10)]
    combobox = ttk.Combobox(tabulador3, width=15, values=datos)
    combobox.grid(row=0, column=0, padx=10, pady=10)
    
    # Seleccionamos un elemento a mostrar
    combobox.current(0)
    
    # Agrega un boton para que se muestre la eleccion del usuario
    def evento2():
        messagebox.showinfo('Valor seleccionado', f'Valor seleccionado: {combobox.get()}')
    
    boton2 = ttk.Button(tabulador3, text='Mostrar valor seleccionado', command=evento2)
    boton2.grid(row=0, column=2, padx=10, pady=10)
    
def componentes_tab4(tabulador4):
    # Variable con ruta a la imagen
    imagen = tk.PhotoImage(file='python-logo.png')
    
    def evento3():
        messagebox.showinfo('Más info de la imagen', f'Nombre de la imagen: {imagen.cget("file")}')
    
    boton3 = ttk.Button(tabulador4, image=imagen, command=evento3)
    boton3.grid(row=0, column=0)
    
def componentes_tab5(tabulador5):
    # Creamos el comoponente de la barra
    barra_progreso = ttk.Progressbar(tabulador5, orient='horizontal', length=550)
    barra_progreso.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
    
    # Botones para los eventos
    
    def evento4():
        barra_progreso['maximum'] = 100
        for valor in range(101):
            sleep(0.05)
            # Incrementar la barra
            barra_progreso['value'] = valor
            # Actualizar la barra
            barra_progreso.update()
        barra_progreso['value'] = 0
                           
    def evento5():
        barra_progreso.start()
    
    def detener():
        barra_progreso.stop()
    
    def despues():
        espera_ms = 1000
        ventana.after(espera_ms, barra_progreso.stop())
    
    boton_inicio = ttk.Button(tabulador5, text='Ejecutar Barra de Progreso', command= evento4)
    boton_inicio.grid(row=1, column=0)
    
    boton_ciclo = ttk.Button(tabulador5, text='Ejecutar ciclo', command= evento5)
    boton_ciclo.grid(row=1, column=1)
    
    boton_detener = ttk.Button(tabulador5, text='Detener ejecucion', command=detener)
    boton_detener.grid(row=1, column=2)
    
    boton_despues = ttk.Button(tabulador5, text='Detener ejecucion después', command=despues)
    boton_despues.grid(row=1, column=3)
    
def crear_tabs():
    
    # Usaremos Notebook
    control_tab = ttk.Notebook(ventana)
    
    # Se agrega un marco
    tab1 = ttk.Frame(control_tab)
    
    # Agregar el tabulador al control
    control_tab.add(tab1, text='Tabulador 1')
    
    # Se muestra el tabulador
    control_tab.pack(fill='both')
    
    # Creamos el metodo para los componentes del tab1 -> Se pide un texto al usuario que se muestra despues
    crear_componentes_tab1(tab1)
    
    # Segundo tab -> se crea un TextBox donde se muestran textos extensos y se puede desplazar
    tab2 = ttk.LabelFrame(control_tab, text='Contenido')
    control_tab.add(tab2, text='Tabulador 2')
    
    # Componentes del segundo tabulador
    componentes_tab2(tab2)
    
    # Creamos un tercer tabulador -> se crea un menu desplegable
    tab3 = ttk.Frame(control_tab)
    control_tab.add(tab3, text='Tabulador 3')
    # Componentes de este tabulador
    componentes_tab3(tab3)
        
    # 4 tabulador -> se muestra una imagen y se convierte en un boton para mostrar mas informacion
    tab4 = ttk.LabelFrame(control_tab, text='Imagen')
    control_tab.add(tab4, text='Tabulador 4')
    componentes_tab4(tab4)
    
    # 5 Tabulador -> se crea una progress bar
    tab5 = ttk.LabelFrame(control_tab, text='Progress Bar')
    control_tab.add(tab5, text='Tabulador 5')
    componentes_tab5(tab5)
    
    
    
crear_tabs()
ventana.mainloop()