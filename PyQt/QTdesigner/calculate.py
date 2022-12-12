import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

UI = 'task.ui'


class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI, self)
        self.setting()

    def setting(self):
        self.check.clicked.connect(self.calculator)

    def calculator(self):
        i = 0
        if self.value.currentText() == '+':
            i = float(self.X.text()) + float(self.Y.text())
        elif self.value.currentText() == '-':
            i = float(self.X.text()) - float(self.Y.text())
        elif self.value.currentText() == '*':
            i = float(self.X.text()) * float(self.Y.text())
        elif self.value.currentText() == '/':
            if self.Y.text() == '0':
                pass
            else:
                i = float(self.X.text()) / float(self.Y.text())
        self.result.setText(str(i))


app = QApplication(sys.argv)
ex = Dialog()
ex.show()
sys.exit(app.exec_())