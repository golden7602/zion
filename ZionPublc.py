import os
import sys
sys.path.append(os.getcwd())

from lib.JPDatebase import JPMySqlSingleTableQuery as JPQ, JPDb
from lib.JPFunction import Singleton


@Singleton
class _JPUser():
    Name = None
    ID = None
    __AllUser = []
    __AllRight = []

    @staticmethod
    def reFreshAllUser():
        return JPQ(
            "select fUserID,fUsername,fPassword from sysusers where fUserID>1")()

    def __init__(self):
        self.__AllRight = JPQ(
            "select fID, fUserID,fRightID,fHasRight from sysuserright")()
        self.__AllUser = self.reFreshAllUser()

    def currentUserRight(self):
        rt = self.__AllRight
        if rt and self.ID:
            return [r for r in rt if r[0] == self.ID]
        else:
            return []

    def setCurrentUserID(self, user_id: int):
        self.ID = user_id
        self.Name = [r[1] for r in self.__AllUser][0]

    def getAllUserList(self)->list:
        return [r[0:2] for r in self.__AllUser]

    def getAllUserEnumList(self) -> list:
        return [[r[1],r[0]] for r in self.__AllUser]

    def __bool__(self):
        return self.Name and self.ID


@Singleton
class JPPub():
    def __init__(self):
        self.user = _JPUser()
        self.customerList = JPQ('''select fCustomerName,fCustomerID,fNUIT,
                            fCity,fContato from t_customer''')()
        self.__allCustomerList = JPQ(
            'select fCustomerName,fCustomerID,fNUIT,fCity,fContato from t_customer')()
        def getEnumDict() -> dict:
            cur = JPDb().currentConn.cursor()
            cur.execute('''select fTypeID,fTitle,fItemID,fSpare1,
                        fSpare2,fNote from t_enumeration''')
            return {
                k: [row1[1:] for row1 in cur._rows if row1[0] == k]
                for k in set(row[0] for row in cur._rows)
            }
        self.__EnumDict = getEnumDict()

    def getEnumList(self, enum_type_id: int):
        return self.__EnumDict[enum_type_id]
    
    def getCustomerList(self):
        return self.__allCustomerList
