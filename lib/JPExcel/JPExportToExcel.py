# -*- coding: utf-8 -*-

from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from lib.JPDatabase.Query import JPQueryFieldInfo
from PyQt5.QtWidgets import QFileDialog, QMessageBox

import xlwt


class clsExportToExcelFromTableWidget(object):
    def __init__(self, tableWidget, MainForm):
        self.tableWidget = tableWidget
        self.MainForm = MainForm

    def run(self):
        fileName_choose, filetype = QFileDialog.getSaveFileName(
            self.MainForm,
            "Export To Excel File Name",
            getcwd(),  # 起始路径
            "Excel Files (*.xls)")
        if not fileName_choose:
            return
        tab = self.tableWidget
        book = xlwt.Workbook(encoding='utf-8')  # 新建一个excel
        sheet = book.add_sheet('newsheet')  # 添加一个sheet页
        borders = xlwt.Borders()  # Create Borders
        borders.left = xlwt.Borders.THIN
        # DASHED虚线 NO_LINE没有 THIN实线
        # May be: NO_LINE, THIN, MEDIUM, DASHED,
        # DOTTED, THICK, DOUBLE, HAIR,
        # MEDIUM_DASHED, THIN_DASH_DOTTED,
        # MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED,
        # MEDIUM_DASH_DOT_DOTTED,
        # SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
        borders.right = xlwt.Borders.THIN
        borders.top = xlwt.Borders.THIN
        borders.bottom = xlwt.Borders.THIN
        borders.left_colour = 0x40
        borders.right_colour = 0x40
        borders.top_colour = 0x40
        borders.bottom_colour = 0x40
        style = xlwt.XFStyle()  # Create Style
        style.borders = borders  # Add Borders to Style

        pattern = xlwt.Pattern()  # Create the Pattern
        # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green,
        # 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon,
        # 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow ,
        # almost brown), 20 = Dark Magenta, 21 = Teal,
        # 22 = Light Gray, 23 = Dark Gray, the list goes on...
        pattern.pattern_fore_colour = 22
        style.pattern = pattern  # Add Pattern to Style

        for i in range(0, tab.columnCount()):
            sheet.write(0, i, tab.horizontalHeaderItem(i).text(), style)
        self.MainForm.ProgressBar.show()
        self.MainForm.Label.setText('Exporting')
        self.MainForm.ProgressBar.setRange(0, tab.rowCount())

        pattern1 = xlwt.Pattern()
        pattern1.pattern = xlwt.Pattern.SOLID_PATTERN
        pattern1.pattern_fore_colour = 1
        style1 = xlwt.XFStyle()
        style1.borders = borders
        style1.pattern = pattern1

        for i in range(0, tab.rowCount()):
            for j in range(0, tab.columnCount()):
                self.MainForm.ProgressBar.setValue(i)
                sheet.write(i + 1, j, tab.item(i, j).text(), style1)
        self.MainForm.Label.setText('')
        self.MainForm.ProgressBar.hide()
        book.save(fileName_choose)


class clsExportToExcelFromJPTabelFieldInfo(object):
    def __init__(self, QueryFieldInfo, MainForm):
        self.QueryFieldInfo = QueryFieldInfo
        self.MainForm = MainForm
        self.linkMainTableFieldIndex = 0
        self.linkSubTableFieldIndex = 0

    def run(self):
        fileName_choose, filetype = QFileDialog.getSaveFileName(
            self.MainForm,
            "Export To Excel File Name",
            getcwd(),  # 起始路径
            "Excel Files (*.xls)")
        if not fileName_choose:
            return
        tab = self.QueryFieldInfo
        book = xlwt.Workbook(encoding='utf-8')  # 新建一个excel
        sheet = book.add_sheet('newsheet')  # 添加一个sheet页
        borders = xlwt.Borders()  # Create Borders
        borders.left = xlwt.Borders.THIN
        # DASHED虚线 NO_LINE没有 THIN实线
        # May be: NO_LINE, THIN, MEDIUM, DASHED,
        # DOTTED, THICK, DOUBLE, HAIR,
        # MEDIUM_DASHED, THIN_DASH_DOTTED,
        # MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED,
        # MEDIUM_DASH_DOT_DOTTED,
        # SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
        borders.right = xlwt.Borders.THIN
        borders.top = xlwt.Borders.THIN
        borders.bottom = xlwt.Borders.THIN
        borders.left_colour = 0x40
        borders.right_colour = 0x40
        borders.top_colour = 0x40
        borders.bottom_colour = 0x40
        style = xlwt.XFStyle()  # Create Style
        style.borders = borders  # Add Borders to Style

        pattern = xlwt.Pattern()  # Create the Pattern
        # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        pattern.pattern = xlwt.Pattern.NO_PATTERN
        # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green,
        # 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon,
        # 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow ,
        # almost brown), 20 = Dark Magenta, 21 = Teal,
        # 22 = Light Gray, 23 = Dark Gray, the list goes on...
        pattern.pattern_fore_colour = 22
        style.pattern = pattern  # Add Pattern to Style

        for i in range(len(tab.Fields)):
            sheet.write(0, i, tab.Fields[i].Title, style)
        try:
            self.MainForm.ProgressBar.show()
            self.MainForm.Label.setText('Exporting')
            self.MainForm.ProgressBar.setRange(0, len(tab))
        except Exception:
            pass

        pattern1 = xlwt.Pattern()
        pattern1.pattern = xlwt.Pattern.SOLID_PATTERN
        pattern1.pattern_fore_colour = 1
        style1 = xlwt.XFStyle()
        style1.borders = borders
        style1.pattern = pattern1
        subTab = self.getSubQueryFieldInfo()
        cols = len(tab.Fields)
        sub_cols = len(subTab.Fields)
        if len(subTab):
            i = 0
            row = 0
            for sub_j in range(sub_cols):
                sheet.write(0, cols + sub_j, subTab.Fields[sub_j].Title, style)
            while i < len(tab):
                for j in range(0, cols):
                    try:
                        self.MainForm.ProgressBar.setValue(row)
                    except Exception:
                        pass
                    sheet.write(row + 1, j, tab.getDispText((row, j)), style1)
                sub_rec = [
                    r.Datas for r in subTab.DataRows
                    if r.Datas[self.linkMainTableFieldIndex] == tab.Datas[row][
                        self.linkMainTableFieldIndex]
                ]
                for sub_i in range(len(subTab)):
                    for sub_j in range(sub_cols):
                        print(sub_i, sub_j)
                        sheet.write(row + 1 + sub_i, cols + sub_j,
                                    tab.getDispText((sub_i, sub_j)), style1)
            try:
                self.MainForm.Label.setText('')
                self.MainForm.ProgressBar.hide()
            except Exception:
                pass
        else:
            for i in range(0, len(tab)):
                for j in range(0, cols):
                    try:
                        self.MainForm.ProgressBar.setValue(i)
                    except Exception:
                        pass
                    sheet.write(i + 1, j, tab.getDispText((i, j)), style1)
            try:
                self.MainForm.Label.setText('')
                self.MainForm.ProgressBar.hide()
            except Exception:
                pass
        book.save(fileName_choose)
        QMessageBox.information(self, '', 'Export to excel complete!',
                                QMessageBox.Yes,
                                QMessageBox.Yes) == QMessageBox.Yes

    def getSubQueryFieldInfo(self):
        return []
