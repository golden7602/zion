from PyQt5 import QtGui, QtCore ,QtWidgets
import sys, os

class Check_ComboBox(QtWidgets.QComboBox):
    def __init__(self):
        super(Check_ComboBox, self).__init__()
        self.view().pressed.connect(self.handleItemPressed)
        self.setModel(QtGui.QStandardItemModel(self))

    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == QtCore.Qt.Checked:
            item.setCheckState(QtCore.Qt.Unchecked)
        else:
            item.setCheckState(QtCore.Qt.Checked)


class myWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(QtWidgets.QMainWindow, self).__init__()
        self.setWindowTitle("custom_combobox")
        myQWidget = QtWidgets.QWidget()
        myBoxLayout = QtWidgets.QVBoxLayout()
        myQWidget.setLayout(myBoxLayout)
        self.setCentralWidget(myQWidget)
        self.ComboBox = Check_ComboBox()
        for i in range(10):
            self.ComboBox.addItem("Class studnet " + str(i))
            item = self.ComboBox.model().item(i, 0)
            item.setCheckState(QtCore.Qt.Unchecked)
        self.toolbutton = QtWidgets.QToolButton(self)
        self.toolbutton.setText('age information')
        self.toolmenu = QtWidgets.QMenu(self)
        for i in range(5):
            action = self.toolmenu.addAction("2" + str(i))
            action.setCheckable(True)
        self.toolbutton.setMenu(self.toolmenu)
        self.toolbutton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        myBoxLayout.addWidget(self.toolbutton)
        myBoxLayout.addWidget(self.ComboBox)
        self.resize(260,120)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ap = myWindow()
    ap.show()
    sys.exit(app.exec_())
