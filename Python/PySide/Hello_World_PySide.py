import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

# Clase base de Qt (PySyde)
app = QApplication()# Se encarga de los eventos
# Crear obejto -> Ventana
# ventana = QPushButton('Boton de PySide')
ventana = QMainWindow()

# Cambiar el titulo de la ventana
ventana.setWindowTitle('Hola Mundo Con Pyside')
# Modificar las dimensiones
ventana.resize(600, 400)
# Mostrar ventana
ventana.show()
sys.exit(app.exec())

