import datetime
from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

import re
from copy import deepcopy
from PyQt5.QtCore import QModelIndex
from lib.JPDatabase.Database import JPDb
from lib.JPDatabase.Field import JPFieldInfo
from PyQt5.QtWidgets import QMessageBox
from lib.JPFunction import JPGetDisplayText
from lib.ZionPublc import JPPub


class JPTabelRowData(object):
    New_None = -1
    New = 0
    OriginalValue = 1
    Update = 2

    def __init__(self, values_or_ColumnCount: [list, int]):
        """生成一个数据行对象
        JPTabelRowData(values_or_ColumnCount)
        参数为一个数据列表，或列数，当给定列数时，则生成一个空行对象，值全部为None
        """
        super().__init__()
        value = values_or_ColumnCount
        if isinstance(value, list):
            self.__data = value
            self._state = self.OriginalValue
        elif isinstance(value, int):
            self.__data = [None] * value
            self._state = self.New
        else:
            raise ValueError("参数值错误")

    @property
    def State(self) -> int:
        return self._state

    def Data(self, column):
        return self.__data[column]

    @property
    def Datas(self):
        return self.__data

    def setData(self, column, value):
        if self.__data[column] == value:
            return
        if self._state == self.OriginalValue:
            self._state = self.Update
        if self._state == self.New_None:
            self._state = self.New
        self.__data[column] = value


class JPQueryFieldInfo(object):
    New_None = -1
    New = 0
    OriginalValue = 1
    Update = 2

    @staticmethod
    def getRC(index: [list, tuple, QModelIndex]):
        if isinstance(index, (list, tuple)):
            if len(index) == 2:
                r, c = index
        elif isinstance(index, QModelIndex):
            r, c = index.row(), index.column()
        else:
            raise ValueError("参数错误,参数一只能为长度为2的list, tuple,或一个QModelIndex")
        return r, c

    def __init__(self, sql):
        '''返回一个只读的查询的数据信息，数据不可更改'''
        db = JPDb()
        flds, data = db.getFeildsInfoAndData(sql)
        # self.__isMain = True
        self.Fields = flds
        self.RowsData = [JPTabelRowData(row) for row in data]
        self.FieldsDict = {fld.FieldName: fld for fld in flds}
        for i in range(len(self.Fields)):
            self.Fields[i]._index = i

    def __len__(self):
        return len(self.RowsData)

    # def setMainSubMode(mode: bool):
    #     self.__self.__isMain = mode

    def getOnlyData(self, index: [list, tuple, QModelIndex]):
        """getOnlyData(index: [list, tuple, QModelIndex])
        根据指定的数据位置返回数据的值"""
        r, c = JPQueryFieldInfo.getRC(index)
        return self.RowsData[r].Data(c)

    def getDispText(self, index: [list, tuple, QModelIndex]):
        """getDispText(index: [list, tuple, QModelIndex])
        根据指定的数据位置返回数据的显示文本"""
        r, c = JPQueryFieldInfo.getRC(index)
        v = self.RowsData[r].Data(c)
        rs = self.Fields[c].RowSource
        if not v:
            return ''
        if rs:
            txts = [item[1] for item in rs if item[0] == v]
            if txts:
                return txts[0]
        else:
            return JPGetDisplayText(v)

    def getRowData(self, row_num) -> list:
        """根据指定的行号返回一个列表,仅仅包含数据"""
        return self.RowsData[row_num].Datas

    def getFieldsInfo(self):
        return self.Fields

    def getRowFieldsInfoAndData(self, row_num: int) -> list:
        """getRowFieldsInfoAndData(row_num: int)
        根据指定的行号返回一个列表，包含所有FieldInfo对象，且有Value属性"""
        flds = deepcopy(self.Fields)
        data = self.RowsData[row_num]
        for i, fld in flds:
            fld.Value = data[i]
        return flds

    def getRowFieldsInfoAndDataDict(self, row_num: int) -> dict:
        """getRowValueDict(row_num: int)
        根据指定的行号返回一个字典，键是字段名，值为FieldInfo对象，且有Value属性"""
        flds = deepcopy(self.Fields)
        data = self.RowsData[row_num].Datas
        r = {}
        for i, item in enumerate(data):
            flds[i].Value = item
            r[flds[i].FieldName] = flds[i]
        return r

    def getRowValueDict(self, row_num: int) -> dict:
        """getRowValueDict(row_num: int)
        根据指定的行号返回一个字典，键是字段名，值为数据"""
        data = self.RowsData[row_num].Datas
        r = {}
        for i, item in enumerate(data):
            r[self.Fields[i].FieldName] = item
        return r

    def getFieldsInfoDict(self) -> dict:
        """返回一个FieldsInfo对象的字典，键是字段名"""
        return self.FieldsDict

    def getFieldInfoAndData(self, index: [list, tuple,
                                          QModelIndex]) -> JPFieldInfo:
        """
         getFieldInfoAndData(index: [list, tuple,QModelIndex])-> JPFieldInfo
        根据行列返回一个包含Value属性的JPFieldInfo对象
        
        """
        r, c = self.getRC(index)
        fld = deepcopy(self.Fields[c])
        fld.value = self.RowsData[r][0][c]

    def setFieldsRowSource(self, key, data: list):
        '''setFieldsRowSource(key, data:list)\n
            key可以是序号或字段名
        '''
        if isinstance(key, str):
            self.FieldsDict[key].RowSource = data
        if isinstance(key, int):
            self.Fields[key].RowSource = data


