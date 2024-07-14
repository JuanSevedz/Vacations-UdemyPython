# Signals and slots
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        self.setFixedSize(400, 200)
        # Definimos: etiqueta y línea de edición
        self.etiqueta = QLabel()
        self.entrada_texto = QLineEdit()
        # Conectar el widget de entrada_texto con la etiqueta
        # la señal es textChanged, el slot es setText
        self.entrada_texto.textChanged.connect(self.etiqueta.setText)
        # Publicamos los componentes usando un layout
        disposicion = QVBoxLayout()
        disposicion.addWidget(self.entrada_texto)
        disposicion.addWidget(self.etiqueta)
        # Crear un contenedor
        contenedor = QWidget()
        contenedor.setLayout(disposicion)
        # Publicamos el contenedor, que ya incluye los demás elementos
        self.setCentralWidget(contenedor)


if __name__ == '__main__':
    # Creamos el objeto aplicación
    app = QApplication([])
    # Creamos una instancia de nuestra clase
    ventana = Main()
    ventana.show()
    sys.exit(app.exec())