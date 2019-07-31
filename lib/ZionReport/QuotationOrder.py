from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from lib.JPDatabase import Database
from lib.ZionWidgets.Order import EditForm_Order,Order_report



class QuotationOrder(EditForm_Order):
    def __init__(self):
        super().__init__()

    def PrintCurrentReport(self, OrderID: str = "CP2019-0201000021"):
        SQL = "select o.*, d.fQuant,d.fProductName,d.fLength,d.fWidth,\
            d.fPrice,d.fAmount as fAmountDetail from  v_order as o right join t_order_detail \
                    as d on o.fOrderID=d.fOrderID  where d.fOrderID='{}'"

        data = pub.getDict(SQL.format(OrderID))
        data.sort(key=lambda x: (x['fCustomerName'], x['fCity'], x['fAmount']
                                 is None, x['fAmount']))
        self.DataSource = data
        self._init_ReportHeader("COTACAO", "")
        self._init_ReportHeader_Individualization()
        self._init_DetailAndPageHeader()
        self._init_ReportFooter()
        super().BeginPrint()

class QuotationOrder_report(Order_report)