class JPTabelFieldInfo(JPQueryFieldInfo):
    def __init__(self, sql: str, noData: bool = False):
        db = JPDb()
        '''根据一个Sql或表名返回一个JPTabelFieldInfo对象\n
        JPTabelFieldInfo(sql:str, noData:bool=False)
        '''
        self.PrimarykeyFieldName = None
        self.PrimarykeyFieldIndex = None
        self.TableName = None
        self.DeleteRows = []

        sql = re.sub(r'^\s', '', re.sub(r'\s+', ' ', re.sub(r'\n', '', sql)))
        sel_p = r"SELECT\s+.*from\s(\S+)\s"
        mt = re.match(sel_p, sql, flags=(re.I))
        self.TableName = mt.groups()[0] if mt else sql
        s_filter = db.getOnlyStrcFilter()
        if noData:
            # 找出不包含条件的SQL语句
            p_s = r"(SELECT\s+.*from\s(\S+)\s(as\s\S+)*)"
            mt1 = re.match(p_s, sql, flags=(re.I))
            sql = mt1.groups(
            )[0] + " " + s_filter if mt else 'Select * from {} {}'.format(
                self.TableName, s_filter) if mt else sql
        else:
            sql = sql if mt else 'Select * from {} {}'.format(sql, s_filter)
        super().__init__(sql)

        # 检查查询结果中是否包含主键,
        for i, fld in enumerate(self.Fields):
            if fld.IsPrimarykey is True:
                self.PrimarykeyFieldName = fld.FieldName
                self.PrimarykeyFieldIndex = i
        if self.PrimarykeyFieldIndex is None:
            raise ValueError('查询语句:\n"{}"中未包含主键字段！'.format(sql))
        # 检查主键字段是不是自增
        #pk_fld = self.getFieldsInfoDict()

    def setData(self, index: [list, tuple, QModelIndex], value=None):
        r, c = super().getRC(index)
        fld = self.Fields[c]
        conDict = fld.getConvertersDict()
        conver = conDict[fld.TypeCode]
        self.RowsData[r].setData(c, conver(value))

    def addRow(self):
        '''增加一行数据，全为None'''
        newRow = JPTabelRowData(len(self.Fields))
        newRow._state = JPTabelRowData.New_None
        self.RowsData.append(newRow)

    def deleteRow(self, row_num: int):
        self.DeleteRows.append(self.RowsData[row_num])
        del self.RowsData[row_num]

    # def ForeignKeyEnent(self, ForeignKeyRoleRole: int):
    #     """此方法必须重写，根据ForeignKeyRoleRole接收外键各参数
    #     """
    #     return self.ForeignKeyType_NoForeignKey

    # def __getSqlStatements(self,
    #                        Mainform,
    #                        isMainTable: bool = False,
    #                        foreignkey_col=None,
    #                        foreignkey_value=None):
    #     sql = []
    #     hasforeignkey = all((foreignkey_col, foreignkey_value))
    #     # 不能为空，不是自增列的列号，如果给定了外键值，则不检查该列
    #     if foreignkey_col and not foreignkey_value:
    #         raise ValueError("指定了外键列但没有指定值！")
    #     not_null_col = []
    #     for i in range(len(self.Fields)):
    #         fld = self.Fields[i]
    #         if all([fld.Auto_Increment is False, fld.NotNull is True]):
    #             if hasforeignkey:
    #                 if i != foreignkey_col:
    #                     not_null_col.append(i)
    #             else:
    #                 not_null_col.append(i)
    #     # 检查空值 如有不合要求的字段，则返回行号
    #     for r in range(len(self.RowsData)):
    #         for i in not_null_col:
    #             if (self.RowsData[r].State != JPTabelRowData.New) and (
    #                     self.RowsData[r].Datas[i] is None):
    #                 msg = "第{}行[{}]字段的值不能为空！".format(r + 1,
    #                                                  self.Fields[i].FieldName)
    #                 QMessageBox.warning(Mainform, '提示', msg, QMessageBox.Yes,
    #                                     QMessageBox.Yes)
    #                 return r
    #     # 开始生成语句
    #     sqls = []  # 存放结果
    #     m_t = self.TableName
    #     sql_i = 'INSERT INTO ' + m_t + ' ({}) VALUES ({});'
    #     sql_u = 'UPDATE ' + m_t + ' SET {} WHERE {}={};'
    #     fn_lst = [fld.FieldName for fld in self.Fields]
    #     pk_index = self.PrimarykeyFieldIndex

    #     for row in self.RowsData:
    #         if row.State == JPTabelRowData.OriginalValue or row.State == JPTabelRowData.New_None:
    #             continue
    #         cur_fn = deepcopy(fn_lst)
    #         cur_row_sqlvalue = [
    #             self.Fields[i].sqlValue(d) for i, d in enumerate(row.Datas)
    #         ]

    #         # 分主子表两种模式分别写

    #         if isMainTable is True:
    #             # 检查主键是不是自增
    #             if row.State == JPTabelRowData.New:
    #                 if self.Fields[pk_index].Auto_Increment:
    #                     del cur_row_sqlvalue[pk_index]
    #                     del cur_fn[pk_index]
    #                 else:
    #                     cur_row_sqlvalue[pk_index] = '@PK'
    #                 sqls.append(
    #                     sql_i.format(','.join(cur_fn),
    #                                  ','.join(cur_row_sqlvalue)))
    #             if row.State == JPTabelRowData.Update:
    #                 if not cur_row_sqlvalue[pk_index]:
    #                     raise ValueError("主键字段'{}'不能为空!".format(
    #                         self.PrimarykeyFieldName))
    #                 pk_value = cur_row_sqlvalue[pk_index]
    #                 del cur_row_sqlvalue[pk_index]
    #                 del cur_fn[pk_index]
    #                 temp = [
    #                     '{}={}'.format(n, v)
    #                     for n, v in zip(cur_fn, cur_row_sqlvalue)
    #                 ]
    #                 sqls.append(
    #                     sql_u.format(','.join(temp), self.PrimarykeyFieldName,
    #                                  pk_value))

    #         if isMainTable is False:
    #             if not self.Fields[pk_index].Auto_Increment:
    #                 raise ValueError("子表主键字段'{}'只能为自增加类型!".format(
    #                     self.PrimarykeyFieldName))
    #             if not foreignkey_col:
    #                 raise ValueError("子表必须指定外键列号")
    #             if row.State == JPTabelRowData.New:
    #                 if foreignkey_value:
    #                     cur_row_sqlvalue[foreignkey_col] = '{}'.format(
    #                         foreignkey_value)
    #                 else:
    #                     cur_row_sqlvalue[foreignkey_col] = '@PK'
    #                 del cur_row_sqlvalue[pk_index]
    #                 del cur_fn[pk_index]
    #                 sqls.append(
    #                     sql_i.format(','.join(cur_fn),
    #                                  ','.join(cur_row_sqlvalue)))
    #             if row.State == JPTabelRowData.Update:
    #                 pk_value = cur_row_sqlvalue[pk_index]
    #                 del cur_row_sqlvalue[pk_index]
    #                 del cur_fn[pk_index]
    #                 temp = [
    #                     '{}={}'.format(n, v)
    #                     for n, v in zip(cur_fn, cur_row_sqlvalue)
    #                 ]
    #                 sqls.append(
    #                     sql_u.format(','.join(temp), self.PrimarykeyFieldName,
    #                                  pk_value))

    #     return sqls

    def getSubSqlStatements(self, foreignkey_col: int, foreignkey_value=None):
        """
        getSubSqlStatements(foreignkey_col:int,foreignkey_value=None)
        返回子表的SQL语句，必须指定外键列号(主表键值对应列号)，外键值在Update模式时必须指定
        外键名在New模式时可不指定，将用主表新生成的主键替换“@PK”
        """
        pb = JPPub()
        appform = pb.MainForm
        sql = []
        hasforeignkey = all((foreignkey_col, foreignkey_value))
        # 不能为空，不是自增列的列号，如果给定了外键值，则不检查该列
        if foreignkey_col and not foreignkey_value:
            raise ValueError("指定了外键列但没有指定值！")
        not_null_col = []
        for i in range(len(self.Fields)):
            fld = self.Fields[i]
            if all([fld.Auto_Increment is False, fld.NotNull is True]):
                if hasforeignkey:
                    if i != foreignkey_col:
                        not_null_col.append(i)
                else:
                    not_null_col.append(i)
        # 检查空值 如有不合要求的字段，则返回行号
        for r in range(len(self.RowsData)):
            for i in not_null_col:
                if (self.RowsData[r].State != JPTabelRowData.New) and (
                        self.RowsData[r].Datas[i] is None):
                    msg = '第{row}行【{fn}】字段的值不能为空！\nRow {row} field [{fn}] cannot be empty!'.format(
                        row=r + 1, fn=self.Fields[i].FieldName)
                    QMessageBox.warning(appform, '提示', msg, QMessageBox.Yes,
                                        QMessageBox.Yes)
                    return r
        # 开始生成语句
        sqls = []  # 存放结果
        m_t = self.TableName
        sql_i = 'INSERT INTO ' + m_t + ' ({}) VALUES ({});'
        sql_u = 'UPDATE ' + m_t + ' SET {} WHERE {}={};'
        fn_lst = [fld.FieldName for fld in self.Fields]
        pk_index = self.PrimarykeyFieldIndex
        st = self.RowsData[0].State
        if not self.Fields[pk_index].Auto_Increment:
            raise ValueError("子表主键字段'{}'只能为自增加类型!".format(
                self.PrimarykeyFieldName))
                
        if st == JPTabelRowData.New:
            pass
        if st == JPTabelRowData.Update:
            pass
        for row in self.RowsData:
            if row.State == JPTabelRowData.OriginalValue or row.State == JPTabelRowData.New_None:
                continue
            cur_fn = deepcopy(fn_lst)
            cur_row_sqlvalue = [
                self.Fields[i].sqlValue(d) for i, d in enumerate(row.Datas)
            ]

            if not self.Fields[pk_index].Auto_Increment:
                raise ValueError("子表主键字段'{}'只能为自增加类型!".format(
                    self.PrimarykeyFieldName))
            if not foreignkey_col:
                raise ValueError("子表必须指定外键列号")
            if row.State == JPTabelRowData.New:
                if foreignkey_value:
                    cur_row_sqlvalue[foreignkey_col] = '{}'.format(
                        foreignkey_value)
                else:
                    cur_row_sqlvalue[foreignkey_col] = '@PK'
                del cur_row_sqlvalue[pk_index]
                del cur_fn[pk_index]
                sqls.append(
                    sql_i.format(','.join(cur_fn), ','.join(cur_row_sqlvalue)))
            if row.State == JPTabelRowData.Update:
                pk_value = cur_row_sqlvalue[pk_index]
                del cur_row_sqlvalue[pk_index]
                del cur_fn[pk_index]
                temp = [
                    '{}={}'.format(n, v)
                    for n, v in zip(cur_fn, cur_row_sqlvalue)
                ]
                sqls.append(
                    sql_u.format(','.join(temp), self.PrimarykeyFieldName,
                                 pk_value))
        return sqls

    def getMainSqlStatements(self):
        """返回主表的SQL语句，如果有检查空值错误，则引发一个错误，错误信息中包含字段名"""
        pb = JPPub()
        appform = pb.MainForm
        nm_lst = []
        v_lst = []
        ds = self.RowsData[0].Datas
        st = self.RowsData[0].State
        # 空值检查
        for fld in self.Fields:
            if fld.IsPrimarykey or fld.Auto_Increment:
                continue
            if fld.NotNull:
                if ds[fld._index] is None:
                    raise ValueError(fld)
                    msg = '字段【{fn}】的值不能为空！\nField [{fn}] cannot be empty!'.format(
                        fn=fld.FieldName)
                    QMessageBox.warning(appform, '提示', msg, QMessageBox.Ok,
                                        QMessageBox.Ok)
        # 空值检查完成
        sql_i = 'INSERT INTO ' + self.TableName + ' ({}) VALUES ({});'
        sql_u = 'UPDATE ' + self.TableName + ' SET {} WHERE {}={};'
        if (st == JPTabelRowData.New_None
                or st == JPTabelRowData.OriginalValue):
            return ''
        if st == JPTabelRowData.New:
            for fld in self.Fields:
                if fld.IsPrimarykey:
                    if fld.Auto_Increment:
                        continue
                    else:
                        nm_lst.append(fld.FieldName)
                        v_lst.append("@PK")
                else:
                    nm_lst.append(fld.FieldName)
                    v_lst.append(fld.sqlValue(ds[fld._index]))
            return sql_i.format(",".join(nm_lst), ",".join(v_lst))
        if st == JPTabelRowData.Update:
            for fld in self.Fields:
                if fld.IsPrimarykey:
                    r_pk_name = fld.FieldName
                    r_pk_v = fld.sqlValue(ds[fld._index])
                else:
                    nm_lst.append(fld.FieldName)
                    v_lst.append(fld.sqlValue(ds[fld._index]))
            temp = ['{}={}'.format(n, v) for n, v in zip(nm_lst, v_lst)]
            return sql_u.format(",".join(temp), r_pk_name, r_pk_v)

    # def getSubSqlStatements(self,
    #                         Mainform,
    #                         foreignkey_col,
    #                         foreignkey_value=None):
    #     return self.__getSqlStatements(Mainform, False, foreignkey_col,
    #                                    foreignkey_value)


