# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import qtawesome

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        self.setFixedSize(1080, 900)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        #左侧部分
        self.left_close = QtWidgets.QPushButton("") # 关闭按钮
        self.left_max = QtWidgets.QPushButton("") # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_close.setFixedSize(15,15) # 设置关闭按钮的大小
        self.left_max.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15) # 设置最小化按钮大小

        self.left_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_max.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')


        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.home',color='white'),"首页")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.music',color='white'),"找寻")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.film',color='white'),"统计")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.download',color='white'),"下载管理")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.comment',color='white'),"反馈建议")
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.question',color='white'),"遇到问题")
        self.left_button_6.setObjectName('left_button')

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;font-size:16px}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: Microsoft YaHei;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')


        self.left_xxx = QtWidgets.QPushButton(" ")

        self.left_layout.addWidget(self.left_mini, 0, 0,1,1)
        self.left_layout.addWidget(self.left_close, 0, 2,1,1)
        self.left_layout.addWidget(self.left_max, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_button_1, 2, 0,1,3)
        self.left_layout.addWidget(self.left_button_2, 3, 0,1,3)
        self.left_layout.addWidget(self.left_button_3, 4, 0,1,3)
        self.left_layout.addWidget(self.left_button_4, 6, 0,1,3)
        self.left_layout.addWidget(self.left_button_5, 7, 0,1,3)
        self.left_layout.addWidget(self.left_button_6, 8, 0,1,3)

        #右侧部分        
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.wgt_video = myVideoWidget(self.centralwidget)
        self.wgt_video.setMinimumSize(QtCore.QSize(410, 200))
        self.wgt_video.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.wgt_video.setPalette(palette)
        self.wgt_video.setAutoFillBackground(True)
        self.wgt_video.setObjectName("wgt_video")
        self.gridLayout.addWidget(self.wgt_video, 0, 0, 1, 1)
        self.sld_video = myVideoSlider(self.centralwidget)
        self.sld_video.setMinimumSize(QtCore.QSize(410, 0))
        self.sld_video.setMaximumSize(QtCore.QSize(16777215, 20))
        self.sld_video.setMaximum(100)
        self.sld_video.setOrientation(QtCore.Qt.Horizontal)
        self.sld_video.setObjectName("sld_video")
        self.gridLayout.addWidget(self.sld_video, 1, 0, 1, 1)
        self.lab_video = QtWidgets.QLabel(self.centralwidget)
        self.lab_video.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lab_video.setObjectName("lab_video")
        self.gridLayout.addWidget(self.lab_video, 1, 1, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.btn_open = QtWidgets.QPushButton(self.splitter)
        self.btn_open.setMaximumSize(QtCore.QSize(100, 25))
        self.btn_open.setObjectName("btn_open")
        self.btn_play = QtWidgets.QPushButton(self.splitter)
        self.btn_play.setMaximumSize(QtCore.QSize(100, 25))
        self.btn_play.setObjectName("btn_play")
        self.btn_stop = QtWidgets.QPushButton(self.splitter)
        self.btn_stop.setMaximumSize(QtCore.QSize(100, 25))
        self.btn_stop.setObjectName("btn_stop")
        self.sld_audio = QtWidgets.QSlider(self.splitter)
        self.sld_audio.setMinimumSize(QtCore.QSize(100, 0))
        self.sld_audio.setMaximumSize(QtCore.QSize(150, 20))
        self.sld_audio.setProperty("value", 99)
        self.sld_audio.setOrientation(QtCore.Qt.Horizontal)
        self.sld_audio.setObjectName("sld_audio")
        self.lab_audio = QtWidgets.QLabel(self.splitter)
        self.lab_audio.setObjectName("lab_audio")
        self.btn_cast = QtWidgets.QPushButton(self.splitter)
        self.btn_cast.setObjectName("btn_cast")
        self.gridLayout.addWidget(self.splitter, 2, 0, 1, 1)
        #MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 23))
        self.menubar.setObjectName("menubar")
        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")


        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.right_layout.addWidget(self.centralwidget, 0, 0, 1, 9)
        self.main_layout.setSpacing(0)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        MainWindow.setWindowTitle(_translate("MainWindow", "Yore"))
        self.lab_video.setText(_translate("MainWindow", "0%"))
        self.btn_open.setText(_translate("MainWindow", "上传监控"))
        self.btn_play.setText(_translate("MainWindow", "播放"))
        self.btn_stop.setText(_translate("MainWindow", "暂停"))
        self.lab_audio.setText(_translate("MainWindow", "volume:100%"))
        self.btn_cast.setText(_translate("MainWindow", "截取"))

from myVideoWidget import myVideoWidget
from myvideoslider import myVideoSlider
