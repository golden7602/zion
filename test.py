import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDateEdit
from lib import Ui_FormOrderMob
from lib.globalVar import pub

class ReadDataToUi(object):
    def __init__(self, tableName, PkName, PkValue,mainUI):
        fldsTP=pub.GetFieldsTypeDict(tableName)
        fTemp=pub.getDict("select * from {} where {}='{}'".format(tableName, PkName, PkValue))
        if len(fTemp)==0:
            return
        fv=fTemp[0]
        fldsName=fldsTP.keys() & mainUI.__dict__.keys()
        for n in fldsName:
            FieldType=fldsTP[n]
            item=mainUI.__dict__[n]
            FieldValue=fv[n]
            if not FieldValue:
                continue
            if FieldType in (1, 3, 8):  # TinyInt,Int
                item.setText(str(FieldValue))
            elif FieldType in (7, 10):  # TS,DATE
                pass
                #item.setText(str(FieldValue))
            elif FieldType == 16:  # Bit
                item.setText(str(ord(FieldValue)))
            elif FieldType == 246:  # Decimal
                item.setText('{:,.2f}'.format(FieldValue))
            elif FieldType in (253, 254):  # VChar,Char
                item.setText(str(FieldValue))
            else:  # other
                item.setText(str(FieldValue))
                    
    

class SaveDataToTabel(object):
    """ tableName 目标表名 PkName 主键字段名 mainUI 主表数据编辑窗口类，在本类中应该有以字段名命名的各种控件 """
    def __init__(self, tableName, PkName, mainUI):
        self.__fields={}
        self.__tableName=tableName
        self.__PkName=PkName
        self.__PkValue=None
        self.__SubSql={}
        for k in mainUI.__dict__:
            obj=mainUI.__dict__[k]
            if PkName.upper() == k.upper():
                self.__PkValue="'{}'".format(obj.text())
                continue
            if isinstance(obj,QtWidgets.QLineEdit) and obj.text():
                self.__fields[k]="'{}'".format(obj.text())
                continue
            if isinstance(obj,QtWidgets.QDateEdit):
                self.__fields[k]="'{}'".format(obj.text())
                continue
            if isinstance(obj,QtWidgets.QTextEdit) and obj.toPlainText():
                self.__fields[k]="'{}'".format(obj.toPlainText())
                continue
            if isinstance(obj,QtWidgets.QCheckBox):
                self.__fields[k]=int(obj.isChecked())
    def CreateNewPK(self,PkRoleID):
        dateStr=''
        db=pub.GetDatabase()
        sql='select fHasDateTime+0 as d ,fPreFix,fCurrentValue,fLenght,fDateFormat from systabelautokeyroles where fRoleID={}'.format(PkRoleID)
        tab=pub.getDict(sql)[0]
        cursor = db.cursor()
        sql_update = "update systabelautokeyroles set fCurrentValue=fCurrentValue+1 where fRoleID={}".format(PkRoleID)
        try:
            cursor.execute(sql_update)
            db.commit()
        except:
            db.rollback()
            return None
        if tab['d']==1:
            s=tab['fDateFormat'].replace('mm','MM')
            Qd=QDateEdit()
            Qd.setDate(QDate.currentDate())
            Qd.setDisplayFormat(s)
            dateStr=Qd.text()
        print(self.__dict__)
        return tab['fPreFix'] + dateStr + ("{:0>"+ str(tab['fLenght']) +"d}").format(tab['fCurrentValue']+1)
        
    def __setSubTableWidget(self,tableWidget):
        pass
    def __InsertSql(self,PkRoleID):
        self.__fields[self.__PkName]=self.CreateNewPK(PkRoleID)
        SQL="Insert into " + self.__tableName + " (" + ",".join(self.__fields.keys()) + ") VALUES (" + ",".join(self.__fields.values()) +")"
        return SQL
    def __UpdateSql(self):
        dict1=[]
        for k,v in self.__fields.items():
            dict1.append(str(k) + "=" + str(v))
        SQL="update " + self.__tableName +" set " + ",".join(dict1) + " where " + self.__PkName + "=" + self.__PkValue
        return SQL




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_FormOrderMob.Ui_Form()
    ui.setupUi(Form)
    ui.fOrderDate.setDate(QDate.currentDate())
    ui.fRequiredDeliveryDate.setDate(QDate.currentDate())
    def btn1():
        a=ReadDataToUi("v_order",'fOrderID','CP2019-0130000001',ui)
        #a=SaveData("order","fOrderID",ui)
        #print(a.CreateNewPK(1))
    ui.butSave.clicked.connect(btn1)















    Form.show()
    sys.exit(app.exec_())
