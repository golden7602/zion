import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
################################################

items_list = [
    "C", "C++", "Java", "Python", "JavaScript", "C#", "Swift", "go", "Ruby",
    "Lua", "PHP"
]


################################################
class Widget(QWidget):
    def __init__(self, *args, **kwargs):
        super(Widget, self).__init__(*args, **kwargs)
        layout = QHBoxLayout(self)
        self.lineedit = QLineEdit(self, minimumWidth=200)
        self.combobox = QComboBox(self, minimumWidth=200)
        self.combobox.setEditable(True)

        layout.addWidget(QLabel("QLineEdit", self))
        layout.addWidget(self.lineedit)
        layout.addItem(
            QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        layout.addWidget(QLabel("QComboBox", self))
        layout.addWidget(self.combobox)

        #初始化combobox
        self.init_lineedit()
        self.init_combobox()

        #增加选中事件
        self.combobox.activated.connect(self.on_combobox_Activate)

    def init_lineedit(self):
        # 增加自动补全
        self.completer = QCompleter(items_list)
        self.lineedit.setCompleter(self.completer)

    def init_combobox(self):
        # 增加选项元素
        for i in range(len(items_list)):
            self.combobox.addItem(items_list[i])
        self.combobox.setCurrentIndex(-1)

        # 增加自动补全
        self.completer = QCompleter(items_list)
        self.combobox.setCompleter(self.completer)

    def on_combobox_Activate(self, index):
        print(self.combobox.count())
        print(self.combobox.currentIndex())
        print(self.combobox.currentText())
        print(self.combobox.currentData())
        print(self.combobox.itemData(self.combobox.currentIndex()))
        print(self.combobox.itemText(self.combobox.currentIndex()))
        print(self.combobox.itemText(index))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())