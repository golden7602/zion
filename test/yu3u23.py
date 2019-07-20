# # import sys
# # from PyQt5.QtWidgets import *
# # from PyQt5.QtGui import *
# # from PyQt5.QtCore import *
# import decimal
# ################################################

# import re


# ################################################
# class mycla():
#     items_list = [[
#         "C", "C++", "Java", "Python", "JavaScript", "C#", "Swift", "go",
#         "Ruby", "Lua", "PHP"
#     ],
#                   [
#                       "C1", "C++1", "Java", "Python", "JavaScript", "C#",
#                       "Swift", "go", "Ruby", "Lua", "PHP"
#                   ]]

#     def __getitem__(self, index: int):
#         return self.items_list[index]


# if __name__ == "__main__":
#     s = """
#                     SELECT fOrderID as 订单号码OrderID,
#                         fOrderDate as 日期OrderDate,
#                         fCustomerName as 客户名Cliente,
#                         fCity as 城市City,
#                         fSubmited1 as 提交Submited,
#                         fSubmit_Name as 提交人Submitter,
#                         fAmount as 金额SubTotal,
#                         fRequiredDeliveryDate as 交货日期RDD,
#                         fDesconto as 折扣Desconto,
#                         fTax as 税金IVA,
#                         fPayable as `应付金额Valor a Pagar`,
#                         fContato as 联系人Contato,
#                         fCelular as 手机Celular,
#                         cast(fSubmited as SIGNED) AS fSubmited
#                 FROM v_order AS o000
#                 WHERE fCanceled=0
#                         AND left(fOrderID,2)='CP'
#                         AND (fSubmited={}
#                         OR fSubmited={})
#                         AND fOrderDate{}
#                 ORDER BY  forderID DESC"""

#     p = r"SELECT\s+.*from\s(\S+)\s"
#     s = re.sub(r'^\s', '', re.sub(r'\s+', ' ', re.sub(r'\n', '', s)))
#     print(s)
#     p = r"(SELECT\s+.*from\s(\S+)\s(as\s\S+)*)"
#     m = re.search(p, s, (re.I))
#     print(m.groups()[0])


from PyQt5.QtSql import QSqlDatabase

db=QSqlDatabase(QSqlDatabase.)