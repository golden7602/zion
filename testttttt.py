import re
# sql = '''
#         SELECT fOrderID, fOrderDate, fVendedorID, fRequiredDeliveryDate , fCustomerID, fContato, fCelular, fTelefone, fAmount, fTax , fPayable, fDesconto, fNote FROM t_order WHERE fOrderID = '';
#         '''

# def getMainTableNameInfo(sql):
#     sql = re.sub(r'^\s', '', re.sub(r'\s+', ' ', re.sub(r'\n', '', sql)))
#     sel_p = r"SELECT\s+.*from\s(\S+)\s(as\s\S+){0,1}where\s(\S+)\s*=.*"
#     mt = re.match(sel_p, sql, flags=(re.I))
#     if mt:
#         return mt.groups()[0],C[2]

# f = '{aaa}= {bbbb}+{ccccc} * {dddddd}'
# f = re.sub(r'\s', '', f)
# mt = re.match("\{(\S+)\}=(.+)", re.sub(r'\s', '', f), flags=(re.I))
# try:
#     fLeft = mt.groups()[0]
#     fRight = mt.groups()[1]
# except Exception:
#     raise ValueError("公式解析错误")
# print(fLeft, fRight)
# a='{aa}0000{ab}'.format(aa=1,ab=1,c=3)
# print(a)




sql = "SELECT fItemID, fTypeID, fTitle AS 'text条目文本', fSpare1 AS 'Value1值1', fSpare2 AS 'Value2值2', fNote AS 'Note说明' FROM t_enumeration as uu WHERE fTypeID = -1 "
sql = re.sub(r'^\s', '', re.sub(r'\s+', ' ', re.sub(r'\n', '', sql)))
sel_p = r"^SELECT\s+.*from\s(\S+)[$|\s].*"
sel_p = r"^(SELECT\s+.*from\s(\S+)[$|\s](as\s\S+)*)"
mt = re.match(sel_p, sql, flags=(re.I | re.M))
print(mt.groups()[0])


str0="-12345.123"


rr = re.match(r"^-?[1-9]\d*\.\d{1,2}$", str0, flags=(re.I))
print(rr)
