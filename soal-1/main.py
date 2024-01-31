import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Soalsatu import *

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.calculate)
        self.show()

    def calculate(self):    
        angka = int(self.ui.lineEdit.text())
        for i in range(1, 11):
            hasil = angka * i
            self.ui.listWidget.addItem(f"{i} x {angka} = {hasil}")
            # item = (f'{angka} x {i} = {angka*i}')
            # self.ui.listWidget.addItem(item) 
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())