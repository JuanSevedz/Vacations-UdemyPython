from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QDial


class QSlideer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QSlider')
        # Rueda que se mueve
        componente = QDial()
        componente.setRange(-5, 50)

        # Conectar a señales
        componente.valueChanged.connect(self.cambio_valor)
        componente.sliderMoved.connect(self.slider_cambio_valor)
        componente.sliderPressed.connect(self.slider_presionado)
        componente.sliderReleased.connect(self.slider_liberado)

        # Publicar el componente
        self.setCentralWidget(componente)

    def cambio_valor(self, nuevo_valor):
        print(f'Nuevo valor: {nuevo_valor}')

    def slider_cambio_valor(self, nuevo_slider):
        print(f'Nueva posicion: {nuevo_slider}')

    def slider_presionado(self):
        print('Slider presionado')

    def slider_liberado(self):
        print('Slider Liberado')

if __name__ == '__main__':
    app = QApplication([])
    ventana = QSlideer()
    ventana.show()
    app.exec()