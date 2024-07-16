from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QHBoxLayout, QVBoxLayout


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
        # Anidar layouts
        layout_horizontal = QHBoxLayout()

        # Agregar espacios en el layput principal
        layout_horizontal.setContentsMargins(10,10,10,10)
        layout_horizontal.setSpacing(30)

        layout_vertical = QVBoxLayout()

        # Agregar espacios al layput secundario
        layout_vertical.setContentsMargins(5, 10, 5, 10)

        # Agregar espacios entre cada elemento
        layout_vertical.setSpacing(20)

        # Agregar widgets
        layout_vertical.addWidget(Color('yellow'))
        layout_vertical.addWidget(Color('blue'))
        layout_vertical.addWidget(Color('red'))

        # Anidar los layouts
        layout_horizontal.addLayout(layout_vertical)

        # Agregar elementos al layout principal
        layout_horizontal.addWidget(Color('green'))
        layout_horizontal.addWidget(Color('blue'))

        # Creamos el componente para que se pueda publicar
        componente = QWidget()
        componente.setLayout(layout_horizontal)
        self.setCentralWidget(componente)

if __name__ == '__main__':
    app = QApplication([])
    ventana = Layautt()
    ventana.show()
    app.exec()