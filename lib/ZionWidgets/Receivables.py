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

        frm.exec_()

    @pyqtSlot()
    def on_CmdRecibido_clicked(self):
        frm = RecibidoEdit()
        frm.ListForm = self
        frm.ui.fAmountCollected.setDoubleValidator(0.01, 100000000.0, 2)
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
        p = FormReport_Rec_print(JPDateConver(self.ui.SelectDate.date(),
                                              str), self.tabinfoCurrentDayRec,
                                 self.tabinfoFangShiTongJi)
        p.BeginPrint()

    def dateChanged(self, s_data):
        str_date = JPDateConver(self.ui.SelectDate.date(), str)

        # 设置当前日收款记录（左上）
        self.tabinfoCurrentDayRec = JPQueryFieldInfo(
            self.SQLCurrentDayRec.format(dateString=str_date))
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
                        fReceiptDate, 
                        fAmountCollected AS 金额Amount,
                        fPayeeID, fNote
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
        self.ui.fPayeeID.refreshValueNotRaiseEvent(JPUser().currentUserID())
        self.__setEnabled()
        self.ui.fCustomerID.currentIndexChanged.connect(self.__setEnabled)
        self.ui.fCustomerID.setEditable(True)
        self.ui.fArrears.setEnabled(True)

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
                ('fPayeeID', u_lst, 1)]

    def onGetPrintReport(self):
        return  #PrintOrder_report_Mob()

    def onDateChangeEvent(self, obj, value):
        nm = obj.objectName()
        if nm == 'fCustomerID':
            self.__customerIDChanged()

    def __customerIDChanged(self):
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

    def onAfterSaveData(self, data):
        self.ui.butSave.setEnabled(False)
        self.ListForm.dateChanged(data)


class FormReport_Rec_print(JPReport):
    def __init__(self,
                 curdate,
                 cur_tab,
                 tongji_tab,
                 PaperSize=QPrinter.A4,
                 Orientation=QPrinter.Orientation(0)):
        super().__init__(PaperSize, Orientation)

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
            '流水号\nID', '客户名\nCliente', '收款额\nAmount', '收款人\nfPayee',
            '收款方式\nModoPago', '备注\nNote'
        ]

        fns = [
            'fID', 'fCustomerName', 'fAmountCollected', 'fPayee',
            'fPaymentMethod', 'fNote'
        ]
        cols = 6
        al_c = Qt.AlignCenter
        al_r = (Qt.AlignVCenter | Qt.AlignRight)
        al_l = (Qt.AlignVCenter | Qt.AlignLeft)
        rpt.SetMargins(30, 30, 30, 30)
        rpt.ReportHeader.AddPrintLables(0,
                                        72,
                                        40,
                                        Texts=title,
                                        Widths=[60, 260, 100, 100, 100, 100],
                                        Aligns=[al_c] * cols)

        rpt.Detail.AddItem(3,
                           0,
                           0,
                           60,
                           25,
                           fns[0],
                           AlignmentFlag=al_c,
                           Font=self.font_YaHei_8)
        rpt.Detail.AddItem(3,
                           60,
                           0,
                           260,
                           25,
                           fns[1],
                           FormatString=' {}',
                           AlignmentFlag=al_l,
                           Font=self.font_YaHei_8)
        rpt.Detail.AddItem(3,
                           320,
                           0,
                           100,
                           25,
                           fns[2],
                           AlignmentFlag=al_r,
                           FormatString='{:,.2f} ',
                           Font=self.font_YaHei_8)
        rpt.Detail.AddItem(3,
                           420,
                           0,
                           100,
                           25,
                           fns[3],
                           AlignmentFlag=al_c,
                           Font=self.font_YaHei_8)
        rpt.Detail.AddItem(3,
                           520,
                           0,
                           100,
                           25,
                           fns[4],
                           AlignmentFlag=al_c,
                           Font=self.font_YaHei_8)
        rpt.Detail.AddItem(3,
                           620,
                           0,
                           100,
                           25,
                           fns[5],
                           AlignmentFlag=al_l,
                           FormatString=' {}',
                           Font=self.font_YaHei_8)

        sum_j = 0
        for i in range(len(cur_tab)):
            sum_j += cur_tab.getOnlyData([i, 4])

        rpt.ReportFooter.AddPrintLables(
            0,
            0,
            25,
            Texts=["合计Sum", JPGetDisplayText(sum_j), " "],
            Widths=[260, 140, 320],
            Aligns=[al_c, al_r, al_c],
            FillColor=QColor(128, 128, 128))

        title = [
            '收款方式\nPaymentMethod', '收款合计\nCollection of receipts',
            '收款笔数\nNumber of Payments Received]'
        ]
        fns = [fld.FieldName for fld in tongji_tab.Fields]
        cols = len(tongji_tab.Fields)
        rpt.ReportFooter.AddPrintLables(0,
                                        45,
                                        40,
                                        Texts=title,
                                        Widths=[240, 240, 240],
                                        Aligns=[al_c] * cols)
        sum_j = 0
        count = 0
        for r in range(len(tongji_tab)):
            rpt.ReportFooter.AddItem(1,
                                     0,
                                     85 + r * 25,
                                     240,
                                     25,
                                     tongji_tab.getDispText([r, 0]),
                                     AlignmentFlag=al_c)
            rpt.ReportFooter.AddItem(1,
                                     240,
                                     85 + r * 25,
                                     240,
                                     25,
                                     tongji_tab.getDispText([r, 1]),
                                     FormatString='{} ',
                                     AlignmentFlag=al_r,
                                     Font=self.font_YaHei_8)
            rpt.ReportFooter.AddItem(1,
                                     480,
                                     85 + r * 25,
                                     240,
                                     25,
                                     tongji_tab.getDispText([r, 2]),
                                     AlignmentFlag=al_c,
                                     Font=self.font_YaHei_8)
            sum_j = sum_j + tongji_tab.getOnlyData([r, 1])
            count = count + tongji_tab.getOnlyData([r, 2])
        rs = len(tongji_tab)
        rpt.ReportFooter.AddItem(1,
                                 0,
                                 85 + rs * 25,
                                 240,
                                 25,
                                 '合计Sum',
                                 AlignmentFlag=al_c,
                                 FillColor=QColor(128, 128, 128))
        rpt.ReportFooter.AddItem(1,
                                 240,
                                 85 + rs * 25,
                                 240,
                                 25,
                                 JPGetDisplayText(sum_j),
                                 AlignmentFlag=al_r,
                                 FillColor=QColor(128, 128, 128),
                                 Font=self.font_YaHei_8)
        rpt.ReportFooter.AddItem(1,
                                 480,
                                 85 + rs * 25,
                                 240,
                                 25,
                                 JPGetDisplayText(count),
                                 AlignmentFlag=al_c,
                                 FillColor=QColor(128, 128, 128),
                                 Font=self.font_YaHei_8)

        rpt.ReportFooter.AddItem(1,
                                 0,
                                 85 + rs * 25+25,
                                 240,
                                 25,
                                 'Credito',
                                 AlignmentFlag=al_c
                                 )
        rpt.ReportFooter.AddItem(1,
                                 240,
                                 85 + rs * 25+25,
                                 240,
                                 25,
                                 " ",
                                 AlignmentFlag=al_r,
                                 Font=self.font_YaHei_8)
        rpt.ReportFooter.AddItem(1,
                                 480,
                                 85 + rs * 25+25,
                                 240,
                                 25,
                                 " ",
                                 AlignmentFlag=al_c,
                                 Font=self.font_YaHei_8)

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
