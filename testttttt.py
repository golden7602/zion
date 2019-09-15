import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLineEdit, QAction
 
 
class MyDateEdit(QLineEdit):
    check_signal = pyqtSignal(bool)         # 验证输入日期是否正确信号
    show_signal = pyqtSignal()              # 点击下拉框发送信号
 
    def __init__(self, init_date=QDate(), parent=None):
        super(MyDateEdit, self).__init__(parent=parent)
        self.my_date = init_date
 
        # 初始化外观
        self.resize(150, 20)
        self.setInputMask(r'9999/99/99;_')
        self.setText(self.my_date.toString('yyyy/MM/dd'))
 
        self.show_action = QAction(self)
        self.show_action.setIcon(QIcon('down.ico'))
        self.addAction(self.show_action, QLineEdit.TrailingPosition)
 
        # 信号和槽连接
        self.show_action.triggered.connect(self._show_calendar_func)
 
    def _show_calendar_func(self):
        """
        发射显示日历信号
        :return: None
        """
        self.show_signal.emit()
 
    def _check_input_func(self, year, month, day):
        """
        判断日期是否正确
        :param year:
        :param month:
        :param day:
        :return: True or False
        """
        # 年部分必须填满四个数
        if len(year) != 4:
            return False
 
        # 月部分必须填满两个数
        if len(month) != 2:
            return False
        else:
            # 填满的话必须小于12
            if int(month) > 12:
                return False
 
        # 日部分必须填满两个数
        if len(day) != 2:
            return False
        else:
            # 填满的话必须小于31
            if int(day) > 31:
                return False
 
        # 上面如果都符合，则用QDate.isValid()方法判断日期是否合理
        if not QDate.isValid(int(year), int(month), int(day)):
            return False
        return True
 
    def date(self):
        """
        获取日期
        :return:self.my_date(QDate类型)
        """
        # 获取日期中的年月日部分
        year = self.text().split('/')[0]
        month = self.text().split('/')[1]
        day = self.text().split('/')[2]
 
        # 进行判断，合理则发送日期，不合理发送信号
        check_result = self._check_input_func(year, month, day)
        if check_result:
            self.my_date = QDate(int(year), int(month), int(day))
            self.check_signal.emit(True)
            return self.my_date
        else:
            self.check_signal.emit(False)
 
    def setDate(self, QDate):
        """
        设置日期
        :param QDate: QDate类型参数
        :return: None
        """
        self.setText(QDate.toString(self.display_format))
 
 
class MyCalendar(QCalendarWidget):
    date_signal = pyqtSignal(str)         # 发送日期信号
 
    def __init__(self, parent=None):
        super(MyCalendar, self).__init__(parent=parent)
        self.clicked.connect(self._set_calendar_date_func)
        self.hide()
 
    def _set_calendar_date_func(self):
        """
        将输入框文本设置为日历上选择的日期，并将日历隐藏
        :return: None
        """
        my_date = self.selectedDate().toString('yyyy/MM/dd')
        self.date_signal.emit(my_date)
        self.hide()
 
 
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)
        self.my_date = MyDateEdit(QDate(2018, 12, 28), self)
        self.my_date.show_signal.connect(self.show_calendar_func)
        self.calendar = MyCalendar(self)
        self.calendar.date_signal.connect(self.set_calendar_date_func)
 
    def show_calendar_func(self):
        if self.calendar.isHidden():
            self.calendar.show()
            self.calendar.setGeometry(self.my_date.x(), self.my_date.height(), 240, 200)
        else:
            self.calendar.hide()
 
    def set_calendar_date_func(self, date):
        self.my_date.setText(date)
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
