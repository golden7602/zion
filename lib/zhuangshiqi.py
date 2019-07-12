from PyQt5.QtCore import QDate, QModelIndex, Qt, pyqtSignal

a=QDate.fromString("2019-02-23","yyyy-MM-dd")
b=QDate.toString()
print(str(a))

