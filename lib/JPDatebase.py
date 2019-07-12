# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.getcwd())

import configparser
from configparser import ConfigParser

from pymysql import connect, cursors
from pymysql.constants import FIELD_TYPE

from lib.JPFunction import Singleton, JPDateConver


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
        self.__db = str(cur._result.fields[0].db, 'utf-8')
        self.PkName, self.__PK_index = [[fld.FieldName, i]
                                        for i, fld in enumerate(self.Fields)
                                        if fld.IsPrimarykey][0]
        sql = "SELECT COLUMN_NAME,COLUMN_DEFAULT,COLUMN_COMMENT "
        sql += "FROM information_schema.`COLUMNS` WHERE TABLE_SCHEMA='{}' AND TABLE_NAME='{}'"
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

    # def getRowsAndFieldsInfo(self):
    #     pass

    # def getRecordFields(self,
    #                     tableName: str,
    #                     view_name: str = None,
    #                     pkvalue: str = None,
    #                     fields_name=[]):
    #     """按主表键值查询表中部分行,返回两个结果，一个是以字段信息为键值的字段信息对象字典，一个是表的主键名
    #     字段信息对象中，如果包含主键字段，其isPK属性设置为True
    #     """
    #     sql = "SELECT column_name FROM INFORMATION_SCHEMA.`KEY_COLUMN_USAGE` \
    #         WHERE table_name='{}' AND constraint_name='PRIMARY'"

    #     cur = self.currentConn.cursor()
    #     cur.execute(sql.format(tableName))
    #     pkname = cur._rows[0][0]
    #     cur = self.currentConn.cursor(cursors.DictCursor)
    #     f_l = '*' if len(fields_name) == 0 else ",".join(fields_name)
    #     if pkvalue is None:
    #         sql = "select {} from {} limit 0".format(f_l, tableName)
    #     else:
    #         tn = view_name if view_name else tableName
    #         sql = "select {} from {} where {}='{}'".format(
    #             f_l, tn, pkname, pkvalue)
    #     cur.execute(sql)
    #     dic = cur.fetchall()
    #     result = {
    #         row[0]:
    #         JPMySQLFieldInfo(*row[1:],
    #                          None if len(cur._rows) == 0 else dic[0][row[0]])
    #         for row in cur.description
    #     }
    #     if pkname in result:
    #         result[pkname].IsPK = True
    #     return result, pkname

    # def getRecordsDict(self, sql: str):
    #     """执行指定SQL,返回两个结果，一个是查询结果的字典列表，一个是以字段名为健、字段信息对象为值的字典"""

    #     cur = self.currentConn.cursor(cursors.DictCursor)
    #     cur.execute(sql)
    #     return cur.fetchall(), {
    #         row[0]: JPMySQLFieldInfo(*row)
    #         for row in cur.description
    #     }

    # def getRecordsAndFieldInfoTuple(self, sql: str):
    #     """执行指定SQL,返回两个结果，一个是查询结果的列表，一个是字段信息对象列表"""
    #     cur = self.currentConn.cursor()
    #     cur.execute(sql)
    #     return list(
    #         cur._rows), [JPMySQLFieldInfo(*row) for row in cur.description]

    # def getRecordsTuple(self, sql: str):
    #     """执行指定SQL,返回结果的列表"""
    #     cur = self.currentConn.cursor()
    #     cur.execute(sql)
    #     return list(cur._rows)

    def getEnumDict(self, sql: str) -> dict:
        """ 输入参数为一个查询语句sql，返回一个字典。
        sql格式：列1-枚举分类值，列2-提示文本；列3-为枚举值，其后依次为其他需返回值;

        返回值为字典，格式如{K:L,...},键K为枚举分类值；
        L格式如[(T,V...),...]：v枚举索引值,T为枚举提示文本，...依次为其他返回值
        """
        cur = self.currentConn.cursor()
        cur.execute(sql)
        return {
            k: [row1[1:] for row1 in cur._rows if row1[0] == k]
            for k in set(row[0] for row in cur._rows)
        }
