from PyQt5.QtSql import QSqlDatabase

import ctypes


class aa():
    def __init__(self):
        #ctypes.windll.LoadLibrary( 'C:/Users/Administrator.USER-20190111RX/AppData/Local/Programs/Python/Python37/Lib/site-packages/PyQt5/Qt/bin/libmysql.dll')
        self.con2 = QSqlDatabase.addDatabase('QMYSQL')
        self.con2.setHostName("127.0.0.1")
        self.con2.setDatabaseName("myorder_python")
        self.con2.setUserName("root")
        self.con2.setPassword("1234")
        self.con2.setPort(3366)
        a = self.con2.open()


aa()
