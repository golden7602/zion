from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from PyQt5.QtCore import QDate, QMetaObject, QModelIndex, Qt, pyqtSlot
from PyQt5.QtGui import QColor, QFont, QPixmap, QIcon
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWidgets import QDialog, QMessageBox, QPushButton, QWidget

from lib.JPDatabase.Query import JPQueryFieldInfo
from lib.JPExcel.JPExportToExcel import JPExpExcelFromManyTabelFieldInfo
from lib.JPFunction import JPDateConver, JPGetDisplayText, findButtonAndSetIcon
from lib.JPMvc import JPWidgets
from lib.JPMvc.JPEditFormModel import JPEditFormDataMode, JPFormModelMain
from lib.JPMvc.JPModel import JPTableViewModelReadOnly
from lib.JPPrintReport import JPReport
from lib.ZionPublc import JPPub, JPUser
from Ui.Ui_FormReceivableEdit import Ui_Form as Edit_ui
from Ui.Ui_FormReceivables import Ui_Form


class Form_Receivables(QWidget):
    def __init__(self, mainform):
        super().__init__()
        self.MainForm = mainform
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #findButtonAndSetIcon(self)
        mainform.addForm(self)
        self.SQLCustomerArrearsList = """
            select c.fCustomerID as 客户编号ID,
                c.fCustomerName as `客户名Cliente`,
                c.fCity as 城市City,
            if(	YS.fYS=0,null,YS.fYS) as `应收合计TotalReceivables`,
                if(SK.fSK=0,null,SK.fSK) as `收款累计SumRec`,
                if(if(isnull(YS.fYS),0,YS.fYS)-if(isnull(SK.fSK),0,SK.fSK)=0,null,if(isnull(YS.fYS),0,YS.fYS)-if(isnull(SK.fSK),0,SK.fSK)) as `欠款Arrears`,
                r1.fReceiptDate as `最后收款日LastfReceiptDate`,
                cast(r1.fAmountCollected as DECIMAL) as `最后收款额LastAmountCollected`
            from t_customer as c left join 
                (select o.fCustomerID,
                    cast(sum(o.fPayable) as DECIMAL) as fYS 
                    from t_order as o 
                    where o.fCanceled=0 and o.fSubmited=1 and o.fConfirmed=1 group by o.fCustomerID) as YS
            on c.fCustomerID=YS.fCustomerID left join 
                (select r.fCustomerID,
                    cast(sum(r.fAmountCollected) as DECIMAL) as fSK,
                    max(r.fID) as LastRecID 
                    from t_receivables as r 
                    group by r.fCustomerID ) as SK
                on c.fCustomerID=SK.fCustomerID
                left join t_receivables as r1 
                on r1.fID=SK.LastRecID
            where c.fCustomerID={CustomerID}
        """
        self.SQLCustomerRecorder = """
                select 
                Q.fDate as 日期OrderDate, 
                Q.fOrderID as 订单号码OrderID, 
                Q.fPayable as 应收金额Payable, 
                Q.fAmountCollected as 收款fAmountCollected 
                from 
                (
                    select 
                    o.fOrderDate as fDate, 
                    o.fOrderID, 
                    cast(o.fPayable as DECIMAL) as fPayable, 
                    null as fAmountCollected, 
                    o.ts 
                    from 
                    t_order as o 
                    where 
                    o.fCustomerID ={CustomerID} 
                    and o.fCanceled = 0 
                    and o.fSubmited = 1 
                    and o.fConfirmed = 1 
                    union all 
                    select 
                    r.fReceiptDate as fDate, 
                    Null as fOrderID, 
                    Null as fPayable, 
                    cast(r.fAmountCollected as DECIMAL) as fAmountCollected, 
                    r.ts 
                    from 
                    t_receivables as r 
                    where 
                    r.fCustomerID ={CustomerID} 
                    union all 
                    select 
                    null as fDate, 
                    'Sum' as fOrderID, 
                    cast(
                        sum(Q1.fPayable) as DECIMAL
                    ) as fPayable, 
                    cast(
                        sum(Q1.fAmountCollected) as DECIMAL
                    ) as fAmountCollected, 
                    null as ts 
                    from 
                    (
                        select 
                        o.fOrderDate as fDate, 
                        o.fOrderID, 
                        cast(o.fPayable as DECIMAL) as fPayable, 
                        null as fAmountCollected, 
                        o.ts 
                        from 
                        t_order as o 
                        where 
                        o.fCustomerID ={CustomerID} 
                        and o.fCanceled = 0 
                        and o.fSubmited = 1 
                        and o.fConfirmed = 1 
                        union all 
                        select 
                        r.fReceiptDate as fDate, 
                        Null as fOrderID, 
                        Null as fPayable, 
                        cast(r.fAmountCollected as DECIMAL), 
                        r.ts 
                        from 
                        t_receivables as r 
                        where 
                        r.fCustomerID ={CustomerID}
                    ) as Q1
                ) as Q 
                order by 
                Q.TS DESC
        """
        self.SQLCurrentDayRec = """
            SELECT fID as 流水号ID,
                    fCustomerID as 客户编号CustomerID,
                    fCustomerName as 客户名Cliente,
                    fReceiptDate as 收款日期ReceiptDate,
                    fAmountCollected as 收款额AmountCollected,
                    fPayee as 收款人fPayee,
                    fPaymentMethod AS 收款方式ModoPago,
                    fOrderID as 订单号OrderID,
                    fNote as 备注Note
                    
            FROM v_receivables as r           
            WHERE 
                r.fReceiptDate = STR_TO_DATE('{dateString}', '%Y-%m-%d') 
            order by fID DESC
        """
        self.SQLSumPaymentMethod = """
            SELECT e.fTitle AS `收款方式PaymentMethod` ,
                    sum(fAmountCollected) AS `收款合计Collection of receipts`,
                    count(fID) AS `收款笔数Number of Payments Received`
            FROM t_receivables AS r
            LEFT JOIN t_enumeration AS e
                ON r.fPaymentMethodID=e.fItemID
            WHERE 
                r.fReceiptDate = STR_TO_DATE('{dateString}', '%Y-%m-%d') 
            GROUP BY  r.fPaymentMethodID

            """
        self.ui.SelectDate.dateChanged.connect(self.dateChanged)
        # 引发一次日期修改事件，刷新 左上、右上
        self.ui.SelectDate.setDate(QDate.currentDate())
        # 引发一次事件，刷新左下、右下
        self.currentCustomerChanged()

    def __formChange(self, *args):
        print(args)

    @pyqtSlot()
    def on_CmdEdit_clicked(self):
        frm = RecibidoEdit()
        frm.ListForm = self
        frm.ui.fAmountCollected.setDoubleValidator(-100000000.0, 100000000.0,
                                                   2)
        frm._currentDate = self.ui.SelectDate.date()
        frm.exec_()

    @pyqtSlot()
    def on_CmdRecibido_clicked(self):
        frm = RecibidoEdit()
        frm.ListForm = self
        frm.ui.fAmountCollected.setDoubleValidator(0.01, 100000000.0, 2)
        frm._currentDate = self.ui.SelectDate.date()
        #frm.ui.fNote.refreshValueNotRaiseEvent('DIBOTO', True)
        frm.exec_()

    @pyqtSlot()
    def on_CmdExportToExcel_clicked(self):
        exp = JPExpExcelFromManyTabelFieldInfo(
            self.tabinfoCurrentDayRec,
            self.tabinfoFangShiTongJi,
            self.tableinfoCustomerRecorder,
            self.tableinfoCustomerArrearsList,
            MainForm=self.MainForm)
        exp.run()

    @pyqtSlot()
    def on_CmdDailyRreport_clicked(self):
        if len(self.tabinfoCurrentDayRec) == 0:
            return
        try:
            p = FormReport_Rec_print(
                JPDateConver(self.ui.SelectDate.date(), str),
                self.tabinfoCurrentDayRec, self.tabinfoFangShiTongJi,
                JPDateConver(self.ui.SelectDate.date(), str))
            p.BeginPrint()
        except Exception as e:
            pass

    def dateChanged(self, s_data):
        str_date = JPDateConver(self.ui.SelectDate.date(), str)

        # 设置当前日收款记录（左上）
        sql = self.SQLCurrentDayRec.format(dateString=str_date)
        self.tabinfoCurrentDayRec = JPQueryFieldInfo(sql)
        self.modCurrentDayRec = JPTableViewModelReadOnly(
            self.ui.tabCurrentDayRec, self.tabinfoCurrentDayRec)
        self.ui.tabCurrentDayRec.setModel(self.modCurrentDayRec)
        self.ui.tabCurrentDayRec.resizeColumnsToContents()
        self.ui.tabCurrentDayRec.selectionModel(
        ).currentRowChanged[QModelIndex, QModelIndex].connect(
            self.currentCustomerChanged)

        # 设置当前日收款方式统计（右上）
        self.tabinfoFangShiTongJi = JPQueryFieldInfo(
            self.SQLSumPaymentMethod.format(dateString=str_date))
        self.modFangShiTongJi = JPTableViewModelReadOnly(
            self.ui.SumPaymentMethod, self.tabinfoFangShiTongJi)
        self.ui.SumPaymentMethod.setModel(self.modFangShiTongJi)
        self.ui.SumPaymentMethod.resizeColumnsToContents()

        #self.currentCustomerChanged()

    def currentCustomerChanged(self):
        id = -1
        index = self.ui.tabCurrentDayRec.selectionModel().currentIndex()
        if index.isValid():
            id = self.modCurrentDayRec.TabelFieldInfo.getOnlyData(
                [index.row(), 1])
        # 刷新左下
        self.tableinfoCustomerRecorder = JPQueryFieldInfo(
            self.SQLCustomerRecorder.format(CustomerID=id))
        self.modCustomerRecorder = JPTableViewModelReadOnly(
            self.ui.tabCustomerRecorder, self.tableinfoCustomerRecorder)
        self.ui.tabCustomerRecorder.setModel(self.modCustomerRecorder)
        self.ui.tabCustomerRecorder.resizeColumnsToContents()

        # 刷新右下
        self.tableinfoCustomerArrearsList = JPQueryFieldInfo(
            self.SQLCustomerArrearsList.format(CustomerID=id))
        self.modCustomerArrearsList = JPTableViewModelReadOnly(
            self.ui.tabCustomerArrearsList, self.tableinfoCustomerArrearsList)
        self.ui.tabCustomerArrearsList.setModel(self.modCustomerArrearsList)
        self.ui.tabCustomerArrearsList.resizeColumnsToContents()

        # self.ui.tabCurrentDayRec.setModel(self.modCurrentDayRec)
        # self.ui.tabCurrentDayRec.resizeColumnsToContents()


