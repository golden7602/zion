from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from Ui.Ui_FormConfig import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QMessageBox, QColorDialog
from lib.ZionPublc import JPPub
from PyQt5.QtCore import Qt
from lib.JPDatabase.Database import JPDb


class Form_Config(QDialog):
    @staticmethod
    def getRGBString(color):
        r = color.red()
        g = color.green()
        b = color.blue()
        return f'rgb({r}, {g}, {b})'

    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        pub = JPPub()
        super().__init__(parent=pub.MainForm, flags=flags)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        pub.MainForm.addOneButtonIcon(self.ui.colorpicker, 'color_picker.ico')
        # 读取信息
        self.configData = pub.getConfigData()
        # 写信息到窗体控件
        self.ui.Note_PrintingOrder.setText(
            self.configData['Note_PrintingOrder'])
        self.ui.Bank_Account.setText(self.configData['Bank_Account'])
        color = self.configData['Null_prompt_bac_color']
        c_str = Form_Config.getRGBString(color)
        self.ui.Null_prompt_bac_color.setStyleSheet(
            f"background-color: {c_str}")

        # 事件处理
        self.ui.Note_PrintingOrder.textChanged.connect(self.configChanged)
        self.ui.Bank_Account.textChanged.connect(self.configChanged)
        self.ui.colorpicker.clicked.connect(self.backColorSelect1)

        self.exec_()

    def configChanged(self):
        self.configData[
            'Note_PrintingOrder'] = self.ui.Note_PrintingOrder.text()
        self.configData['Bank_Account'] = self.ui.Bank_Account.text()

    def backColorSelect1(self):
        color = QColorDialog.getColor()
        if color:
            c_str = self.getRGBString(color)
            self.ui.Null_prompt_bac_color.setStyleSheet(
                f"background-color: {c_str}")
            self.configData['Null_prompt_bac_color'] = color

    def accept(self):
        JPPub().saveConfigData(self.configData)
        JPPub().ConfigData(True)
        QMessageBox.information(self, '',
                                '保存数据成功！\nSave datas complete!')
        self.close()
