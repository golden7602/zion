# import abc
# import time
# from datetime import date, datetime, time

# from pymysql import connect, cursors
# from pymysql.constants import FIELD_TYPE


# class pub(object):
#     __DB = None  # 类属性

#     @classmethod
#     def GetDatabase(cls):
#         db = cls.__DB
#         if db is None:
#             #con = pymysql.converters.conversions.copy()
#             db = connect(host="127.0.0.1",
#                                  user="root",
#                                  password="1234",
#                                  database="myorder_python",
#                                  port=3306)
#             cls.__DB = db
#             return db
#         else:
#             return db

#     @classmethod
#     def getDict(cls, sql) -> dict:
#         cursor = cls.GetDatabase().cursor(cursors.DictCursor)
#         cursor.execute(sql)

#         return cursor.fetchall()

#     @classmethod
#     def GetFieldsTypeDict(cls, tableName) -> dict:
#         ft = {}
#         cur = pub.GetDatabase().cursor()
#         cur.execute("select * from {} limit 0".format(tableName))
#         flds = cur._result.fields
#         for i in range(0, len(flds)):
#             ft[flds[i].name] = flds[i].type_code
#         return ft





