# -*- coding: utf-8 -*-
from os import getcwd
from sys import path as jppath
jppath.append(getcwd())


from lib.JPDatabase.Database import JPDb
from lib.JPFunction import Singleton
from PyQt5.QtWidgets import QTreeWidgetItem, QMessageBox, QDialog
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QObject
from PyQt5.QtGui import QIcon, QPixmap
from Ui.Ui_FormUserLogin import Ui_Dialog as Ui_Dialog_Login
from Ui.Ui_FormChangePassword import Ui_Dialog as Ui_Dialog_ChnPwd
from lib.JPFunction import md5_passwd, setWidgetIconByName


class Form_ChangePassword(QDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.ui = Ui_Dialog_ChnPwd()
        self.ui.setupUi(self)
        self.ui.Login_64.setPixmap(
            QPixmap(getcwd() + "\\res\\ico\\{}".format("changepassword.png")))
        self.exec_()
    def accept(self):
        def msgbox(msg: str):
            QMessageBox.warning(self, '提示', msg, QMessageBox.Yes,
                                QMessageBox.Yes)

        old_pw = self.ui.OldPassword.text()
        new_pw = self.ui.NewPassowrd.text()
        new_pw2 = self.ui.ConfirmPassword.text()
        uid = JPUser().currentUserID()
        if not all((old_pw, new_pw, new_pw2)):
            msgbox('请完整输入！\nPlease complete the form')
            return False
        sql = """
            select fUserID from sysusers
             where fUserID='{uid}' and fPassword='{pwd}'
             """.format(uid=uid, pwd=md5_passwd(old_pw))
        if not JPDb().getDataList(sql):
            msgbox('密码错误！\nPassword error!')
            return False
        if new_pw != new_pw2:
            msgbox(
                '两次输入新密码不一致！\nYour confirmed password and new password do not match'
            )
            return False
        sql = """
            update sysusers set fPassword='{pwd}' 
            where fUserID='{uid}'""".format(uid=uid, pwd=md5_passwd(new_pw))
        result = JPDb().executeTransaction(sql)
        if result:
            msgbox('密码修改完成。\nSuccessful password modification.')
        self.close()


class Form_UserLogin(QDialog):
    def __init__(self, isLogin=True):
        super().__init__()
        self.ui = Ui_Dialog_Login()
        self.ui.setupUi(self)
        self.ui.Login_64.setPixmap(
            QPixmap(getcwd() + "\\res\\ico\\{}".format("login_64.png")))
        self.isLogin = isLogin
        us = JPUser()
        for r in [r for r in us.getAllUserList() if r[0] > 1]:
            self.ui.User.addItem('{} {}'.format(r[0], r[1]), r[0])
        self.ui.User.setCurrentIndex(-1)
        self.setWindowFlags(Qt.WindowTitleHint)
        if not isLogin:
            self.setWindowTitle("Change User")
            self.ui.label_Title.setText("Change User")
        self.exec_()

    def accept(self):
        def msgbox(msg: str):
            QMessageBox.warning(self, '提示', msg, QMessageBox.Yes,
                                QMessageBox.Yes)

        uid = self.ui.User.currentText()
        pwd = self.ui.Password.text()
        sql0 = """
            select fUserID from sysusers 
            where fUserName='{username}' and fPassword='{pwd}'"""
        sql1 = """
            select fUserID from sysusers 
            where fUserID='{uid}' and fPassword='{pwd}' 
                and ord(fEnabled)=1"""
        if all((pwd, uid)):
            isAdmin = 1 if uid.upper() == 'ADMIN' else 0
            if isAdmin:
                sql = sql0.format(pwd=md5_passwd(pwd), username=uid)
            else:
                sql = sql1.format(pwd=md5_passwd(pwd),
                                  uid=self.ui.User.currentData())
            lst = JPDb().getDict(sql)
            if lst:
                JPUser().setCurrentUserID(lst[0]['fUserID'])
                self.hide()
            else:
                msgbox('用户名或密码错误！\nUsername or password incorrect!')
        else:
            msgbox('用名或密码没有输入！')

    def reject(self):
        if not self.isLogin:
            self.hide()
        else:
            # 退出程序
            JPDb().close()
            exit()


@Singleton
class JPUser(QObject):
    __Name = None
    __ID = None
    __AllUser = []
    __CurrentUserRight = []
    userChange = pyqtSignal(list)
    FRM_LOGIN = None
    FRM_PASSOWRD = None

    def reFreshAllUser(self):
        db = JPDb()
        sql = """select fUserID,fUsername from sysusers where fUserID=1 or fEnabled=1"""
        self.__AllUser = db.getDataList(sql)

    def currentUserID(self):
        if self.__ID:
            return self.__ID
        self.FRM_LOGIN = Form_UserLogin()

    def changeUser(self):
        self.FRM_LOGIN = Form_UserLogin(False)

    def changePassword(self):
        self.FRM_PASSOWRD = Form_ChangePassword()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def INIT(self):
        self.reFreshAllUser()

    def __refreshCurrentUserRight(self):
        db = JPDb()
        uid = self.currentUserID()
        sql_1 = """
            SELECT 1, n.fNMID, n.fDispIndex, n.fParentId, 
                n.fMenuText, n.fObjectName, n.fIcon, 
                n.fIsCommandButton+0 AS fIsCommandButton, 
                1 as fHasRight
            FROM sysnavigationmenus n
				where n.fNMID in (1,11,13,135,136,137) or n.fDefault=1
        """
        sql_else = """
            SELECT ur.fUserID, n.fNMID, n.fDispIndex, n.fParentId, 
                n.fMenuText, n.fObjectName, n.fIcon, 
                n.fIsCommandButton+0 AS fIsCommandButton, 
                ur.fHasRight+0 as fHasRight
            FROM sysnavigationmenus n
                left JOIN (
                    SELECT *
                    FROM sysuserright
                    WHERE fUserID = {}
                ) ur
                ON n.fNMID = ur.fRightID
            WHERE (n.fEnabled = 1 and ur.fHasRight=1) or n.fDefault=1
            ORDER BY n.fParentId, n.fDispIndex
        """.format(uid)
        exesql = sql_1 if uid == 1 else sql_else
        re = db.getDict(exesql)
        menu = [r for r in re if r['fIsCommandButton'] == 0]
        for r in menu:
            r['btns'] = [
                b for b in re
                if b['fParentId'] == r['fNMID'] and b['fIsCommandButton'] == 1
            ]
        self.__CurrentUserRight = menu

    def currentUserRight(self):
        return self.__CurrentUserRight

    def setCurrentUserID(self, user_id: int):
        self.__ID = user_id
        self.Name = [r[1] for r in self.__AllUser if r[0] == self.__ID][0]
        self.__refreshCurrentUserRight()
        self.userChange.emit([self.__ID, self.Name])

    def getAllUserList(self) -> list:
        return [r[0:2] for r in self.__AllUser]

    def getAllUserEnumList(self) -> list:
        return [[r[1], r[0]] for r in self.__AllUser]

    def __bool__(self):
        return self.Name and self.__ID


@Singleton
class JPPub(QObject):
    MainForm = None

    def __init__(self):
        if self.MainForm is None:
            super().__init__()
            self.user = JPUser()
            self.db = JPDb()
            self.INITCustomer()
            self.INITEnum()

            sql = """
                SELECT fNMID, fMenuText, fParentId, fCommand, fObjectName, fIcon,
                        cast(fIsCommandButton AS SIGNED) AS fIsCommandButton
                FROM sysnavigationmenus
                WHERE fEnabled=1 AND fNMID>1
                ORDER BY fDispIndex
                """
            self.__sysNavigationMenusDict = self.db.getDict(sql)

    def INITEnum(self):
        def getEnumDict() -> dict:
            sql = '''select fTypeID,fTitle,fItemID,fSpare1,
                        fSpare2,fNote from t_enumeration'''
            rows = self.db.getDataList(sql)
            return {
                k: [row1[1:] for row1 in rows if row1[0] == k]
                for k in set(row[0] for row in rows)
            }

        self.__EnumDict = getEnumDict()

    def INITCustomer(self):
        sql = '''select fCustomerName,fCustomerID,
                fNUIT,fCity,fContato,fTaxRegCer from t_customer'''
        self.__allCustomerList = self.db.getDataList(sql)

    def getEnumList(self, enum_type_id: int):
        return self.__EnumDict[enum_type_id]

    def getCustomerList(self):
        return self.__allCustomerList

    def getSysNavigationMenusDict(self):
        return self.__sysNavigationMenusDict
