# -*- coding: utf-8 -*-
# @Time    : 18-12-1 下午3:26
# @Author  : 张帆
# @Site    : 
# @File    : currencymodel.py
# @Software: PyCharm
from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt
 
 
class CurrencyModel(QAbstractTableModel):
    def __init__(self,data:list,header):
        super(CurrencyModel, self).__init__()
        self.data = data
        self.header = header
 
 
    def append_data(self,x):
        self.data.append(x)
        self.layoutChanged.emit()
 
    def remove_row(self,row):
        self.data.pop(row)
        self.layoutChanged.emit()
 
    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.data)
 
    def columnCount(self, parent=None, *args, **kwargs):
        if len(self.data) > 0:
            return len(self.data[0])
        return 0
 
 
    def get_data(self):
        return self
    # 返回一个项的任意角色的值，这个项被指定为QModelIndex
    def data(self, QModelIndex, role=None):
        if not QModelIndex.isValid():
            print("行或者列有问题")
            return QVariant()
        # if role == Qt.TextAlignmentRole:
        #     return int(Qt.AlignRight | Qt.AlignVCenter)
        # elif role == Qt.DisplayRole:
        #     row = QModelIndex.row()
        #     column = QModelIndex.column()
        #     return self.currencyMap.get('data')[row][column]
        # # print("查数据")
        # row = QModelIndex.row()
        # # print('role:',role)
        # if role is None:
        #     return self.currencyMap.get('data')[row]
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.data[QModelIndex.row()][QModelIndex.column()])
 
 
    def headerData(self, p_int, Qt_Orientation, role=None):
        # if role != Qt.DisplayRole:
        #     return QVariant()
        # else:
        #     if Qt_Orientation == Qt.Horizontal:
        #         if len(self.currencyMap.get('header')) > p_int:
        #             return self.currencyMap.get('header')[p_int]
        if Qt_Orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.header[p_int])
        return QVariant
