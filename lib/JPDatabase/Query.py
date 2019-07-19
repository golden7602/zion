import re
from copy import deepcopy
from PyQt5.QtCore import QModelIndex
from JPDatabase.Database import JPDb
from JPDatabase.Field import JPFieldInfo
from PyQt5.QtWidgets import QMessageBox


class JPTabelRowData(object):
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
            self.OriginalValue = self.New
        else:
            raise ValueError("参数值错误")

    @property
    def State(self) -> int:
        return self._state

    @property
    def Data(self, column):
        return self.__data[column]

    @property
    def Datas(self):
        return self.__data

    def setData(self, column, value):
        self.OriginalValue = self.Update
        self.__data[column] = value


class JPQueryFieldInfo(object):
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
        self.Fields = flds
        self.RowsData = [JPTabelRowData(row) for row in data]
        self.FieldsDict = {fld.FieldName: fld for fld in flds}

    def getOnlyData(self, index: [list, tuple, QModelIndex]):
        r, c = JPQueryFieldInfo.getRC(index)
        return self.RowsData(r)[c]

    def getRowData(self, row_num) -> JPTabelRowData:
        pass

    def getFieldsInfo(self):
        return self.Fields

    def getRowFieldsInfoAndData(self, row_num):
        flds = deepcopy(self.Fields)
        data = self.RowsData[row_num]
        for i, fld in flds:
            fld.Value = data[i]
        return flds

    def getRowValueDict(self, row_num: int) -> dict:
        data = self.RowsData(row_num)
        r = {}
        for i, item in enumerate(data):
            r[self.Fields[i].FieldName] = item
        return r

    def getFieldsInfoDict(self) -> dict:
        return self.FieldsDict

    def getFieldInfoAndData(self, field_name: str,
                            index: [list, tuple, QModelIndex]) -> JPFieldInfo:
        r, c = self.getRC(index)
        fld = deepcopy(self.FieldsDict[field_name])
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

        sql = re.sub(r'^\s', '', re.sub(r'\s+', ' ', re.sub(r'\n', '', sql)))
        sel_p = r"SELECT\s+.*from\s(\S+)\s"
        mt = re.match(sel_p, sql, flags=(re.I))
        JPEditFormDataMode = mt.groups()[0] if mt else sql
        s_filter = db.getOnlyStrcFilter()
        if noData:
            # 找出不包含条件的SQL语句
            p_s = r"(SELECT\s+.*from\s(\S+)\s(as\s\S+)*)"
            mt1 = re.match(p_s, sql, flags=(re.I))
            sql = mt1.groups(
            )[0] + " " + s_filter if mt else 'Select * from {} {}'.format(
                JPEditFormDataMode, s_filter) if mt else sql
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
        pk_fld=self.getFieldsInfoDict()

    def setData(self, index: [list, tuple, QModelIndex], value=None):
        r, c = super().getRC(index)
        self.RowsData[r].setData(c, value)

    def addRow(self):
        '''增加一行数据，全为None'''
        self.RowsData.append(JPTabelRowData(len(self.Fields)))

    def getSqlstatements(self, Mainform):
        sql = []
        # 不能为空，不是主键，不是自增列的列号
        not_null_col = []
        for i in range(self.Fields):
            fld = self.Fields[i]
            if all([
                    fld.IsPrimarykey is False, fld.Auto_Increment is False,
                    fld.NotNull is True
            ]):
                not_null_col.append(i)
        # 检查空值 如有不全要求的字段，则返回行号
        for r in range(self.RowsData):
            for i in not_null_col:
                if (self.RowsData.State != JPTabelRowData.New) and (
                        self.RowsData[r].Datas[i] is None):
                    msg = "第{}行[{}]字段的值不能为空！".format(r + 1,
                                                     self.Fields[i].FieldName)
                    QMessageBox.warning(self, msg, QMessageBox.Yes,
                                        QMessageBox.Yes)
                    return r
        for row in self.RowsData:
            if row.State == JPTabelRowData.OriginalValue:
                continue
            if row.State == JPTabelRowData.New
                if 
            

    # def GetSQLS(self) -> dict:
    #     d = self.TabelFieldInfo.Data
    #     fs = self.TabelFieldInfo.Fields
    #     pk_col = [i for i, f in enumerate(fs) if f.IsPrimarykey]
    #     if len[pk_col] == 0:
    #         raise ValueError("数据表中未包含主键字段！")
    #     else:
    #         pk_col = pk_col[0]
    #     no_pk_fld = {
    #         i: f
    #         for i, f in enumerate(fs)
    #         if f.IsPrimarykey is False and f.Auto_Increment is False
    #     }

    #     # 检查空值
    #     not_null_cols = [k for k, f in no_pk_fld.items if f.NotNull is True]

    #     for r, line in enumerate(d):
    #         for i in not_null_cols:
    #             if line[i] is None:
    #                 raise ValueError("第{}行[{}]字段的值不能为空！".format(
    #                     r + 1, fs[i].FieldName))
    #     sqls = {}
    #     sqls["DELETE"] = []
    #     if self.del_data:
    #         s = str(tuple(self.del_data))
    #         sqls["DELETE"] = "delete from {} where {} in {}".format(s)
    #     sqls["INSERT"] = []
    #     sqls["UPDATE"] = []

    #     def getRow():
    #         for i, r in enumerate(d):
    #             bz = 1 if r[pk_col] is None else 0
    #             yield bz, i, r

    #     for bz, i, r in getRow():
    #         if bz == 1:
    #             pass