if __name__ == "__main__":
    from lib.JPDatabase.Database import JPDbType, JPDb
    db = JPDb()
    db.setDatabaseType(JPDbType.MySQL)
    aa = JPQueryFieldInfo("""
        SELECT if(isnull(Q3.d), 'Sum', Q3.d) AS Day0
            , M1, M2, M3, M4, M5, M6, M7, M8, M9, M10
            , M11, M12
        FROM (
            SELECT Q1.d
                , IF(Q1.m = 1, Q1.j1, NULL) AS M1
                , IF(Q1.m = 2, Q1.j1, NULL) AS M2
                , IF(Q1.m = 3, Q1.j1, NULL) AS M3
                , IF(Q1.m = 4, Q1.j1, NULL) AS M4
                , IF(Q1.m = 5, Q1.j1, NULL) AS M5
                , IF(Q1.m = 6, Q1.j1, NULL) AS M6
                , IF(Q1.m = 7, Q1.j1, NULL) AS M7
                , IF(Q1.m = 8, Q1.j1, NULL) AS M8
                , IF(Q1.m = 9, Q1.j1, NULL) AS M9
                , IF(Q1.m = 10, Q1.j1, NULL) AS M10
                , IF(Q1.m = 11, Q1.j1, NULL) AS M11
                , IF(Q1.m = 12, Q1.j1, NULL) AS M12
            FROM (
                SELECT MONTH(fOrderDate) AS m, DAY(fOrderDate) AS d
                    , SUM(fPayable) AS j1
                FROM t_order
                WHERE (Year(fOrderDate) = {}
                    AND fCanceled = 0
                    AND fSubmited = 1
                    AND fConfirmed = 1)
                GROUP BY MONTH(fOrderDate), DAY(fOrderDate)
            ) Q1
            GROUP BY Q1.d WITH ROLLUP
        ) Q3
        """.format(2019))
    print("dd")