import sys, random, time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow

sum = "1Qq.2Ww3E_e4Rr_.5Tt6Y_y7Uu18Ii9O.o0Pp1Aa2_Ss3Dd4F_g5G.g6H3h_7Jj8K6k_.LlZz9.XxCc_V0vB5bNnM.m"

class Generator(QtWidgets.QMainWindow):
    def __init__(self):
        super(Generator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    
    def init_UI(self):
        self.setWindowTitle('Password Generator')
        self.setWindowIcon(QIcon('icon.ico')) 
        self.ui.pushButton.clicked.connect (self.PasswGenerator)
    
    def PasswGenerator(self):
        count = self.ui.count.text()
        for n in range(1):
            passw = ''
            for i in range(int(count)):
                passw += random.choice(sum)

        self.ui.passw.setText(str(passw))

app = QtWidgets.QApplication ([])
application = Generator()
application.show()

sys.exit(app.exec())