from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QPushButton
from PyQt5.QtCore import QFile, QTextStream, QTextCodec
from PyQt5.uic import loadUi
import json
import cbor

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Cargar la interfaz de usuario desde el archivo XML
        loadUi("mainWindow.ui", self)

        # Conectar señales y slots
        self.btnConvertToJson.clicked.connect(self.convert_to_json)
        self.btnConvertToCbor.clicked.connect(self.convert_to_cbor)

    def convert_to_json(self):
        # Obtener el texto del campo CBOR
        cbor_data = self.textEditCbor.toPlainText()

        try:
            # Decodificar el CBOR a JSON
            json_data = cbor.loads(bytes.fromhex(cbor_data))
            # Mostrar el JSON en el campo JSON
            self.textEditJson.setPlainText(json.dumps(json_data, indent=4))
        except Exception as e:
            self.textEditJson.setPlainText("ERROR\n" + str(e))
            print("Error al convertir a JSON:", e)

    def convert_to_cbor(self):
        # Obtener el texto del campo JSON
        json_data = self.textEditJson.toPlainText()

        try:
            # Codificar el JSON a CBOR
            cbor_data = cbor.dumps(json.loads(json_data))
            # Mostrar el CBOR en el campo CBOR
            self.textEditCbor.setPlainText(cbor_data.hex())
        except Exception as e:
            self.textEditCbor.setPlainText("ERROR\n" + str(e))
            print("Error al convertir a CBOR:", e)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
