from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMenu


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menú Contextual')
        

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        boton_nuevo = QAction(QIcon('nuevo.png'), 'Nuevo', self)
        boton_guardar = QAction(QIcon('guardar.png'), 'Guardar', self)
        boton_salir = QAction('Salir', self)
        # Conectamos con la opción triggered
        boton_nuevo.triggered.connect(self.click_boton_nuevo)
        boton_guardar.triggered.connect(self.click_boton_guardar)
        boton_salir.triggered.connect(self.click_boton_salir)
        menu.addAction(boton_nuevo)
        menu.addAction(boton_guardar)
        menu.addAction(boton_salir)
        # Recuperamos la posición del cursor como posición global de la ventana padre
        # Ejecutamos el menú contextual
        menu.exec(event.globalPos())

    def click_boton_nuevo(self, s):
        print('Opción Nuevo...')

    def click_boton_guardar(self, s):
        print('Opción Guardar...')

    def click_boton_salir(self, s):
        print('Opción Salir...')
        self.close()  # Cierra la ventana


if __name__ == '__main__':
    app = QApplication([])
    ventana = Menu()
    ventana.show()
    app.exec()
