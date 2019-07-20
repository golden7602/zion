
class PrintingOrder(Order):
    def __init__(self):
        super().__init__()

    def _init_PrintingOrder_Individualization(self):
        RH.AddItem(1,
                   0,
                   155,
                   90,
                   20,
                   "类别Especie:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(3,
                   90,
                   155,
                   90,
                   20,
                   "fCategory",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignLeft)
        RH.AddItem(1,
                   180,
                   155,
                   130,
                   20,
                   "材料Materia:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(3,
                   310,
                   155,
                   90,
                   20,
                   "fBrandMateria",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignLeft)
        RH.AddItem(1,
                   400,
                   155,
                   90,
                   20,
                   "电话Tel:",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignCenter)
        RH.AddItem(3,
                   490,
                   155,
                   160,
                   20,
                   "fTelefone",
                   Font=self.font_YaHei_8,
                   AlignmentFlag=Qt.AlignLeft)

    def __myinit(self):
        logo = QPixmap("D:\\JinptConfig\\桌面2018\\newPYprj\\res\\Zions_100.png")
        self.FillColor = QColor(128, 128, 128)
        (Qt.AlignRight | Qt.AlignVCenter) = (Qt.AlignRight | Qt.AlignVCenter)
        font = QFont("微软雅黑", 15)
        self.font_YaHei_8 = QFont("微软雅黑", 8)
        font.setBold(True)
        RH = self.ReportHeader
        # sec.AddItem(1,5010,15,5295,435,'NOTA DE PAGAMENTO',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,5099,453,5130,450,'(ESTE DOCUMENTO é DO USO INTERNO)',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6285,0,1485,295,'订单号码No',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6285,590,1485,295,'城市City:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,0,590,1440,295,'税号NUIT:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,0,295,1440,295,'客户Cliente:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,0,0,1440,295,'订单日期Date:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,1440,295,4845,295,'fCustomerName',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,7771,0,2460,295,'fOrderID',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,1440,0,1395,295,'fOrderDate',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,7771,590,2460,295,'fCity',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,1440,590,4845,295,'fNUIT',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,10230,435,225,2259,'CONT.  / PRDUCAO
        # ',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,2835,0,2085,295,'交货日期Delivery date:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,4920,0,1365,295,'fRequiredDeliveryDate',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6285,295,1485,295,'销售Vendedor:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,7771,295,2460,295,'fVendedor',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,1440,885,7050,340,'fEndereco',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,4710,1565,1920,340,'fBrandMateria',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,4710,2245,1920,340,'fNumerBegin',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,7350,2245,2880,340,'fNumerEnd',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,7701,1565,780,340,'fQuant',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,1440,1225,1590,340,'fContato',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,4710,1225,1920,340,'fCelular',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,7701,1225,2528,340,'fTelefone',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6630,2245,720,340,'ATE',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,9516,1565,714,340,'fPrice',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,1440,1565,1590,340,'fEspecie',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,1440,1905,1590,340,'fAvista',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,1440,2245,1590,340,'fTamanho',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,4710,1905,1920,340,'fNrCopy',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,7701,1905,780,340,'fPagePerVolumn',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,0,1225,1440,340,'联系人Contato:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,0,1565,1440,340,'类别Especie:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,0,1905,1440,340,'每页序号Avista:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,0,2245,1440,340,'尺寸Tamanho:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,3030,1565,1680,340,'材料Materia:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,3030,1225,1680,340,'手机Celular:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,3030,2245,1680,340,'序号Numeracao:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,3030,1905,1680,340,'联数Nr.Copy:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6630,1565,1071,340,'数量Quant:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6630,1225,1071,340,'电话Tel:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,8481,1565,1035,340,'单价Price:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6630,1905,1071,340,'Page/Vol:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,0,885,1440,340,'地址Endereco:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,8490,885,1740,340,'Sucursal:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,8481,1905,1748,340,'Logo:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,8208,3744,570,145,'fNote',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,7488,3744,575,145,'Note:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,9072,3744,285,135,'Note:
        # Esta ordem sera entregue em 10 dias de trabalho, se esta for urgente,e necessario pagar mais 20%. Para que nao afecte os trrabalhos diarios da vossa empresa,por favor, encomendem a vossa ordem  o mais rapido possivel.',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6768,3744,576,145,'LianCi',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6624,2880,2295,295,'折扣Desconto:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,8920,2880,1310,295,'fDesconto',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6624,3470,2295,295,'应付金额Valor a Pagar:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6624,3175,2295,295,'税金IVA:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,6624,2585,2295,295,'金额合计SubTotal:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,8920,3470,1310,295,'fPayable',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,8920,3175,1310,295,'fTax',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,8920,2585,1310,295,'fAmount',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,0,2592,6630,1585,'fNote1',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,3750,315,6456,345,'TextPrintTime',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,0,0,1695,295,'制作人 Productor:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,3630,0,1590,295,'审核人 Aprovar:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,7200,0,1125,295,'会计Caixa:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)
        # sec.AddItem(1,0,345,1695,280,'销售Vendedor:',Font=self.font_YaHei_8,AlignmentFlag = Qt.AlignCenter)

    def BeginPrint(self, OrderID: str = "CP2019-0201000021"):
        SQL = "select o.*, d.fQuant,d.fProductName,d.fLength,d.fWidth,\
            d.fPrice,d.fAmount as fAmountDetail from  v_order as o right join t_order_detail \
                    as d on o.fOrderID=d.fOrderID  where d.fOrderID='{}'"

        # SQL = "select o.*, d.fQuant,d.fProductName,d.fLength,d.fWidth,\
        #     d.fPrice,d.fAmount as fAmountDetail from  v_order as o right join t_order_detail \
        #         as d on o.fOrderID=d.fOrderID  "
        data = pub.getDict(SQL.format(OrderID))
        data.sort(key=lambda x: (x['fCustomerName'], x['fCity'], x['fAmount']
                                 is None, x['fAmount']))
        self.DataSource = data
        self.__myinit()
        super().BeginPrint()

