# -*- coding: utf-8 -*-

from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

import configparser
from configparser import ConfigParser

from pymysql import connect, cursors
from pymysql.constants import FIELD_TYPE
from PyQt5.QtCore import Qt, QModelIndex, QDate
from lib.JPFunction import Singleton, JPDateConver
from abc import abstractmethod








def getDict(sql) -> dict:
    db = JPDb()
    cursor = db.currentConn.cursor(cursors.DictCursor)
    cursor.execute(sql)
    return cursor.fetchall()




class JPTabelRowData(object):
    New = 0
    OriginalValue = 1
    Update = 2

    def __init__(self, value: [list, int]):
        super().__init__()
        if isinstance(value, list):
            self.__data = value
            self._state = self.OriginalValue
        elif isinstance(value, int):
            self.__data = [None] * value
            self.OriginalValue = self.New
        else:
            raise ValueError("参数值错误")

    @property
    def State(self) -> int:
        return self.__state

    @property
    def InteriorData(self):
        return self.__data

    def __len__(self):
        return len(self.__data)

    def __getitem__(self, key):
        return self.__data[key]

    def __setitem__(self, key, value):
        self.__data[key] = value
        self.__state = self.Update

    def __iter__(self):
        self.__curIndex = 0
        return self

    def __next__(self):
        if self.__curIndex < len(self.__data):
            r = self.__data[self.__curIndex]
            self.__curIndex += 1
            return r
        else:
            raise StopIteration


#等删除
# class JPRowFieldInfo(object):
#     def __init__(self, fields: list):
#         """代表无数据的一组字段信息
#         fields 字段信息列表,类型
#         """
#         self.__rowData = None
#         self.__fields = fields
#         self.__fieldsDict = {
#             f.FieldName: i
#             for i, f in enumerate(self.__fields)
#         }

#     def setRowData(self, values: list):
#         for i, data in enumerate(values):
#             self.__fields[i].Value = data
#         self.__rowData = values

#     def __getitem__(self, key) -> JPFieldInfo:
#         """key可为顺序号或字段名"""
#         index = None
#         if isinstance(key, int):
#             index = key
#         elif isinstance(key, str):
#             index = self.__fieldsDict[key]
#         fld = self.__fields[index]
#         if self.__rowData:
#             fld.Vlaue = self.__rowData[index]
#         else:
#             fld.Vlaue = None
#         return fld

#     def __iter__(self):
#         self.__curIndex = 0
#         return self

#     def __next__(self) -> JPFieldInfo:
#         if self.__curIndex < len(self.__fields):
#             fld = self.__fields[self.__curIndex]
#             fld.Value = self.__rowData[self.__curIndex]
#             self.__curIndex += 1
#             return fld
#         else:
#             raise StopIteration

#     def __len__(self):
#         return len(self.__fields)



def _getFieldAndData(sql):
    cur = JPDb().currentConn.cursor()
    try:
        cur.execute(sql)
    except Exception as e:
        raise ValueError('SQL语句或表名格式不正确!\n{}\n'.format(sql) + str(e))

    covsdict = _getClassFieldsInfo().getConvertersDict()
    flds = [_getClassFieldsInfo(item) for item in cur._result.fields]
    rs = cur._result.rows
    cover = [curCls._conver[fld.TypeCode] for fld in flds]
    datas = []
    for i in range(len(rs)):
        datas.append([covsdict[i](v) for v in rs[i]])
    return flds, datas


def getDataListAndFields(sql: str) -> list:
    '''根据查询语句返回一个列表'''
    cur = JPDb().currentConn.cursor()
    cur.execute(sql)
    l = [list(row) for row in cur._result.rows]
    f = [_JPMySQLFieldInfo(item) for item in cur._result.fields]
    return l, f


def JPGetFields(sql: str) -> list:
    '''
    根据查询语句返回一个列表，查询语句不包含条件，只包含字段信息
    结果也史包含字段信息
    '''
    cur = JPDb().currentConn.cursor()
    cur.execute(sql)
    return [_JPMySQLFieldInfo(item) for item in cur._result.fields]


