import re
sql = '''
        SELECT fOrderID, fOrderDate, fVendedorID, fRequiredDeliveryDate , fCustomerID, fContato, fCelular, fTelefone, fAmount, fTax , fPayable, fDesconto, fNote FROM t_order WHERE fOrderID = '';
        '''


def getMainTableNameInfo(sql):
    sql = re.sub(r'^\s', '', re.sub(r'\s+', ' ', re.sub(r'\n', '', sql)))
    sel_p = r"SELECT\s+.*from\s(\S+)\s(as\s\S+){0,1}where\s(\S+)\s*=.*"
    mt = re.match(sel_p, sql, flags=(re.I))
    if mt:
        return mt.groups()[0], mt.groups()[2]