class RecibidoEdit(JPFormModelMain):
    def __init__(self):
        m_sql = '''SELECT fID, 
                        fCustomerID AS 客户名Cliente, 
                        fPaymentMethodID AS 收款方式ModoPago, 
                        fReceiptDate as 收款日期ReceiptDate,
                        fAmountCollected AS 金额Amount,
                        fPayeeID, fNote,
                        fOrderID as 单据号码OrderID
                        FROM t_receivables
                        WHERE fID = '{}'
                '''
        super().__init__(Edit_ui(),
                         sql_main=m_sql,
                         PKValue=None,
                         edit_mode=JPEditFormDataMode.New,
                         flags=Qt.WindowFlags())
        JPPub().MainForm.addLogoToLabel(self.ui.label_logo)
        JPPub().MainForm.addOneButtonIcon(self.ui.butSave, 'save.png')
        JPPub().MainForm.addOneButtonIcon(self.ui.butCancel, 'cancel.png')
        self.ui.butCancel.clicked.connect(self.close)
        self.ui.fID.hide()
        self.readData()
        self.ui.fPayeeID.refreshValueNotRaiseEvent(JPUser().currentUserID(), )
        self.__setEnabled()
        self.ui.fCustomerID.currentIndexChanged.connect(self.__setEnabled)
        self.ui.fCustomerID.setEditable(True)
        self.ui.fOrderID.setEditable(False)
        self.ui.fOrderID.setEnabled(False)
        self.ui.fArrears.setEnabled(True)
        self.ui.fCustomerID.setFocus()

    @property
    def _currentDate(self):
        return self.ui.fReceiptDate.date()

    @_currentDate.setter
    def _currentDate(self, d):
        self.ui.fReceiptDate.refreshValueNotRaiseEvent(d)

    def __setEnabled(self):
        self.ui.fCustomerID.setEnabled(True)
        self.ui.fCity.setEnabled(False)
        self.ui.fNUIT.setEnabled(False)
        self.ui.fEndereco.setEnabled(False)
        self.ui.fEndereco.setEnabled(False)
        self.ui.fCelular.setEnabled(False)
        self.ui.fTelefone.setEnabled(False)
        self.ui.fAmountPayable.setEnabled(False)
        self.ui.fAmountPaid.setEnabled(False)
        #self.ui.fArrears.setEnabled(False)
        self.ui.fPayeeID.setEnabled(False)

    def onGetFieldsRowSources(self):
        pub = JPPub()
        u_lst = [[item[1], item[0]] for item in JPUser().getAllUserList()]
        return [('fCustomerID', pub.getCustomerList(), 1),
                ('fPaymentMethodID', pub.getEnumList(3), 1),
                ('fPayeeID', u_lst, 1), ('fOrderID', [['DIBOTO']], 0)]

    def onGetPrintReport(self):
        return  #PrintOrder_report_Mob()

    def onDateChangeEvent(self, obj, value):
        nm = obj.objectName()
        if nm == 'fCustomerID':
            self.__customerIDChanged()

    def __customerIDChanged(self):
        # 刷新客户有关信息
        sql = '''
            SELECT fNUIT, fCity, fEndereco, fCelular, fContato
                , fTelefone, Q0.fAmountPayable  , Q1.fAmountPaid,
                Q0.fAmountPayable-Q1.fAmountPaid as fArrears,-1 as fPaymentMethodID
            FROM t_customer c
                LEFT JOIN (
                    SELECT fCustomerID, SUM(fPayable) AS fAmountPayable
                    FROM t_order
                    WHERE fCustomerID = {CustomerID}
                        AND fConfirmed = 1
                ) Q0
                ON c.fCustomerID = Q0.fCustomerID
                LEFT JOIN (
                    SELECT fCustomerID, SUM(fAmountCollected) AS fAmountPaid
                    FROM t_receivables
                    WHERE fCustomerID = {CustomerID}
                ) Q1
                ON c.fCustomerID = Q1.fCustomerID
            WHERE c.fCustomerID = {CustomerID}
        '''
        sql = sql.format(CustomerID=self.ui.fCustomerID.Value())
        tab = JPQueryFieldInfo(sql)
        obj_name = [
            'fNUIT', 'fCity', 'fEndereco', 'fCelular', 'fContato', 'fTelefone',
            'fAmountPayable', 'fAmountPaid', 'fArrears'
        ]
        tup = (JPWidgets.QLineEdit, JPWidgets.QDateEdit, JPWidgets.QComboBox,
               JPWidgets.QTextEdit, JPWidgets.QCheckBox)
        fld_dict = tab.getRowFieldsInfoDict(0)
        for i, nm in enumerate(obj_name):
            obj = self.findChild(tup, nm)
            if obj:
                obj.setRowsData(tab.DataRows[0])
                obj.setMainModel(self)
                obj.setFieldInfo(fld_dict[nm])
                obj.refreshValueNotRaiseEvent(tab.getOnlyData([0, i]), True)

        # 刷新该客户名下当日单据号码
        sql_orderID = """
        select 'DIBOTO' as fOrderID
        union all 
        select fOrderID from t_order 
        where fCustomerID={CustomerID} 
            and fOrderDate=STR_TO_DATE('{dateString}', '%Y-%m-%d')
            and fConfirmed=1
            and fSubmited=1
            and fCanceled=0
        """
        sql_orderID = sql_orderID.format(
            CustomerID=self.ui.fCustomerID.Value(),
            dateString=JPDateConver(self._currentDate, str))
        tab = JPQueryFieldInfo(sql_orderID)
        fld = self.ui.fOrderID.FieldInfo
        fld.RowSource = [[r.Datas[0]] for r in tab.DataRows]
        fld.BindingColumn = 0
        fld.Value = None
        fld.NotNull = True
        self.ui.fOrderID.setFieldInfo(fld, False)
        self.ui.fOrderID.setEnabled(True)

    def onAfterSaveData(self, data):
        self.ui.butSave.setEnabled(False)
        self.ListForm.dateChanged(data)