class JPMySqlSingleTableQuery(object):
    def __init__(self, sql: str, only_structure: bool = False):
        '''根据指定的SQl,返回一个对象。SQL中一般使用一个表。\n
        对于SQL中包含复杂语句、多表连接时，生成SQL相关功能将失效。\n
        增加记录使用本类时，only_structure请指定为真，\n
        将自动在sql后加上 " limit 0" 以只返回一个结构。
        '''
        cur = JPDb().currentConn.cursor()
        cur.execute(sql)
        self.Fields = [_JPMySQLFieldInfo(item) for item in cur._result.fields]
        self.data = [list(row) for row in cur._result.rows]
        self.TableName = cur._result.fields[0].org_table
        self.__db = str(cur._result.fields[0].db, 'utf-8')  # 得到表名
        pklist = [[fld.FieldName, i] for i, fld in enumerate(self.Fields)
                  if fld.IsPrimarykey]
        if len(pklist) == 0:
            raise ValueError('查询语句:\n"{}"中未包含主键字段！'.format(sql))
        self.PkName, self.__PK_index = pklist[0]
        sql = """
            SELECT COLUMN_NAME,COLUMN_DEFAULT,COLUMN_COMMENT 
            FROM information_schema.`COLUMNS` 
            WHERE TABLE_SCHEMA='{}' AND TABLE_NAME='{}'"""
        cur.execute(sql.format(self.__db, self.TableName))
        for fld in self.Fields:
            fld.DefaultValue, fld.Comment = [
                row[1:] for row in cur._rows if row[0] == fld.FieldName
            ][0]
        self.__delPKs = []
        cur.close()

    def __call__(self):
        return self.data

    def __checkRowNum(self, i):
        if i not in range(len(self.data)):
            raise KeyError('记录行号超出范围!\nKey is out of range!')

    def getSQL(self,
               UpdateRowNumbers: list = None,
               MainTablePkName: str = None,
               MainTablePkValue: str = None) -> dict:
        """返回一组SQL语句，格式为：
        {"Delete"：str,"UPDATE":[,,,],"INSERT":[,,,]}
        """
        sd = self.data
        sf = self.Fields
        k_n = MainTablePkName
        k_v = MainTablePkValue
        pk_i = self.__PK_index
        # 更新主表主键值
        if all([k_n, k_v]):
            for fld in self.Fields:
                if fld.FieldName == k_n:
                    fld.Value = k_v

        if (1 if k_n else 0) + (1 if k_v else 0) == 1:
            raise ValueError("主键字段的值不能为空!\nPrimarykey not be Empty!")
        flds_no_pk = [fld for fld in self.Fields if not fld.IsPrimarykey]

        result = {}
        del_sql = "DELETR FROM {} WHERE {} IN ({})"
        result["DELETE"] = del_sql.format(
            self.TableName, self.PkName, ",".join(
                self.__delPKs)) if self.__delPKs else None

        result["UPDATE"] = []
        sql_upd = "UPDATE {} SET {} WHERE {}={}"
        for r in UpdateRowNumbers:
            self.__checkRowNum(r)
            self.__setValueToFieldsInfo(sd[r], k_n, k_v)
            temp_sql_v = [
                '{}={}'.format(fld.FieldName, flds_no_pk[i].sqlValue())
                for i, fld in enumerate(flds_no_pk)
            ]
            result["UPDATE"].append(
                sql_upd.format(self.TableName, ",".join(temp_sql_v),
                               sf[pk_i].FieldName, sf[pk_i].sqlValue()))

        result["INSERT"] = []
        ins_sql = "INSERT INTO {} ({}) VALUES ({})"
        ins_row = [row for row in sd if row[pk_i] is None]
        temp_fns = ",".join([fld.FieldName for fld in flds_no_pk])
        for row in ins_row:
            self.__setValueToFieldsInfo(row, k_n, k_v)
            temp_sql_v = ",".join([fld.sqlValue() for fld in flds_no_pk])
            result["INSERT"].append(
                ins_sql.format(self.TableName, temp_fns, temp_sql_v))
        return result

    def __setValueToFieldsInfo(self,
                               RowData,
                               MainTablePkName: str = None,
                               MainTablePkValue: str = None):
        bz = all([MainTablePkName, MainTablePkValue])
        for i, fld in enumerate(self.Fields):
            fld.Value = MainTablePkValue if all(
                [bz, fld.FieldName == MainTablePkName]) else RowData[i]

    def getRecordFieldInfo(self, row) -> JPFieldInfo:
        self.__checkRowNum(row)
        is_int = isinstance(row, int)
        for i, item in enumerate(self.Fields):
            item.Value = None
            item.Value = self.data[row][i] if is_int else row[i]
        for item in self.Fields:
            yield item

    def RecordsFieldInfo(self):
        """可迭代对象，迭代每一个FieldInfo对象"""
        for i in range(len(self.data)):
            yield self.getRecordFieldInfo(i)

    def delRow(self, row_num):
        self.__checkRowNum(row_num)
        self.__delPKs.append(str(self.data[row_num][self.__PK_index]))
        del self.data[row_num]

    def addNewRow(self):
        newrow = [
            None if fld.NoDefaultValue else fld.DefaultValue
            for fld in self.Fields
        ]
        self.data.append(newrow)

    def setFieldsRowSource(self, RowSource):
        '''设置字段数据来源，给一个字段设置数据来源，会使该字段的编辑控件为Combo
        可以同时设置多个，按字段名、行来源顺序设置就行
        '''
        args = RowSource
        if (len(args) % 2) != 0 or len(args) == 0:
            raise ValueError("参数个数必须为偶数，按字段名、行来源顺序排列")
        lst = list(zip(args[::2], args[1::2]))
        # 生成两两分组的一个列表
        for item in lst:
            if isinstance(item[0], str) and isinstance(item[1], (dict, list)):
                for fld in self.Fields:
                    if fld.FieldName == item[0]:
                        fld.RowSource = item[1]
                        continue
            else:
                raise ValueError("参数类型错误，奇数参数为字段名，偶数参数为列表")


#if __name__ == "__main__":
#a = getTabelFieldInfo("select * from t_order where 1>0")
