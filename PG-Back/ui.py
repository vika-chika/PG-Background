from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 330)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("background-color: #FFA07A")
        self.centralwidget.setObjectName("centralwidget")
        self.count = QtWidgets.QLineEdit(self.centralwidget)
        self.count.setGeometry(QtCore.QRect(25, 120, 250, 45))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        MainWindow.setFixedSize(300, 330)
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.count.setFont(font)
        self.count.setAutoFillBackground(False)
        self.count.setStyleSheet("background-color: #FFA07A;\n"
"border: 2px solid #F08080;\n"
"border-radius: 20px;\n"
"color: white")
        self.count.setText("14")
        self.count.setAlignment(QtCore.Qt.AlignCenter)
        self.count.setObjectName("count")
        self.phone = QtWidgets.QLabel(self.centralwidget)
        self.phone.setGeometry(QtCore.QRect(0, -40, 300, 110))
        self.phone.setStyleSheet("background-color: #F08080;\n"
"border: 1px solid #F08080;\n"
"border-radius: 20px;\n"
"")
        self.phone.setText("")
        self.phone.setObjectName("phone")
        self.text = QtWidgets.QLabel(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(0, 15, 300, 40))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.text.setFont(font)
        self.text.setStyleSheet("background-color: #F08080;\n"
"color: white")
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setObjectName("text")
        self.passw = QtWidgets.QLineEdit(self.centralwidget)
        self.passw.setGeometry(QtCore.QRect(25, 210, 250, 45))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.passw.setFont(font)
        self.passw.setAutoFillBackground(False)
        self.passw.setStyleSheet("background-color: #FFA07A;\n"
"border: 2px solid #F08080;\n"
"border-radius: 20px;\n"
"color: white")
        self.passw.setText("")
        self.passw.setAlignment(QtCore.Qt.AlignCenter)
        self.passw.setObjectName("passw")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 270, 220, 40))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"background-color: #E9967A;\n"
"color: white;\n"
"border: 2px solid #F08080;\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #FA8072;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 80, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 170, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.text.setText(_translate("MainWindow", "PASSWORD GENERATOR"))
        self.pushButton.setText(_translate("MainWindow", "GENERATE"))
        self.label.setText(_translate("MainWindow", "Password length:"))
        self.label_2.setText(_translate("MainWindow", "Result:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setFixedSize(300, 330)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
