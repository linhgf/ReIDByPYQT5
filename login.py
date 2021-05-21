import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton
from PyQt5.QtCore import Qt
from QQLogin import Ui_Dialog
from PyQt5.Qt import QWidget
from PyQt5.QtGui import QIcon, QPixmap, QMovie

import image_rc


class QSSLoad:
    def __init__(self):
           pass
        
    @staticmethod
    def readQssFile(qssFileName):
           with open(qssFileName, 'r',  encoding='UTF-8') as file:
               return file.read()


class MyMainWindow(QWidget, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去掉标题栏

        self.accountcomboBox.setEditable(True)
        lineEdit = self.accountcomboBox.lineEdit()
        lineEdit.setPlaceholderText("QQ号码/手机/邮箱")
        self.passwordEdit.setPlaceholderText("密码")
        self.loginStatusBtn.raise_()

        self.picLab.setPixmap(QPixmap(':/images/HeadImage.png'))
        self.loginStatusBtn.setIcon(QIcon(':/images/state_online.png'))

        self.initBackGif()

    #设置背景gif图
    def initBackGif(self):
        pback = QLabel(self)
        movie = QMovie()
        movie.setFileName(":/images/back.gif")
        movie.start()
        movie.stop()
        pback.setMovie(movie)
        movie.start()
        pback.move(0, 0)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    qssFileName = "./images/login1.qss"
    qssFile = QSSLoad.readQssFile(qssFileName)

    win = MyMainWindow()
    win.setStyleSheet(qssFile)
    win.show()
    sys.exit(app.exec())
