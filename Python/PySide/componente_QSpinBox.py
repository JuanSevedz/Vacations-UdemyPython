from PySide6.QtWidgets import QMainWindow, QApplication, QSpinBox


class QSpinB(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QSpinBox')

        # Iniciamos el componente QSpinBox
        numero = QSpinBox()

        # Establecer MIN/MAX (rango)
        # numero.setMinimum(-5)
        # numero.setMaximum(7)
        numero.setRange(-5, 7)

        # Prefijos:
        numero.setPrefix('$')
        # Sufijo
        numero.setSuffix('c')

        # Saltos -> cuando se preciona la felca, es el número de saltos que da
        numero.setSingleStep(3)

        # Conexion a eventos
        numero.valueChanged.connect(self.cambio_valor)# Nuevo valor
        numero.textChanged.connect(self.cambio_texto)# Cambios en el texto



        # La publicamos
        self.setCentralWidget(numero)

    def cambio_valor(self, new_value):
        print(f'Nuevo valor: {new_value}')

    def cambio_texto(self, nuevo_texto):
        print(f'Nuevo texto: {nuevo_texto}')


if __name__ == '__main__':
    app = QApplication([])
    ventana = QSpinB()
    ventana.show()
    app.exec()