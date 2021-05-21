from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from GUI_3 import Ui_MainWindow
from myVideoWidget import myVideoWidget
from myVideoSurface import myVideoSurface
import sys
from qssload import QSSLoad


class myMainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.grab_player_position = 0 #截图的时候视频播放位置
        self.grab_player_state = QMediaPlayer.StoppedState  # 截图的时候视频播放状态
        self.sld_video_pressed=False  #判断当前进度条识别否被鼠标点击
        self.videoFullScreen = False   # 判断当前widget是否全屏
        self.videoFullScreenWidget = myVideoWidget()   # 创建一个全屏的widget
        self.VideoSurface = myVideoSurface()
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.wgt_video)  # 视频播放输出到videosurface
        # self.left_close.clicked.connect(self.close) #关闭窗口
        # self.left_max.clicked.connect(self.maxmisize) #最大化窗口
        # self.left_mini.clicked.connect(self.minimize) #最小化窗口
        self.btn_open.clicked.connect(self.openVideoFile)   # 打开视频文件按钮
        self.btn_play.clicked.connect(self.playVideo)       # play
        self.btn_stop.clicked.connect(self.pauseVideo)       # pause
        self.btn_cast.clicked.connect(self.start_grab_video)        # 视频截图
        self.VideoSurface.FinishGrab.connect(self.finish_grab_video)
        self.player.positionChanged.connect(self.changeSlide)      # change Slide
        self.videoFullScreenWidget.doubleClickedItem.connect(self.videoDoubleClicked)  #双击响应
        self.wgt_video.doubleClickedItem.connect(self.videoDoubleClicked)   #双击响应
        self.sld_video.setTracking(False)
        self.sld_video.sliderReleased.connect(self.releaseSlider)
        self.sld_video.sliderPressed.connect(self.pressSlider)
        self.sld_video.sliderMoved.connect(self.moveSlider)   # 进度条拖拽跳转
        self.sld_video.ClickedValue.connect(self.clickedSlider)  # 进度条点击跳转
        self.sld_audio.valueChanged.connect(self.volumeChange)  # 控制声音播放

    def maxmisize(self):
        if not self.isMaximized():
            self.showMaximized()
        else:
            self.showNormal()

    def minimize(self):
        self.showMinimized()

    def start_grab_video(self):
        # 记录当前的播放信息，方便恢复播放的时候使用
        if self.player.state() != QMediaPlayer.StoppedState:
            self.grab_player_state = self.player.state()
            self.grab_player_position = self.player.position()
            self.player.pause()  # 暂停当前的播放
            self.player.setVideoOutput(self.VideoSurface)  # 设置输出为帧获取
            self.player.setPosition(self.grab_player_position)
            self.player.play()

    def finish_grab_video(self):
        # 视频截图完成后恢复原先的播放状态
        self.player.stop()
        self.player.setVideoOutput(self.wgt_video)
        self.player.setPosition(self.grab_player_position)
        if self.grab_player_state == QMediaPlayer.PlayingState:
            self.player.play()

    def volumeChange(self, position):
        volume= round(position/self.sld_audio.maximum()*100)
        print("vlume %f" %volume)
        self.player.setVolume(volume)
        self.lab_audio.setText("volume:"+str(volume)+"%")

    def clickedSlider(self, position):
        if self.player.duration() > 0:  # 开始播放后才允许进行跳转
            video_position = int((position / 100) * self.player.duration())
            self.player.setPosition(video_position)
            self.lab_video.setText("%.2f%%" % position)
        else:
            self.sld_video.setValue(0)

    def moveSlider(self, position):
        self.sld_video_pressed = True
        if self.player.duration() > 0:  # 开始播放后才允许进行跳转
            video_position = int((position / 100) * self.player.duration())
            self.player.setPosition(video_position)
            self.lab_video.setText("%.2f%%" % position)

    def pressSlider(self):
        self.sld_video_pressed = True
        print("pressed")

    def releaseSlider(self):
        self.sld_video_pressed = False

    def changeSlide(self, position):
        if not self.sld_video_pressed:  # 进度条被鼠标点击时不更新
            self.vidoeLength = self.player.duration()+0.1
            self.sld_video.setValue(round((position/self.vidoeLength)*100))
            self.lab_video.setText("%.2f%%" % ((position/self.vidoeLength)*100))

    def openVideoFile(self):
        self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))  # 选取视频文件
        self.player.play()  # 播放视频

    def playVideo(self):
        self.player.play()

    def pauseVideo(self):
        self.player.pause()

    def videoDoubleClicked(self, text):

        if self.player.duration() > 0:  # 开始播放后才允许进行全屏操作
            if self.videoFullScreen:
                self.player.setVideoOutput(self.wgt_video)
                self.videoFullScreenWidget.hide()
                self.videoFullScreen = False
            else:
                self.videoFullScreenWidget.show()
                self.player.setVideoOutput(self.videoFullScreenWidget)
                self.videoFullScreenWidget.setFullScreen(1)
                self.videoFullScreen = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    vieo_gui = myMainWindow()
    # qssFileName = "./py_code/style.qss"
    # qssFile = QSSLoad.readQssFile(qssFileName)
    # vieo_gui.setStyleSheet(qssFile)
    vieo_gui.show()
    sys.exit(app.exec_())
