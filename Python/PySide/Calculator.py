from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit


class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora')
        self.setFixedSize(300, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout_principal = QVBoxLayout(self.central_widget)

        self.pantalla = QLineEdit()
        self.pantalla.setReadOnly(True)
        self.pantalla.setAlignment(Qt.AlignRight)
        self.pantalla.setFixedHeight(35)
        self.layout_principal.addWidget(self.pantalla)

        self.botones = QGridLayout()
        self.layout_principal.addLayout(self.botones)

        self.crear_botones()

    def crear_botones(self):
        botones = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3),
            '4': (1, 0), '5': (1, 1), '6': (1, 2), '*': (1, 3),
            '1': (2, 0), '2': (2, 1), '3': (2, 2), '-': (2, 3),
            '0': (3, 0), '.': (3, 1), '=': (3, 2), '+': (3, 3),
            'C': (4, 0), '←': (4, 1, 1, 3)
        }

        for texto, posicion in botones.items():
            boton = QPushButton(texto)
            boton.setFixedSize(60, 60)
            if texto not in {'=', 'C', '←'}:
                boton.clicked.connect(self.agregar_texto)
            elif texto == '=':
                boton.clicked.connect(self.calcular_resultado)
            elif texto == 'C':
                boton.clicked.connect(self.limpiar_pantalla)
            else:  # Botón '←'
                boton.clicked.connect(self.borrar_ultimo_caracter)
            self.botones.addWidget(boton, *posicion)

    def agregar_texto(self):
        boton = self.sender()
        texto_actual = self.pantalla.text()
        nuevo_texto = texto_actual + boton.text()
        self.pantalla.setText(nuevo_texto)

    def calcular_resultado(self):
        try:
            resultado = eval(self.pantalla.text())
            self.pantalla.setText(str(resultado))
        except Exception as e:
            self.pantalla.setText('Error')

    def limpiar_pantalla(self):
        self.pantalla.clear()

    def borrar_ultimo_caracter(self):
        texto_actual = self.pantalla.text()
        nuevo_texto = texto_actual[:-1]
        self.pantalla.setText(nuevo_texto)


if __name__ == '__main__':
    app = QApplication([])
    ventana = Calculadora()
    ventana.show()
    app.exec()
