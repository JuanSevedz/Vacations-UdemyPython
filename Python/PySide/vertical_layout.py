from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout


class Color(QWidget):
    def __init__(self, nuevo_color):
        super().__init__()
        # Indicamos que se puede agregar un color de fondo
        self.setAutoFillBackground(True)
        paletaColores = self.palette()
        # Creamos el componente de color de fondo aplicando el nuevo color
        paletaColores.setColor(QPalette.Window, QColor(nuevo_color))
        # Aplicamos el nuevo color al componente
        self.setPalette(paletaColores)

class Layautt(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Layouts en PySide')

        layout = QVBoxLayout()
        # Agregar un componente de color
        layout.addWidget(Color('yellow'))
        layout.addWidget(Color('blue'))
        layout.addWidget(Color('red'))
        # Creamos el componente para que se pueda publicar
        componente = QWidget()
        componente.setLayout(layout)
        self.setCentralWidget(componente)

if __name__ == '__main__':
    app = QApplication([])
    ventana = Layautt()
    ventana.show()
    app.exec()