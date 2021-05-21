# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(863, 596)
        MainWindow.setStyleSheet("")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background:rgba(255, 255, 255, 0)")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.left_widget = QtWidgets.QWidget(self.centralwidget)
        self.left_widget.setMinimumSize(QtCore.QSize(80, 420))
        self.left_widget.setStyleSheet("background:rgb(65,105,225);\n"
"border-right:1px solid rgb(100,100,100);\n"
"border-bottom-left-radius:8px;\n"
"border-left:1px solid white;\n"
"border-right:1px solid white;")
        self.left_widget.setObjectName("left_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.left_widget)
        self.verticalLayout.setContentsMargins(1, -1, 1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.index_button = QtWidgets.QPushButton(self.left_widget)
        self.index_button.setMinimumSize(QtCore.QSize(0, 40))
        self.index_button.setStyleSheet("QPushButton#index_button{\n"
"border:none;\n"
"font-size:14px;\n"
"color:white;\n"
"font-family:Microsoft YaHei;\n"
"font-weight:700;\n"
"}\n"
"QPushButton#index_button:hover{\n"
"background:rgb(75,108,179);\n"
"}")
        self.index_button.setObjectName("index_button")
        self.verticalLayout.addWidget(self.index_button)
        self.push_button = QtWidgets.QPushButton(self.left_widget)
        self.push_button.setMinimumSize(QtCore.QSize(0, 40))
        self.push_button.setStyleSheet("QPushButton#push_button{\n"
"border:none;\n"
"font-size:14px;\n"
"color:white;\n"
"font-family:Microsoft YaHei;\n"
"font-weight:700;\n"
"}\n"
"QPushButton#push_button:hover{\n"
"background:rgb(75,108,179);\n"
"}")
        self.push_button.setObjectName("push_button")
        self.verticalLayout.addWidget(self.push_button)
        self.monitor_button = QtWidgets.QPushButton(self.left_widget)
        self.monitor_button.setMinimumSize(QtCore.QSize(0, 40))
        self.monitor_button.setStyleSheet("QPushButton#monitor_button{\n"
"border:none;\n"
"font-size:14px;\n"
"color:white;\n"
"font-family:Microsoft YaHei;\n"
"font-weight:700;\n"
"}\n"
"QPushButton#monitor_button:hover{\n"
"background:rgb(75,108,179);\n"
"}")
        self.monitor_button.setObjectName("monitor_button")
        self.verticalLayout.addWidget(self.monitor_button)
        self.gridLayout.addWidget(self.left_widget, 1, 0, 4, 1)
        self.right_widget = QtWidgets.QWidget(self.centralwidget)
        self.right_widget.setEnabled(True)
        self.right_widget.setMinimumSize(QtCore.QSize(0, 480))
        self.right_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.right_widget.setStyleSheet("background:rgb(255,255,255);\n"
"border-bottom-right-radius:8px;")
        self.right_widget.setObjectName("right_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.right_widget)
        self.verticalLayout_2.setContentsMargins(10, 0, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.wgt_video = myVideoWidget(self.right_widget)
        self.wgt_video.setEnabled(True)
        self.wgt_video.setMinimumSize(QtCore.QSize(410, 482))
        self.wgt_video.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(250, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.wgt_video.setPalette(palette)
        self.wgt_video.setAutoFillBackground(False)
        self.wgt_video.setStyleSheet("background:rgb(250,250,250);")
        self.wgt_video.setObjectName("wgt_video")
        self.verticalLayout_2.addWidget(self.wgt_video)
        self.horizontalWidget = QtWidgets.QWidget(self.right_widget)
        self.horizontalWidget.setMinimumSize(QtCore.QSize(0, 30))
        self.horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 30))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sld_video = myVideoSlider(self.horizontalWidget)
        self.sld_video.setMinimumSize(QtCore.QSize(410, 0))
        self.sld_video.setMaximumSize(QtCore.QSize(16777215, 20))
        self.sld_video.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #4A708B;\n"
"background: #C0C0C0;\n"
"height: 5px;\n"
"border-radius: 1px;\n"
"padding-left:-1px;\n"
"padding-right:-1px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"    stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #5DCCFF, stop: 1 #1874CD);\n"
"border: 1px solid #4A708B;\n"
"height: 10px;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #575757;\n"
"border: 0px solid #777;\n"
"height: 10px;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal\n"
"{\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, \n"
"    stop:0.6 #45ADED, stop:0.778409 rgba(255, 255, 255, 255));\n"
"\n"
"    width: 11px;\n"
"    margin-top: -3px;\n"
"    margin-bottom: -3px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 #2A8BDA, \n"
"    stop:0.778409 rgba(255, 255, 255, 255));\n"
"\n"
"    width: 11px;\n"
"    margin-top: -3px;\n"
"    margin-bottom: -3px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #00009C;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}\n"
"")
        self.sld_video.setMaximum(100)
        self.sld_video.setOrientation(QtCore.Qt.Horizontal)
        self.sld_video.setObjectName("sld_video")
        self.horizontalLayout.addWidget(self.sld_video)
        self.lab_video = QtWidgets.QLabel(self.horizontalWidget)
        self.lab_video.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lab_video.setStyleSheet("color:black;")
        self.lab_video.setObjectName("lab_video")
        self.horizontalLayout.addWidget(self.lab_video)
        self.verticalLayout_2.addWidget(self.horizontalWidget)
        self.splitter = QtWidgets.QSplitter(self.right_widget)
        self.splitter.setEnabled(True)
        self.splitter.setStyleSheet("")
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.btn_open = QtWidgets.QPushButton(self.splitter)
        self.btn_open.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_open.setMaximumSize(QtCore.QSize(100, 40))
        self.btn_open.setStyleSheet("QPushButton#btn_open{\n"
"border-radius:8px;\n"
"background:rgb(65,105,225);\n"
"font-size:14px;\n"
"color:white;\n"
"font-family:Microsoft YaHei;\n"
"}\n"
"\n"
"QPushButton#btn_open:hover{\n"
"background:rgb(55,95,215);\n"
"}\n"
"")
        self.btn_open.setObjectName("btn_open")
        self.btn_play = QtWidgets.QPushButton(self.splitter)
        self.btn_play.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_play.setMaximumSize(QtCore.QSize(80, 40))
        self.btn_play.setStyleSheet("QPushButton#btn_play{\n"
"border-radius:8px;\n"
"background:rgb(65,105,225);\n"
"font-size:14px;\n"
"color:white;\n"
"font-family:Microsoft YaHei;\n"
"}\n"
"\n"
"QPushButton#btn_play:hover{\n"
"background:rgb(55,95,215);\n"
"}")
        self.btn_play.setObjectName("btn_play")
        self.btn_stop = QtWidgets.QPushButton(self.splitter)
        self.btn_stop.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_stop.setMaximumSize(QtCore.QSize(80, 40))
        self.btn_stop.setStyleSheet("QPushButton#btn_stop{\n"
"border-radius:8px;\n"
"background:rgb(65,105,225);\n"
"font-size:14px;\n"
"color:white;\n"
"font-family:Microsoft YaHei;\n"
"}\n"
"\n"
"QPushButton#btn_stop:hover{\n"
"background:rgb(55,95,215);\n"
"}")
        self.btn_stop.setObjectName("btn_stop")
        self.sld_audio = QtWidgets.QSlider(self.splitter)
        self.sld_audio.setMinimumSize(QtCore.QSize(100, 40))
        self.sld_audio.setMaximumSize(QtCore.QSize(150, 20))
        self.sld_audio.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #4A708B;\n"
"background: #C0C0C0;\n"
"height: 5px;\n"
"border-radius: 1px;\n"
"padding-left:-1px;\n"
"padding-right:-1px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: #4169E1;\n"
"border: 1px solid #4A708B;\n"
"height: 10px;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #575757;\n"
"border: 0px solid #777;\n"
"height: 10px;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal \n"
"{\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, \n"
"    stop:0.6 #45ADED, stop:0.778409 rgba(255, 255, 255, 255));\n"
"    width: 11px;\n"
"    margin-top: -3px;\n"
"    margin-bottom: -3px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 #2A8BDA, \n"
"    stop:0.778409 rgba(255, 255, 255, 255));\n"
"\n"
"    width: 11px;\n"
"    margin-top: -3px;\n"
"    margin-bottom: -3px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #00009C;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}\n"
"")
        self.sld_audio.setProperty("value", 99)
        self.sld_audio.setOrientation(QtCore.Qt.Horizontal)
        self.sld_audio.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.sld_audio.setTickInterval(0)
        self.sld_audio.setObjectName("sld_audio")
        self.lab_audio = QtWidgets.QLabel(self.splitter)
        self.lab_audio.setEnabled(True)
        self.lab_audio.setMinimumSize(QtCore.QSize(0, 0))
        self.lab_audio.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lab_audio.setStyleSheet("font-size:14px;\n"
"color:black;\n"
"font-family:Microsoft YaHei;")
        self.lab_audio.setObjectName("lab_audio")
        self.btn_cast = QtWidgets.QPushButton(self.splitter)
        self.btn_cast.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_cast.setStyleSheet("QPushButton#btn_cast{\n"
"border-radius:2px;\n"
"background:rgb(65,105,225);\n"
"font-size:14px;\n"
"color:white;\n"
"font-family:Microsoft YaHei;\n"
"}\n"
"\n"
"QPushButton#btn_cast:hover{\n"
"background:rgb(55,95,215);\n"
"}")
        self.btn_cast.setObjectName("btn_cast")
        self.verticalLayout_2.addWidget(self.splitter)
        self.gridLayout.addWidget(self.right_widget, 1, 1, 4, 1)
        self.top_widget = QtWidgets.QWidget(self.centralwidget)
        self.top_widget.setMinimumSize(QtCore.QSize(0, 50))
        self.top_widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.top_widget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.top_widget.setStyleSheet("background:rgb(65,105,225);\n"
"\n"
"border-top-left-radius:8px;\n"
"border-top-right-radius:8px;\n"
"\n"
"border-left:1px solid white;\n"
"border-top:1px solid white;\n"
"border-bottom:1px solid orange;")
        self.top_widget.setObjectName("top_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.top_widget)
        self.horizontalLayout_3.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.close_button = QtWidgets.QPushButton(self.top_widget)
        self.close_button.setMinimumSize(QtCore.QSize(25, 25))
        self.close_button.setMaximumSize(QtCore.QSize(25, 25))
        self.close_button.setStyleSheet("QPushButton#close_button{\n"
"border-image:url(:/icon/icon/close.png);\n"
"}\n"
"\n"
"\n"
"QPushButton#close_button:hover{\n"
"border-image:url(:/icon/icon/close_hover.png);\n"
"}\n"
"\n"
"")
        self.close_button.setText("")
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_3.addWidget(self.close_button)
        self.maxmize_button = QtWidgets.QPushButton(self.top_widget)
        self.maxmize_button.setMinimumSize(QtCore.QSize(25, 25))
        self.maxmize_button.setMaximumSize(QtCore.QSize(25, 25))
        self.maxmize_button.setStyleSheet("QPushButton#maxmize_button{\n"
"border-image:url(:/icon/icon/maxmize.png);\n"
"}\n"
"\n"
"\n"
"QPushButton#maxmize_button:hover{\n"
"border-image:url(:/icon/icon/maxmize_hover.png);\n"
"}\n"
"\n"
"")
        self.maxmize_button.setText("")
        self.maxmize_button.setObjectName("maxmize_button")
        self.horizontalLayout_3.addWidget(self.maxmize_button)
        self.minimize_button = QtWidgets.QPushButton(self.top_widget)
        self.minimize_button.setMinimumSize(QtCore.QSize(30, 30))
        self.minimize_button.setMaximumSize(QtCore.QSize(30, 30))
        self.minimize_button.setStyleSheet("QPushButton#minimize_button{\n"
"border-image:url(:/icon/icon/minimize.png);\n"
"}\n"
"\n"
"\n"
"QPushButton#minimize_button:hover{\n"
"border-image:url(:/icon/icon/minimize_hover.png);\n"
"}\n"
"\n"
"")
        self.minimize_button.setText("")
        self.minimize_button.setObjectName("minimize_button")
        self.horizontalLayout_3.addWidget(self.minimize_button)
        self.label = QtWidgets.QLabel(self.top_widget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;\n"
"border:none;")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.gridLayout.addWidget(self.top_widget, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        MainWindow.setWindowTitle(_translate("MainWindow", "Yore"))
        self.index_button.setText(_translate("MainWindow", "首页"))
        self.push_button.setText(_translate("MainWindow", "上传监控"))
        self.monitor_button.setText(_translate("MainWindow", "监控管理"))
        self.lab_video.setText(_translate("MainWindow", "0%"))
        self.btn_open.setText(_translate("MainWindow", "上传监控"))
        self.btn_play.setText(_translate("MainWindow", "播放"))
        self.btn_stop.setText(_translate("MainWindow", "暂停"))
        self.lab_audio.setText(_translate("MainWindow", "音量:100%"))
        self.btn_cast.setText(_translate("MainWindow", "截取"))
        self.label.setText(_translate("MainWindow", "YORE"))
from myVideoWidget import myVideoWidget
from myvideoslider import myVideoSlider
import icon_rc

