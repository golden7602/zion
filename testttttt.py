from PyQt5.QtWidgets import QApplication, QPushButton, QColorDialog, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
import sys
import json
from os import getcwd
from sys import argv
from sys import exit as sys_exit
from sys import path as jppath

jppath.append(getcwd())
import pickle
from PyQt5 import sip
from PyQt5.QtCore import QMetaObject, Qt, QThread
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
                             QProgressBar, QPushButton, QTreeWidgetItem,
                             QWidget)

from lib.JPDatabase.Database import JPDb, JPDbType
from lib.JPFunction import readQss, setWidgetIconByName, seWindowsIcon
from lib.ZionPublc import JPPub, JPUser
from Ui.Ui_FormMain import Ui_MainWindow
from lib.JPConfigInfo import ConfigInfo

from Ui.Ui_FormConfig import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QMessageBox
from lib.ZionPublc import JPPub
from PyQt5.QtCore import Qt
from lib.JPDatabase.Database import JPDb
from pymysql.converters import escape_string


class ColorDialog(QWidget):
    def __init__(self):
        super().__init__()

        self.configData = {
            'Note_PrintingOrder':
            JPDb().getOnConfigValue('Note_PrintingOrder', str),
            'Bank_Account':
            JPDb().getOnConfigValue('Bank_Account', str)
        }
        #颜色值
        color = QColor(0, 0, 0)
        #位置
        self.setGeometry(300, 300, 350, 280)
        #标题
        self.setWindowTitle('颜色选择')
        #按钮名称
        self.button = QPushButton('Dialog', self)
        self.button.setFocusPolicy(Qt.NoFocus)
        #按钮位置
        self.button.move(40, 20)
        #按钮绑定方法
        self.button.clicked.connect(self.showDialog)
        self.setFocus()
        self.widget = QWidget(self)
        self.widget.setStyleSheet('QWidget{background-color:%s} ' %
                                  color.name())
        self.widget.setGeometry(130, 22, 200, 100)

    def showDialog(self):
        sql = "update sysconfig set fValueInt=%s, fValue=%s where fName='configValue'"
        col = QColorDialog.getColor()
        self.configData['Null_prompt_bac_color'] = col
        s = pickle.dumps(self.configData)

        db = JPDb()
        conn = db.currentConn
        cur = JPDb().currentConn.cursor()
        cur.execute(sql, [222, s])
        conn.commit()


        self.configData = None
        sql = "select fValue from sysconfig where fName='configValue'"
        cur.execute(sql)
        s=cur._result.rows[0][0]
        #self.configData =
        if col.isValid():
            self.widget.setStyleSheet('QWidget {background-color:%s}' %
                                      col.name())




if __name__ == "__main__":

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setStyle('Fusion')
    app = QApplication(argv)
    db = JPDb()
    db.setDatabaseType(JPDbType.MySQL)

    qb = ColorDialog()
    qb.show()
    sys.exit(app.exec_())