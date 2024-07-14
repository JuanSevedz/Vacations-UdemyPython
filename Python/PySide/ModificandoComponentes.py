# Signals and slots
import sys
from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        # se crea el Boton
        self.boton = QPushButton('Click aquí')
        # Asociamos la señal de click al slot evento_click
        self.boton.clicked.connect(self.evento_click)
        # Conectar a la señal cambio de título
        self.windowTitleChanged.connect(self.cambio_titulo)
        # Publicamos el botón
        self.setCentralWidget(self.boton)

    def evento_click(self):
        # Cambiar el texto del botón y el título de la ventana
        self.boton.setText('Boton presionado')
        self.boton.setEnabled(False)
        self.setWindowTitle('Pagina cambiada por el boton')
        print('evento_click')

    def cambio_titulo(self, nuevo_titulo):
        print(f'Nuevo titulo de la app: {nuevo_titulo}')



if __name__ == '__main__':
    # Creamos el objeto aplicación
    app = QApplication([])
    # Creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())