import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QCheckBox


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        # Crear el CheckBox
        checkBox = QCheckBox('Este es un ChckBox')
        # Activar un 3cer estado al checkbox
        checkBox.setTristate(True)
        # Conectarlo a una señal
        checkBox.stateChanged.connect(self.show_state)

        # Publicarlo
        self.setCentralWidget(checkBox)

    def show_state(self, estado):
        print('Estado del CheckBox', estado)
        # cambair los numeros a constantes
        if estado == 2:
            print('CheckBox encendido')
        elif estado == 1:
            print('Sin estado o parcaialmente checado')
        elif estado == 0:
            print('CheckBox Apagado')
        else:
            print('CheckBox Inválido')
if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()
