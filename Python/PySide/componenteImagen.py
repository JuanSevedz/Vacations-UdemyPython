import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Insertar Imagen')
        self.setFixedSize(500, 600)
        # Componente -> Etiqueta(label)
        etiqueta = QLabel('Hola')
        # Modificaciones del texto
        etiqueta.setText('Saludando ando')
        # Fuente
        fuente = etiqueta.font()
        fuente.setPointSize(25)
        etiqueta.setFont(fuente)
        # Posicion de la etiqueta
        # etiqueta.setAlignment(Qt.AlignCenter) # Forma 1
        etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)# Forma 2
        etiqueta.setPixmap(QPixmap('Perrita.jpg'))
        etiqueta.setScaledContents(True)
        # Publicamoe es componente
        self.setCentralWidget(etiqueta)


if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()
