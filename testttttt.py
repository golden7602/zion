import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QHBoxLayout,QLabel
from PyQt5.QtGui import QIcon,QPixmap,QImage
from PyQt5 import QtCore
from PIL import Image

class FirstMainWin(QWidget):

    def __init__(self):
        super(QWidget,self).__init__()
        self.initUI()

        # 设置窗口的尺寸

        self.setWindowTitle('显示图像')
        # self.status = self.statusBar()
        #
        # self.status.showMessage('只存在5秒的消息',5000)

    def initUI(self):
        self.resize(800, 300)
        self.move(300, 200)
        self.lbl = QLabel(self)
        self.pil_image=QImage('D:\pycode20100406\pycode\data\login\任达华.jpg')

        self.fcku(self.pil_image)


        #self.show()
        self.timer = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率

        self.timer.timeout.connect(lambda:self.fcku(self.pil_image))
        self.timer.start(10)

    def fcku(self,fckimage):
        # hbox = QHBoxLayout(self)
        #print(fckimage.size())
        pil_image = self.m_resize(self.width(), self.height(), fckimage)
        # fckimage=cv2.cvtColor(fckimage,cv2.COLOR_RGB2BGR)
        #fckimage = QImage(fckimage.width, fckimage.height, QImage.Format_RGB888)
        # print(fckimage.width)

        pixmap = QPixmap.fromImage(pil_image)
        # print(pixmap.height())
        # pixmap = self.m_resize(self.width(), self.height(), pixmap)
        self.lbl.resize(pil_image.width(),pil_image.height())
        self.lbl.setPixmap(pixmap)
        #print(pixmap.size())
        # hbox.addWidget(lbl)
        # self.setLayout(hbox)

    def m_resize(self,w_box, h_box, pil_image):  # 参数是：要适应的窗口宽、高、Image.open后的图片

        w, h = pil_image.width(), pil_image.height() # 获取图像的原始大小

        f1 = 1.0*w_box/w
        f2 = 1.0 * h_box / h

        factor = min([f1, f2])

        width = int(w * factor)

        height = int(h * factor)
        #return pil_image.resize(width, height)
        return pil_image.scaled(width, height)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('D:\JinptConfig\桌面2018\111.jpg'))
    main = FirstMainWin()
    main.show()

    sys.exit(app.exec_())
