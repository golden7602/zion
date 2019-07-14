# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.getcwd())

import configparser
from configparser import ConfigParser

from pymysql import connect, cursors
from pymysql.constants import FIELD_TYPE

from lib.JPFunction import Singleton, JPDateConver


@Singleton
class JPDb(object):
    def __init__(self):
        self.__currentConn = None

    @property
    def currentConn(self):
        if self.__currentConn is None:
            config = ConfigParser()
            config.read("config.ini", encoding="utf-8")
            kw = dict(config._sections["database"])
            self.__currentConn = connect(host=kw["host"],
                                         user=kw["user"],
                                         password=kw["password"],
                                         database=kw["database"],
                                         port=int(kw['port']))
        return self.__currentConn


class JPFieldType(object):
    Int = 1
    Float = 2
    String = 3
    Date = 4
    Boolean = 5
    Other = 0


class JPFieldInfo(JPFieldType):
    def __init__(self):
        self.FieldName = None
        self.Title = None
        self._type_code = None
        self.Scale = None
        self.Length = None
        self.NotNull = None
        self.IsPrimarykey = None
        self.NoDefaultValue = None
        self.Auto_Increment = None
        self.DefaultValue = None
        self.Comment = None
        self.RowSource = None
        self.Formula = None
        self.Value = None


class JPMySQLFieldInfo(JPFieldInfo):
    NOT_NULL_FLAG = 1
    PRI_KEY_FLAG = 2
    UNIQUE_KEY_FLAG = 4  #唯一约束
    MULTIPLE_KEY_FLAG = 8  #复合主键
    BLOB_FLAG = 16
    UNSIGNED_FLAG = 32  # 无符号
    ZEROFILL_FLAG = 64  # 前导零
    BINARY_FLAG = 128
    ENUM_FLAG = 256
    AUTO_INCREMENT_FLAG = 512  #自动编号
    TIMESTAMP_FLAG = 1024
    NO_DEFAULT_VALUE_FLAG = 4096
    PART_KEY_FLAG = 16384
    tp = {
        FIELD_TYPE.TINY: JPFieldInfo.Int,
        FIELD_TYPE.SHORT: JPFieldInfo.Int,
        FIELD_TYPE.LONG: JPFieldInfo.Int,
        FIELD_TYPE.LONGLONG: JPFieldInfo.Int,
        FIELD_TYPE.INT24: JPFieldInfo.Int,
        FIELD_TYPE.YEAR: JPFieldInfo.Int,
        FIELD_TYPE.DECIMAL: JPFieldInfo.Float,
        FIELD_TYPE.FLOAT: JPFieldInfo.Float,
        FIELD_TYPE.DOUBLE: JPFieldInfo.Float,
        FIELD_TYPE.NEWDECIMAL: JPFieldInfo.Float,
        FIELD_TYPE.VARCHAR: JPFieldInfo.String,
        FIELD_TYPE.JSON: JPFieldInfo.String,
        FIELD_TYPE.VAR_STRING: JPFieldInfo.String,
        FIELD_TYPE.STRING: JPFieldInfo.String,
        FIELD_TYPE.DATE: JPFieldInfo.Date,
        FIELD_TYPE.DATETIME: JPFieldInfo.Date,
        FIELD_TYPE.NEWDATE: JPFieldInfo.Date,
        FIELD_TYPE.TIMESTAMP: JPFieldInfo.Date,
        FIELD_TYPE.BIT: JPFieldInfo.Boolean
    }
    sqlValueCreater = {
        JPFieldInfo.Int:
        lambda x: "'{}'".format(x),
        JPFieldInfo.Float:
        lambda x: "'{}'".format(x),
        JPFieldInfo.String:
        lambda x: "'{}'".format(x),
        JPFieldInfo.Date:
        lambda x: "'{}'".format(JPDateConver(x, str)),
        JPFieldInfo.Boolean:
        lambda x: "'{}'".format(ord(x) if isinstance(x, bytes) else x),
        JPFieldInfo.Other:
        lambda x: "'{}'".format(x)
    }

    def __init__(self, cursors_field):
        super().__init__()
        f = cursors_field
        fl = JPMySQLFieldInfo
        self.FieldName = f.org_name
        self.Title = f.name
        self._type_code = f.type_code
        self.Scale = f.scale
        self.Length = f.length
        self.NotNull = f.flags & fl.NOT_NULL_FLAG != 0
        self.IsPrimarykey = f.flags & fl.PRI_KEY_FLAG != 0
        self.NoDefaultValue = f.flags & fl.NO_DEFAULT_VALUE_FLAG != 0
        self.Auto_Increment = f.flags & fl.AUTO_INCREMENT_FLAG != 0

    @property
    def TypeCode(self):
        try:
            return self.tp[self._type_code]
        except KeyError:
            return 0

    def sqlValue(self, value=None):
        v = value if value else self.Value
        if self.NotNull and v is None:
            raise ValueError(
                "字段[{title}]的值不能为空!\nField[{title}] not be Empty!",
                format(title=self.Title))
        t = self.TypeCode
        if v is None:
            return 'Null'
        return self.sqlValueCreater[t](v)


def jpGetDataListAndFields(sql: str) -> list:
    '''根据查询语句返回一个列表'''
    cur = JPDb().currentConn.cursor()
    cur.execute(sql)
    l=[list(row) for row in cur._result.rows]
    f=[JPMySQLFieldInfo(item) for item in cur._result.fields]
    return l,f

# class JPMySqlFeildsInfo():
#     def __init__(self):



class JPMySqlSingleTableQuery(object):
    def __init__(self, sql: str, only_structure: bool = False):
        '''根据指定的SQl,返回一个对象。SQL中一般使用一个表。\n
        对于SQL中包含复杂语句、多表连接时，生成SQL相关功能将失效。\n
        增加记录使用本类时，only_structure请指定为真，\n
        将自动在sql后加上 " limit 0" 以只返回一个结构。
        '''
        cur = JPDb().currentConn.cursor()
        cur.execute(sql)
        self.Fields = [JPMySQLFieldInfo(item) for item in cur._result.fields]
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

    def getRecordFieldInfo(self, row) -> JPMySQLFieldInfo:
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


if __name__ == "__main__":
    print(jpGetDataListAndFields("select * from t_order"))
