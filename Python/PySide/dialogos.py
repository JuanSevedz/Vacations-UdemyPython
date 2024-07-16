
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class VentanaDialogo(QDialog):

    def __init__(self, padre = None):
        super().__init__(padre)
        self.setWindowTitle('QDialog')
        # boton de acptar/cancelar
        botones = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.botones_dialog = QDialogButtonBox(botones)
        self.botones_dialog.accepted.connect(self.accept)
        self.botones_dialog.rejected.connect(self.reject)

        # Layout
        self.layout =  QVBoxLayout()
        mensaje = QLabel('Presiona cualquier botón')
        self.layout.addWidget(mensaje)
        self.layout.addWidget(self.botones_dialog)
        self.setLayout(self.layout)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dialogo')

        # Boton
        boton = QPushButton('Mostrar dialogo')
        boton.clicked.connect(self.click_boton)
        self.setCentralWidget(boton)



    def click_boton(self, s):
        print(f'Click en el boton: {s}')
        # Dialogo
        dialogo = VentanaDialogo(self)
        valor_returned = dialogo.exec()
        print(f'Valor que retorna: {valor_returned}')
        if valor_returned:
            print('Se presiono OK')
        else:
            print('Se presionó CANCEL')





if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()