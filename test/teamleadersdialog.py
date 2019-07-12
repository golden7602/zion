# @Author  : 张帆
# @Site    : 
# @File    : teamleadersdialog.py
# @Software: PyCharm
import sys
 
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QDialog, QListView, QAbstractItemView, QDialogButtonBox, QVBoxLayout, QTableView, \
    QApplication
 
from currencymodel import CurrencyModel
 
 
class TeamLeadersDialog(QDialog):
    def __init__(self, leaders):
        super(TeamLeadersDialog, self).__init__()
 
        self.model = QStringListModel(self)
        self.model.setStringList(leaders)
 
        self.listView = QListView()
        self.listView.setModel(self.model)
        self.listView.setEditTriggers(QAbstractItemView.AnyKeyPressed | QAbstractItemView.DoubleClicked)
        self.buttonBox = QDialogButtonBox()
        self.insertButton = self.buttonBox.addButton("Insert", QDialogButtonBox.ActionRole)
        self.deleteButton = self.buttonBox.addButton("Delete", QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(QDialogButtonBox.Ok)
        self.buttonBox.addButton(QDialogButtonBox.Cancel)
        self.insertButton.clicked.connect(self.insert)
        self.deleteButton.clicked.connect(self.del_)
        self.currencyMap = {
            "header": ["姓名", "性别", "年龄"],
            "data": [["张帆", "男", 24], ["张帆", "男", 24], ["张帆", "男", 24], ["张帆", "男", 24], ["张帆", "男", 24],
                     ["张帆", "男", 24]]
        }
        self.currencyModel = CurrencyModel(self.currencyMap.get('data'),self.currencyMap.get('header'))
        self.tableView = QTableView()
        self.tableView.setModel(self.currencyModel)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setWindowTitle("Currencies")
        self.tableView.show()
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.listView)
        self.mainLayout.addWidget(self.buttonBox)
        self.mainLayout.addWidget(self.tableView)
        self.setLayout(self.mainLayout)
        self.setWindowTitle("Team leaders")
        self.count = 0
 
    def leaders(self):
        return self.model.stringList()
 
    def insert(self):
        row = self.model.rowCount()
        print(row)
        self.model.insertRow(row)
        index = self.model.index(row)
        self.model.setData(index,"123")
        currencyMap = {
            "header": ["姓名", "性别", "年龄"],
            "data": [["张帆", "男", 242], ["张帆", "男", 24], ["张帆", "男", 24], ["张帆", "男", 24], ["张帆", "男", 24],
                     ["张帆", "男", 24],['sdaf','asdf','asdf']]
        }
        x = self.tableView.currentIndex()
 
        self.currencyModel.append_data(['zhangfan','nf',str(self.count)])
        self.count+=1
        print(self.currencyModel.data)
 
 
 
    def del_(self):
        self.model.removeRows(self.listView.currentIndex().row(), 1)
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    leaders = ['1','2','3','4','5','6','6']
    teamLeadersDialog = TeamLeadersDialog(leaders)
    teamLeadersDialog.show()
