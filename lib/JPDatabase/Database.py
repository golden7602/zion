from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from configparser import ConfigParser
from functools import singledispatch

from pymysql import (connect as mysql_connect, cursors as mysql_cursors)

from lib.JPDatabase.Field import JPFieldInfo, JPMySQLFieldInfo
from lib.JPFunction import Singleton


class JPDbType(object):
    MySQL = 1
    SqlServer = 2
    Acdess = 3


@Singleton
class JPDb(object):
    def __init__(self):
        self.__currentConn = None

    def setDatabaseType(self, db_type: JPDbType):
        self.__db_type = db_type
    @property
    def currentConn(self):
        if self.__db_type == JPDbType.MySQL:
            if self.__currentConn is None:
                config = ConfigParser()
                config.read("config.ini", encoding="utf-8")
                kw = dict(config._sections["database"])
                self.__currentConn = mysql_connect(host=kw["host"],
                                                   user=kw["user"],
                                                   password=kw["password"],
                                                   database=kw["database"],
                                                   port=int(kw['port']))
            return self.__currentConn
        if self.__db_type == JPDbType.SqlServer:
            pass

        if self.__db_type == JPDbType.SqlServer:
            pass

    # 生成一个空对象
    def getFeildsInfoAndData(self, sql) -> JPFieldInfo:
        if self.__db_type == JPDbType.MySQL:
            cur = self.currentConn.cursor()
            try:
                cur.execute(sql)
            except Exception as e:
                raise ValueError('SQL语句或表名格式不正确!\n{}\n'.format(sql) + str(e))

            covsdict = JPMySQLFieldInfo.getConvertersDict()
            flds = [JPMySQLFieldInfo(item) for item in cur._result.fields]
            rs = cur._result.rows
            cover = [covsdict[fld.TypeCode] for fld in flds]
            datas = []
            for i in range(len(rs)):
                datas.append([cover[j](v) for j, v in enumerate(rs[i])])
            return flds, datas

    def NewPkSQL(self, role_id: int):
        if self.__db_type == JPDbType.MySQL:
            return [[
                """
                SELECT CONCAT(fPreFix,
                        if(fHasDateTime,
                        DATE_FORMAT(CURRENT_DATE(),
                        replace(replace(replace(replace(fDateFormat,
                        'yyyy','%Y'),'yy','%y'),'mm','%m'),'dd','%d')),''),
                        LPAD(fCurrentValue+1, fLenght , 0)) into @PK
                FROM systabelautokeyroles
                WHERE fRoleID={};""".format(role_id)
            ],
                    [
                        """
                UPDATE systabelautokeyroles 
                    SET fCurrentValue=@fCurrentValue+1 
                WHERE fRoleID={};""".format(role_id)
                    ]]

    def getDataList(self, sql: str) -> list:
        if self.__db_type == JPDbType.MySQL:
            cur = self.currentConn.cursor()
            try:
                cur.execute(sql)
            except Exception as e:
                raise ValueError('SQL语句或表名格式不正确!\n{}\n'.format(sql) + str(e))
        return [list(r) for r in cur._result.rows]

    def getDict(self, sql) -> dict:
        if self.__db_type == JPDbType.MySQL:
            cur = self.currentConn.cursor()
            try:
                cur.execute(sql)
            except Exception as e:
                raise ValueError('SQL语句或表名格式不正确!\n{}\n'.format(sql) + str(e))

            covsdict = JPMySQLFieldInfo.getConvertersDict()
            flds = [JPMySQLFieldInfo(item) for item in cur._result.fields]
            rs = cur._result.rows
            cover = [covsdict[fld.TypeCode] for fld in flds]
            datas = []
            for i in range(len(rs)):
                datas.append({
                    flds[j].FieldName: cover[j](v)
                    for j, v in enumerate(rs[i])
                })
            return datas

    def getOnlyStrcFilter(self):
        if self.__db_type == JPDbType.MySQL:
            return " Limit 0"

    def __getattr__(self, name):
        if name == '_JPDb__db_type':
            raise AttributeError("应在第一使用JPDb类时，先调用其setDatabaseType方法指定数据库类型")


if __name__ == "__main__":
    db = JPDb()
    db.setDatabaseType(JPDbType.MySQL)
    sql = "select * from t_order"
    a = db.getDict(sql)
    print(a)