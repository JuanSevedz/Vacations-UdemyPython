import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QComboBox


class ComboBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ComboBox')
        # se cera el combo Box
        combobox = QComboBox()
        # Añadir elementos
        combobox.addItem('Uno')
        combobox.addItems(['Dos', 'Tres'])
        # Publicarlo
        self.setCentralWidget(combobox)
        # Añadir sel+ñales y monitorear los cambios seleccionados
        combobox.currentIndexChanged.connect(self.cambio_index)
        combobox.currentTextChanged.connect(self.cambio_texto)
        # Hacer editable el componente
        combobox.setEditable(True)
        # Especificar los parametros para poder insertar
        # combobox.setInsertPolicy(QComboBox.NoInsert)
        # Agregar un elemento al inicio
        # combobox.setInsertPolicy(QComboBox.InsertAtTop)
        # Modificar un elemento actual
        # combobox.setInsertPolicy(QComboBox.InsertAtCurrent)
        # Insertar al final
        # combobox.setInsertPolicy(QComboBox.InsertAtBottom)
        # iNSERTAR ELEMENTO ANTES DEL ELEMENTO ACTUAL
        # combobox.setInsertPolicy(QComboBox.InsertBeforeCurrent)
        # Insertar elementos despues del elemento actual
        # combobox.setInsertPolicy(QComboBox.InsertAfterCurrent)
        # Insertar por orden alfabético
        combobox.setInsertPolicy(QComboBox.InsertAlphabetically)
        # Limitar el numero de elementos que se pueden añadir
        combobox.setMaxCount(6)
    def cambio_index(self, indice):
        print(f'Nuevo indice seleccionado: {indice + 1}')

    def cambio_texto(self, texto):
        print(f'Nuevo texto seleccionado: {texto}')


if __name__ == '__main__':
    app = QApplication([])
    ventana = ComboBox()
    ventana.show()
    app.exec()
