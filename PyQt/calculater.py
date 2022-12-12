from PyQt5.QtWidgets import QMainWindow, QApplication


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "계산기"
        self.setWindowTitle(self.title)

        self.left = 100
        self.top = 200
        self.width = 300
        self.height = 200
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()


app = QApplication([])
calc = App()
app.exec_()

import QToolButton


class Button(QToolButton):
    def __init__(self, text):
        super().__init__()
        buttonStyle = '''
        QToolButton:hover {border:1px solid #0078d7; background-color:#e5f1fb;}
        QToolButton:pressed {background-color:#a7c8e3}
        QToolButton {font-size:11pt; font-family:NaNum Gothic; border:1px solid #d6d7d8; background-color#f0f1f1}
        '''
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.setStyleSheet(buttonStyle)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 30)
        size.setWidth(max(size.width(), size.height()))
        return size

self.display = QLineEdit("0")
self.display.setReadOnly(True)
self.display.setAlignment(QT.AlignRight)
self.display.setStyleSheet("border:0px; font-size:20pt; font-family:Nanum Gothic; font-weight:bold; padding:10px")

gridLayout = QGridLayout()
gridLayout.setSizeConstraint(QLayout.SetFixedSize)

layout = QVBoxLayout()
layout.addWidget(self.display)
layout.addLayout(gridLayout)
self.setLayout(layout)

self.clearButton = self.createButton("CE", self.clear)
self.clearAllButton = self.createButton("C", self.clearAll)
self.backButton = self.createButton("Back", self.backDelete)
self.divButton = self.createButton("/", self.clickButtons)
self.multiplyButton = self.createButton("*", self.clickButtons)
self.minusButton = self.createButton("-", self.clickButtons)
self.plusButton = self.createButton("+", self.clickButtons)
self.equalButton = self.createButton("=", self.clickButtons)
self.dotButton = self.createButton(".", self.clickButtons)
self.reverseButton = self.createButton("R", self.reverse)

gridLayout.addWidget(self.clearButton, 0,0,1,1)
gridLayout.addWidget(self.clearAllButton, 0,1,1,1)
gridLayout.addWidget(self.backButton, 0,2,1,1)
gridLayout.addWidget(self.divButton, 0,3,1,1)
gridLayout.addWidget(self.multiplyButton, 1,3,1,1)
gridLayout.addWidget(self.minusButton, 2,3,1,1)
gridLayout.addWidget(self.plusButton, 3,3,1,1)
gridLayout.addWidget(self.equalButton, 4,3,1,1)
gridLayout.addWidget(self.dotButton, 4,2,1,1)
gridLayout.addWidget(self.reverseButton, 4,0,1,1)
