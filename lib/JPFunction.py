# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
import datetime

from PyQt5.QtCore import QDate
from functools import singledispatch
from decimal import Decimal


def PrintFunctionRunTime(func):
    """计算函数运行时间的装饰器"""

    def run(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("函数{0}的运行时间为： {1}".format(func.__name__, time.time() - start))
        return result

    return run


def Singleton(cls, *args, **kw):
    """单实例装饰器"""
    instance = {}

    def _singleton():
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]

    return _singleton


@Singleton
class JPBooleanString(object):
    __BoolString = (('Non', 0), ('SIM', 1))

    def getBooleanString(self):
        return self.__BoolString

    def setBooleanString(tup: tuple):
        """设置全局逻辑变量的默认值
        格式如 (('', 0), ('SIM', 1))"""
        self.__BoolString = [tup]


def JPReadDataToWidget(Widget, FieldType, FieldValue):
    if FieldValue is None: return
    if FieldType in (1, 3, 8):  # TinyInt,Int
        Widget.setText(str(FieldValue))
    elif FieldType in (7, 10):  # TS,DATE
        pass
        #item.setText(str(FieldValue))
    elif FieldType == 16:  # Bit
        Widget.setText(str(ord(FieldValue)))
    elif FieldType == 246:  # Decimal
        Widget.setText('{:,.2f}'.format(FieldValue))
    elif FieldType in (253, 254):  # VChar,Char
        Widget.setText(str(FieldValue))
    else:  # other
        Widget.setText(str(FieldValue))


def NV(value, mod):
    if isinstance(mod, str):
        return str(value) if value else ''
    if isinstance(mod, int):
        return int(value) if value else 0
    if isinstance(mod, (float, Decimal)):
        return float(value) if value else 0.0
    return value


def JPReadLineToTableWidgetItem(item, FieldType, FieldValue):
    if FieldValue is None: return
    left = (Qt.AlignLeft | Qt.AlignVCenter)
    center = (Qt.AlignCenter | Qt.AlignVCenter)
    right = (Qt.AlignRight | Qt.AlignVCenter)
    if FieldType in (1, 3, 8):  # TinyInt,Int
        item.setText(str(FieldValue))
        item.setTextAlignment(right)
    elif FieldType in (7, 10):  # TS,DATE
        item.setText(str(FieldValue))
        item.setTextAlignment(center)
    elif FieldType == 16:  # Bit
        item.setText(str(ord(FieldValue)))
        item.setTextAlignment(center)
    elif FieldType == 246:  # Decimal
        item.setText('{:,.2f}'.format(FieldValue))
        item.setTextAlignment(right)
    elif FieldType in (253, 254):  # VChar,Char
        item.setText(str(FieldValue))
        item.setTextAlignment(left)
    else:  # other
        item.setText(str(FieldValue))
        item.setTextAlignment(left)


def JPRound(number, power=0):
    """
    实现精确四舍五入，包含正、负小数多种场景
    :param number: 需要四舍五入的小数
    :param power: 四舍五入位数，支持0-∞
    :return: 返回四舍五入后的结果
    """
    if number is None:
        return
    digit = 10**power
    num2 = float(int(number * digit))
    # 处理正数，power不为0的情况
    if number >= 0 and power != 0:
        tag = number * digit - num2 + 1 / (digit * 10)
        if tag >= 0.5:
            return (num2 + 1) / digit
        else:
            return num2 / digit
    # 处理正数，power为0取整的情况
    elif number >= 0 and power == 0:
        tag = number * digit - int(number)
        if tag >= 0.5:
            return (num2 + 1) / digit
        else:
            return num2 / digit
    # 处理负数，power为0取整的情况
    elif power == 0 and number < 0:
        tag = number * digit - int(number)
        if tag <= -0.5:
            return (num2 - 1) / digit
        else:
            return num2 / digit
    # 处理负数，power不为0的情况
    else:
        tag = number * digit - num2 - 1 / (digit * 10)
        if tag <= -0.5:
            return (num2 - 1) / digit
        else:
            return num2 / digit

###################################################################
@singledispatch
def JPGetDisplayText(value, *args) -> str:
    '''返回参数的显示用字符形式
    指定value是一个外键值时，请指定第二个参数为一个列表
    该列表第一列是返回的字符串，第一列为value对应值
    '''
    if value:
        return value


@JPGetDisplayText.register(QDate)
def _(value, *args):
    return value.toString("yyyy-MM-dd")


@JPGetDisplayText.register(datetime.date)
def _(value, *args):
    return value.toString("yyyy-MM-dd")


@JPGetDisplayText.register(int)
def _(value, *args):
    return '{:,}'.format(value)


@JPGetDisplayText.register(float)
def _(value, *args):
    return '{:,.2f}'.format(value)


@JPGetDisplayText.register(Decimal)
def _(value, *args):
    v=float(str(value))
    return '{:,.2f}'.format(v)




@JPGetDisplayText.register(bytes)
def _(value, *args):
    return JPBooleanString().getBooleanString()[ord(x)]

######################################################################
@singledispatch
def JPDateConver(value, vCls=str):
    '''JPDateConver(value, vCls)\n
    日期转换:value类型可为str、datetime.date、datetime.datatime或QDate\n
    vCls指定输出格式，为一类名可以是datetime.date、QDate或str
    '''
    raise TypeError("JPDateConver函数参数类型错误！")


@JPDateConver.register(str)
def _(value, vCls=str):
    cur_date = QDate.fromString(value, "yyyy-MM-dd")
    if vCls is str:
        return value
    if vCls is QDate:
        return cur_date
    if vCls is datetime.date:
        return datetime.datetime.strptime(value, '%Y-%m-%d').date()
    raise TypeError("JPDateConver函数vCls参数类型错误！")


@JPDateConver.register(QDate)
def _(value, vCls=str):
    if vCls is str:
        return value.toString("yyyy-MM-dd")
    if vCls is QDate:
        return value
    if vCls is datetime.date:
        return datetime.datetime(value.year(), value.month(),
                                 value.day()).date()
    raise TypeError("JPDateConver函数vCls参数类型错误！")


@JPDateConver.register(datetime.date)
def _(value, vCls=str):
    cur_date = QDate(value.year, value.month, value.day)
    if vCls is str:
        return cur_date.toString("yyyy-MM-dd")
    if vCls is QDate:
        return cur_date
    if vCls is datetime.date:
        return value
    raise TypeError("JPDateConver函数vCls参数类型错误！")



# print(JPGetDisplayText(5456123465))
# print(JPGetDisplayText(float(875648266)))
# print(JPGetDisplayText(None))
# print(JPGetDisplayText('dfsgsdfg'))
# print(JPGetDisplayText(bytes('0')))
