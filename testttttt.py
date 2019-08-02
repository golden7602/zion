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

f = '{aaa}= {bbbb}+{ccccc} * {dddddd}'
f = re.sub(r'\s', '', f)
mt = re.match("\{(\S+)\}=(.+)", re.sub(r'\s', '', f), flags=(re.I))
try:
    fLeft = mt.groups()[0]
    fRight = mt.groups()[1]
except Exception:
    raise ValueError("公式解析错误")
print(fLeft, fRight)
a='{aa}0000{ab}'.format(aa=1,ab=1,c=3)
print(a)
