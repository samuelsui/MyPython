# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sec_test.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1763, 1303)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 30, 271, 651))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 0, 1, 1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 0, 0, 1, 1)
        self.value1 = QtWidgets.QLabel(self.centralwidget)
        self.value1.setGeometry(QtCore.QRect(70, 700, 269, 23))
        self.value1.setObjectName("value1")
        self.value2 = QtWidgets.QLabel(self.centralwidget)
        self.value2.setGeometry(QtCore.QRect(70, 750, 269, 23))
        self.value2.setObjectName("value2")
        self.cal_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cal_btn.clicked.connect(self.calculate)
        self.cal_btn.setGeometry(QtCore.QRect(500, 700, 75, 23))
        self.cal_btn.setObjectName("cal_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_2.setText(_translate("MainWindow", "10"))
        self.lineEdit_1.setText(_translate("MainWindow", "5"))
        self.value1.setText(_translate("MainWindow", "Result Here"))
        self.value2.setText(_translate("MainWindow", "Result Here"))
        self.cal_btn.setText(_translate("MainWindow", "Calculate"))
        self.action.setText(_translate("MainWindow", "??"))

    def calculate(self):
        result1 = int(self.lineEdit_1.text()) * int(self.lineEdit_2.text())
        result2 = result1 + int(self.lineEdit_2.text())

        self.value1.setNum(result1)
        self.value2.setNum(result2)
        self.value1, self.value2.adjustSize()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())