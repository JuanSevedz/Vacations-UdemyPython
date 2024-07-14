import sys
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton


class VentanaPySide(QMainWindow):
    def __init__(self):
        # Llamamos al método init de la clase padre
        super().__init__()
        self.setWindowTitle('POO con PySide')
        # self.resize(600,400)
        # Valores de ancho y alto, fijos
        self.setFixedSize(QSize(600,400))
        # Creamos algunos componentes
        self._add_components()


    def _add_components(self):
        # Crear el menu
        menu = self.menuBar()
        menu_archivo = menu.addMenu('Archivo')
        # Agregar opciones al menu
        accion_nuevo = QAction('Nuevo', self)
        menu_archivo.addAction(accion_nuevo)
        # Agregamos texto a la barra de estado
        accion_nuevo.setStatusTip('Nuevo archivo')
        # Ahora un mensaje...
        self.statusBar().showMessage('Informacion Barra de estado')
        # Agregar botones
        boton = QPushButton('Nuevo Boton')
        # Mostrar el boton
        self.setCentralWidget(boton)


if __name__ == '__main__':
    app = QApplication([])
    # Creamos un objeto de tipo ventana
    ventana = VentanaPySide()
    ventana.show()
    # Ejecutamos la ventana
    sys.exit(app.exec())