class FormReport_Rec_print(JPReport):
    def __init__(self,
                 curdate,
                 cur_tab,
                 tongji_tab,
                 dateString,
                 PaperSize=QPrinter.A4,
                 Orientation=QPrinter.Orientation(0)):
        super().__init__(PaperSize, Orientation)
        self.configData = JPPub().getConfigData()
        self.font_YaHei = QFont("Microsoft YaHei")
        self.font_YaHei_8 = QFont(self.font_YaHei)
        self.font_YaHei_8.setPointSize(8)
        self.font_YaHei_10 = QFont(self.font_YaHei)
        self.font_YaHei_10.setPointSize(20)
        self.font_YaHei_10.setBold(True)
        rpt = self

        rpt.logo = QPixmap(getcwd() + "\\res\\tmLogo100.png")
        rpt.ReportHeader.AddItem(2, 0, 0, 274, 50, rpt.logo)
        rpt.ReportHeader.AddItem(1,
                                 274,
                                 0,
                                 446,
                                 60,
                                 'de vendas diárias 收款日报表',
                                 Bolder=False,
                                 AlignmentFlag=(Qt.AlignCenter),
                                 Font=self.font_YaHei_10)

        rpt.ReportHeader.AddItem(1,
                                 0,
                                 50,
                                 720,
                                 20,
                                 'Date:{}'.format(curdate),
                                 Bolder=False,
                                 AlignmentFlag=(Qt.AlignRight),
                                 Font=self.font_YaHei_8)

        title = [
            '序号\nID', '客户名\nCliente', '收款额\nAmount', '收款人\nfPayee',
            '收款方式\nModoPago', '单据号\nOrderID', '备注\nNote'
        ]

        fns = [
            'fID', 'fCustomerName', 'fAmountCollected', 'fPayee',
            'fPaymentMethod', 'fOrderID', 'fNote'
        ]
        cols = 7
        al_c = Qt.AlignCenter
        al_r = (Qt.AlignVCenter | Qt.AlignRight)
        al_l = (Qt.AlignVCenter | Qt.AlignLeft)
        rpt.SetMargins(30, 30, 30, 30)
        rpt.ReportHeader.AddPrintLables(0,
                                        72,
                                        40,
                                        Texts=title,
                                        Widths=[40, 210, 80, 80, 100, 120, 90],
                                        Aligns=[al_c] * cols)
        rpt.Detail.addPrintRowCountItem(0,
                                        0,
                                        40,
                                        20,
                                        AlignmentFlag=al_c,
                                        Font=self.font_YaHei_8)
        rpt.Detail.AddItem(
            3,
            40,
            0,
            210,
            20,
            fns[1],
            FormatString=' {}',
            AlignmentFlag=al_l,
            # 超出长度省略
            AutoShrinkFont=self.configData['AutoShrinkFonts'],
            AutoEllipsis=self.configData['AutoEllipsis'],
            Font=self.font_YaHei_8)
        rpt.Detail.AddItem(3,
                           250,
                           0,
                           80,
                           20,
                           fns[2],
                           AlignmentFlag=al_r,
                           FormatString='{:,.2f} ',
                           Font=self.font_YaHei_8)
        rpt.Detail.AddItem(3,
                           330,
                           0,
                           80,
                           20,
                           fns[3],
                           AlignmentFlag=al_c,
                           Font=self.font_YaHei_8)
        rpt.Detail.AddItem(3,
                           410,
                           0,
                           100,
                           20,
                           fns[4],
                           AlignmentFlag=al_c,
                           Font=self.font_YaHei_8)
        rpt.Detail.AddItem(3,
                           510,
                           0,
                           120,
                           20,
                           fns[5],
                           AlignmentFlag=al_l,
                           FormatString=' {}',
                           Font=self.font_YaHei_8)
        rpt.Detail.AddItem(3,
                           630,
                           0,
                           90,
                           20,
                           fns[6],
                           AlignmentFlag=al_l,
                           FormatString=' {}',
                           Font=self.font_YaHei_8)

        sum_j = 0
        for i in range(len(cur_tab)):
            sum_j += cur_tab.getOnlyData([i, 4])

        rpt.ReportFooter.AddPrintLables(
            0,
            0,
            20,
            Texts=["合计Sum", JPGetDisplayText(sum_j), " "],
            Widths=[250, 80, 390],
            Aligns=[al_c, al_r, al_c],
            FillColor=QColor(194, 194, 194),
            Font=self.font_YaHei_8)

        sql_payable = f"""
            SELECT SUM(fPayable) AS sumPayable, 
                COUNT(fOrderID) AS countOrderID
            FROM t_order
            WHERE (fOrderDate = STR_TO_DATE('{dateString}', '%Y-%m-%d')
                AND fCanceled = 0
                AND fConfirmed = 1)
        """
        sql_SKFS = f"""
        select if(isnull(Q.fPaymentMethod),'Sum合计',Q.fPaymentMethod) as skfs,
            Q.今日收款,Q.今日收款笔数,Q.DIBOTO,Q.DIBOTO笔数,Q.小计Subtotal,Q.笔数小计Subcount
            from (
            SELECT fPaymentMethod
                , SUM(if(fOrderID = 'DIBOTO', NULL, fAmountCollected)) AS 今日收款
                , COUNT(if(fOrderID = 'DIBOTO', NULL, fAmountCollected)) AS 今日收款笔数
                , SUM(if(fOrderID = 'DIBOTO', fAmountCollected, NULL)) AS DIBOTO
                , COUNT(if(fOrderID = 'DIBOTO', fAmountCollected, NULL)) AS DIBOTO笔数
                , SUM(fAmountCollected) AS 小计Subtotal, COUNT(fAmountCollected) AS 笔数小计Subcount
            FROM v_receivables
            WHERE fReceiptDate=STR_TO_DATE('{dateString}', '%Y-%m-%d')
            GROUP BY fPaymentMethod WITH ROLLUP) as Q        
        """
        title_height = 20
        rpt.ReportFooter.AddItem(1,
                                 0,
                                 title_height,
                                 720,
                                 30,
                                 "本日结算方式统计Today's settlement statistics",
                                 Bolder=False,
                                 AlignmentFlag=al_c)
        title_height += 30
        title = ['方式PM', "收当日订单Today's Order Rec", '收欠款DIBOTO', '小计SubTotle']
        rpt.ReportFooter.AddPrintLables(0,
                                        title_height,
                                        25,
                                        title,
                                        Widths=[120, 200, 200, 200],
                                        Aligns=[al_c] * 4,
                                        Font=self.font_YaHei_8)
        tongji_tab = JPQueryFieldInfo(sql_SKFS)
        title_height += 25
        for r in range(len(tongji_tab)):
            FillColor = QColor(255, 255,
                               255) if r < (len(tongji_tab) - 1) else QColor(
                                   194, 194, 194)
            rpt.ReportFooter.AddItem(1,
                                     0,
                                     title_height + r * 20,
                                     120,
                                     20,
                                     tongji_tab.getDispText([r, 0]),
                                     FormatString=' {}',
                                     AlignmentFlag=al_l,
                                     Font=self.font_YaHei_8,
                                     FillColor=FillColor)
            rpt.ReportFooter.AddItem(1,
                                     120,
                                     title_height + r * 20,
                                     150,
                                     20,
                                     tongji_tab.getDispText([r, 1]),
                                     FormatString='{} ',
                                     AlignmentFlag=al_r,
                                     Font=self.font_YaHei_8,
                                     FillColor=FillColor)
            rpt.ReportFooter.AddItem(1,
                                     270,
                                     title_height + r * 20,
                                     50,
                                     20,
                                     tongji_tab.getDispText([r, 2]),
                                     FormatString='{} ',
                                     AlignmentFlag=al_r,
                                     Font=self.font_YaHei_8,
                                     FillColor=FillColor)
            rpt.ReportFooter.AddItem(1,
                                     320,
                                     title_height + r * 20,
                                     150,
                                     20,
                                     tongji_tab.getDispText([r, 3]),
                                     FormatString='{} ',
                                     AlignmentFlag=al_r,
                                     Font=self.font_YaHei_8,
                                     FillColor=FillColor)
            rpt.ReportFooter.AddItem(1,
                                     470,
                                     title_height + r * 20,
                                     50,
                                     20,
                                     tongji_tab.getDispText([r, 4]),
                                     FormatString='{} ',
                                     AlignmentFlag=al_r,
                                     Font=self.font_YaHei_8,
                                     FillColor=FillColor)
            rpt.ReportFooter.AddItem(1,
                                     520,
                                     title_height + r * 20,
                                     150,
                                     20,
                                     tongji_tab.getDispText([r, 5]),
                                     FormatString='{} ',
                                     AlignmentFlag=al_r,
                                     Font=self.font_YaHei_8,
                                     FillColor=FillColor)
            rpt.ReportFooter.AddItem(1,
                                     670,
                                     title_height + r * 20,
                                     50,
                                     20,
                                     tongji_tab.getDispText([r, 6]),
                                     FormatString='{} ',
                                     AlignmentFlag=al_r,
                                     Font=self.font_YaHei_8,
                                     FillColor=FillColor)

        # 总结部分
        title_height += (len(tongji_tab) - 1) * 20
        title_height += 40
        title = [
            "当日订单应付Today's Order Payable",
            "收当日订单Today's Order Rec",
            '欠款Arrears',
        ]
        rpt.ReportFooter.AddPrintLables(120,
                                        title_height,
                                        25,
                                        title,
                                        Widths=[200, 200, 200],
                                        Aligns=[al_c] * 3,
                                        Font=self.font_YaHei_8)
        rpt.ReportFooter.AddItem(1,
                                 0,
                                 title_height,
                                 120,
                                 45,
                                 '总结\nsummary',
                                 FormatString='{} ',
                                 AlignmentFlag=al_c,
                                 Font=self.font_YaHei_8,
                                 FillColor=FillColor)

        title_height += 25
        payable_tab = JPQueryFieldInfo(sql_payable)
        v1 = payable_tab.getOnlyData([0, 0])
        v2 = tongji_tab.getOnlyData([len(tongji_tab) - 1, 5])
        v3 = '{:,.2f}'.format((v1 if v1 else 0) - (v2 if v2 else 0))
        t2 = tongji_tab.getDispText([len(tongji_tab) -
                                     1, 5]) + " " if v2 else "0 "
        txt = [
            payable_tab.getDispText([0, 0]) + " ",
            JPGetDisplayText(len(payable_tab), str) + " ",
            t2,
            # tongji_tab.getDispText([len(tongji_tab) - 1, 5]) + " ",
            JPGetDisplayText(len(tongji_tab), str) + " ",
            v3 + " "
        ]
        rpt.ReportFooter.AddPrintLables(120,
                                        title_height,
                                        20,
                                        txt,
                                        Widths=[150, 50, 150, 50, 200],
                                        Aligns=[al_r] * 5,
                                        Font=self.font_YaHei_8,
                                        FillColor=QColor(194, 194, 194))
        # 页脚
        self.PageFooter.AddItem(4,
                                10,
                                0,
                                100,
                                20,
                                '',
                                FormatString='Page: {Page}/{Pages}',
                                Bolder=False,
                                AlignmentFlag=Qt.AlignLeft,
                                Font=self.font_YaHei_8)
        self.PageFooter.AddItem(5,
                                0,
                                0,
                                720,
                                20,
                                '',
                                FormatString="PrintTime: %Y-%m-%d %H:%M:%S",
                                Bolder=False,
                                AlignmentFlag=Qt.AlignRight,
                                Font=self.font_YaHei_8)
        self.DataSource = [
            cur_tab.getRowValueDict(i) for i in range(len(cur_tab))
        ]

    def onFormat(self, SectionType, CurrentPage, RowDate=None):
        return False
