# Signals and Slots
import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class Main(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signal And Slots')
        # Crear el boton..
        boton = QPushButton('Click Aquí')
        # Chequear el evento que por default es (False)
        boton.setCheckable(True)
        # conectar el slot al evento chequear
        boton.clicked.connect(self.evento_checar)
        # Conectar el evento Signal
        boton.clicked.connect(self.evento_click)
        # Publicamos el botón...
        self.setCentralWidget(boton)

    def evento_checar(self, checar):
        self.boton_checado = checar
        print('Checado?', self.boton_checado)
    def evento_click(self):
        print('Haz hecho click')
        # Acceder al estado del botn
        print('Checando el estado del bottón desde el evento click:', self.boton_checado)

if __name__ == '__main__':
    # creamos el app
    app = QApplication([])

    ventana = Main()
    ventana.show()
    sys.exit(app.exec())
