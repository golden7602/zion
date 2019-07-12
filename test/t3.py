
#!/usr/bin/env python3
import platform
import sys
import html
from PyQt5.QtCore import QSize, Qt,pyqtSignal
from PyQt5.QtGui import QColor, QFont,QFontMetrics, QIcon, QKeySequence, QPixmap,QTextCharFormat
from PyQt5.QtWidgets import QAction,QApplication,QMenu,QTextEdit



class RichTextLineEdit(QTextEdit):
    returnPressed=pyqtSignal()
    (Bold, Italic, Underline, StrikeOut, Monospaced, Sans, Serif,
     NoSuperOrSubscript, Subscript, Superscript) = range(10)


    def __init__(self, parent=None):
        super(RichTextLineEdit, self).__init__(parent)

        self.monofamily = "courier"
        self.sansfamily = "helvetica"
        self.seriffamily = "times"
        self.setLineWrapMode(QTextEdit.NoWrap)
        self.setTabChangesFocus(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        fm = QFontMetrics(self.font())
        h = int(fm.height() * (1.4 if platform.system() == "Windows"
                                   else 1.2))
        self.setMinimumHeight(h)
        self.setMaximumHeight(int(h * 1.2))
        self.setToolTip("Press Ctrl+M for the text effects "
                "menu and Ctrl+K for the color menu")

    
    def toggleItalic(self):
        self.setFontItalic(not self.fontItalic())


    def toggleUnderline(self):
        self.setFontUnderline(not self.fontUnderline())


    def toggleBold(self):
        self.setFontWeight(QFont.Normal
                if self.fontWeight() > QFont.Normal else QFont.Bold)


    def sizeHint(self):
        return QSize(self.document().idealWidth() + 5,
                     self.maximumHeight())


    def minimumSizeHint(self):
        fm = QFontMetrics(self.font())
        return QSize(fm.width("WWWW"), self.minimumHeight())


    def contextMenuEvent(self, event):
        self.textEffectMenu()

        
    def keyPressEvent(self, event):
        if event.modifiers() & Qt.ControlModifier:
            handled = False
            if event.key() == Qt.Key_B:
                self.toggleBold()
                handled = True
            elif event.key() == Qt.Key_I:
                self.toggleItalic()
                handled = True
            elif event.key() == Qt.Key_K:
                self.colorMenu()
                handled = True
            elif event.key() == Qt.Key_M:
                self.textEffectMenu()
                handled = True
            elif event.key() == Qt.Key_U:
                self.toggleUnderline()
                handled = True
            if handled:
                event.accept()
                return
        if event.key() in (Qt.Key_Enter, Qt.Key_Return):
            self.returnPressed.emit()
            event.accept()
        else:
            QTextEdit.keyPressEvent(self, event)


    def colorMenu(self):
        pixmap = QPixmap(22, 22)
        menu = QMenu("Colour")
        for text, color in (
                ("&Black", Qt.black),
                ("B&lue", Qt.blue),
                ("Dark Bl&ue", Qt.darkBlue),
                ("&Cyan", Qt.cyan),
                ("Dar&k Cyan", Qt.darkCyan),
                ("&Green", Qt.green),
                ("Dark Gr&een", Qt.darkGreen),
                ("M&agenta", Qt.magenta),
                ("Dark Mage&nta", Qt.darkMagenta),
                ("&Red", Qt.red),
                ("&Dark Red", Qt.darkRed)):
            color = QColor(color)
            pixmap.fill(color)
            action = menu.addAction(QIcon(pixmap), text, self.setColor)
            action.setData(color)
        self.ensureCursorVisible()
        menu.exec_(self.viewport().mapToGlobal(
                   self.cursorRect().center()))


    def setColor(self):
        action = self.sender()
        if action is not None and isinstance(action, QAction):
            color = QColor(action.data())
            if color.isValid():
                self.setTextColor(color)


    def textEffectMenu(self):
        format = self.currentCharFormat()
        menu = QMenu("Text Effect")
        for text, shortcut, data, checked in (
                ("&Bold", "Ctrl+B", RichTextLineEdit.Bold,
                 self.fontWeight() > QFont.Normal),
                ("&Italic", "Ctrl+I", RichTextLineEdit.Italic,
                 self.fontItalic()),
                ("Strike &out", None, RichTextLineEdit.StrikeOut,
                 format.fontStrikeOut()),
                ("&Underline", "Ctrl+U", RichTextLineEdit.Underline,
                 self.fontUnderline()),
                ("&Monospaced", None, RichTextLineEdit.Monospaced,
                 format.fontFamily() == self.monofamily),
                ("&Serifed", None, RichTextLineEdit.Serif,
                 format.fontFamily() == self.seriffamily),
                ("S&ans Serif", None, RichTextLineEdit.Sans,
                 format.fontFamily() == self.sansfamily),
                ("&No super or subscript", None,
                 RichTextLineEdit.NoSuperOrSubscript,
                 format.verticalAlignment() ==
                 QTextCharFormat.AlignNormal),
                ("Su&perscript", None, RichTextLineEdit.Superscript,
                 format.verticalAlignment() ==
                 QTextCharFormat.AlignSuperScript),
                ("Subs&cript", None, RichTextLineEdit.Subscript,
                 format.verticalAlignment() ==
                 QTextCharFormat.AlignSubScript)):
            action = menu.addAction(text, self.setTextEffect)
            if shortcut is not None:
                action.setShortcut(QKeySequence(shortcut))
            action.setData(data)
            action.setCheckable(True)
            action.setChecked(checked)
        self.ensureCursorVisible()
        menu.exec_(self.viewport().mapToGlobal(
                   self.cursorRect().center()))


    def setTextEffect(self):
        action = self.sender()
        if action is not None and isinstance(action, QAction):
            what = action.data()
            if what == RichTextLineEdit.Bold:
                self.toggleBold()
                return
            if what == RichTextLineEdit.Italic:
                self.toggleItalic()
                return
            if what == RichTextLineEdit.Underline:
                self.toggleUnderline()
                return
            format = self.currentCharFormat()
            if what == RichTextLineEdit.Monospaced:
                format.setFontFamily(self.monofamily)
            elif what == RichTextLineEdit.Serif:
                format.setFontFamily(self.seriffamily)
            elif what == RichTextLineEdit.Sans:
                format.setFontFamily(self.sansfamily)
            if what == RichTextLineEdit.StrikeOut:
                format.setFontStrikeOut(not format.fontStrikeOut())
            if what == RichTextLineEdit.NoSuperOrSubscript:
                format.setVerticalAlignment(
                        QTextCharFormat.AlignNormal)
            elif what == RichTextLineEdit.Superscript:
                format.setVerticalAlignment(
                        QTextCharFormat.AlignSuperScript)
            elif what == RichTextLineEdit.Subscript:
                format.setVerticalAlignment(
                        QTextCharFormat.AlignSubScript)
            self.mergeCurrentCharFormat(format)


    def toSimpleHtml(self):
        htmltext = ""
        black = QColor(Qt.black)
        block = self.document().begin()
        while block.isValid():
            iterator = block.begin()
            while iterator != block.end():
                fragment = iterator.fragment()
                if fragment.isValid():
                    format = fragment.charFormat()
                    family = format.fontFamily()
                    color = format.foreground().color()                  
                    text=html.escape(fragment.text())
                    if (format.verticalAlignment() ==
                        QTextCharFormat.AlignSubScript):
                        text = "{0}".format(text)
                    elif (format.verticalAlignment() ==
                          QTextCharFormat.AlignSuperScript):
                        text = "{0}".format(text)
                    if format.fontUnderline():
                        text = "{0}".format(text)
                    if format.fontItalic():
                        text = "{0}".format(text)
                    if format.fontWeight() > QFont.Normal:
                        text = "{0}".format(text)
                    if format.fontStrikeOut():
                        text = "{0}".format(text)
                    if color != black or family:
                        attribs = ""
                        if color != black:
                            attribs += ' color="{0}"'.format(color.name())
                        if family:
                            attribs += ' face="{0}"'.format(family)
                        text = "{1}".format(attribs,text)
                    htmltext += text
                iterator += 1
            block = block.next()
        return htmltext

if __name__ == "__main__":
    def printout(lineedit):
        print(str(lineedit.toHtml()))
        print(str(lineedit.toPlainText()))
        print(str(lineedit.toSimpleHtml()))                
    app = QApplication(sys.argv)
    lineedit = RichTextLineEdit()
    lineedit.returnPressed.connect(lambda:printout(lineedit))
    lineedit.show()
    lineedit.setWindowTitle("RichTextEdit")
    app.exec_()

/home/yrd/eric_workspace/chap14/ships_delegate_ans/ships_ans.py


#!/usr/bin/env python3

import platform
import re
from PyQt5.QtCore import (QAbstractTableModel, QDataStream, QFile,
                          QIODevice, QModelIndex,QRegExp, QSize,QVariant, Qt,pyqtSignal)
from PyQt5.QtGui import QColor,QTextDocument
from PyQt5.QtWidgets import QApplication, QWidget,QComboBox, QLineEdit,QSpinBox, QStyle,QStyledItemDelegate, QTextEdit
import richtextlineedit

NAME, OWNER, COUNTRY, DESCRIPTION, TEU = range(5)

MAGIC_NUMBER = 0x570C4
FILE_VERSION = 1


class Ship(object):

    def __init__(self, name, owner, country, teu=0, description=""):
        self.name = name
        self.owner = owner
        self.country = country
        self.teu = teu
        self.description = description


    def __hash__(self):
        return super(Ship, self).__hash__()


    def __lt__(self, other):
        return bool(self.name.lower()


    def __eq__(self, other):
        return bool(self.name.lower()==other.name.lower())


class ShipTableModel(QAbstractTableModel):
    dataChanged = pyqtSignal(QModelIndex,QModelIndex)
    def __init__(self, filename=""):
        super(ShipTableModel, self).__init__()
        self.filename = filename
        self.dirty = False
        self.ships = []
        self.owners = set()
        self.countries = set()


    def sortByName(self):
        self.beginResetModel()
        self.ships = sorted(self.ships)
        self.endResetModel()


    def sortByTEU(self):
        self.beginResetModel()
        ships = [(ship.teu, ship) for ship in self.ships]
        ships.sort()
        self.ships = [ship for teu, ship in ships]
        self.endResetModel()


    def sortByCountryOwner(self):
        self.beginResetModel()
        self.ships = sorted(self.ships,
                            key=lambda x: (x.country, x.owner, x.name))
        self.endResetModel()


    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemFlags(QAbstractTableModel.flags(self, index)|
                            Qt.ItemIsEditable)


    def data(self, index, role=Qt.DisplayRole):
        if (not index.isValid() or
            not (0 <= index.row() < len(self.ships))):
            return QVariant()
        ship = self.ships[index.row()]
        column = index.column()
        if role == Qt.DisplayRole:
            if column == NAME:
                return ship.name
            elif column == OWNER:
                return ship.owner
            elif column == COUNTRY:
                return ship.country
            elif column == DESCRIPTION:
                return ship.description
            elif column == TEU:
                return "{0}".format(ship.teu)
        elif role == Qt.TextAlignmentRole:
            if column == TEU:
                return QVariant(int(Qt.AlignRight|Qt.AlignVCenter))
            return QVariant(int(Qt.AlignLeft|Qt.AlignVCenter))
        elif role == Qt.TextColorRole and column == TEU:
            if ship.teu < 80000:
                return QVariant(QColor(Qt.black))
            elif ship.teu < 100000:
                return QVariant(QColor(Qt.darkBlue))
            elif ship.teu < 120000:
                return QVariant(QColor(Qt.blue))
            else:
                return QVariant(QColor(Qt.red))
        elif role == Qt.BackgroundColorRole:
            if ship.country in ("Bahamas", "Cyprus", "Denmark",
                    "France", "Germany", "Greece"):
                return QVariant(QColor(250, 230, 250))
            elif ship.country in ("Hong Kong", "Japan", "Taiwan"):
                return QVariant(QColor(250, 250, 230))
            elif ship.country in ("Marshall Islands",):
                return QVariant(QColor(230, 250, 250))
            else:
                return QVariant(QColor(210, 230, 230))
        elif role == Qt.ToolTipRole:
            msg = "
(minimum of 3 characters)"
            if column == NAME:
                return ship.name + msg
            elif column == OWNER:
                return ship.owner + msg
            elif column == COUNTRY:
                return ship.country + msg
            elif column == DESCRIPTION:
                return ship.description
            elif column == TEU:
                return "{0} twenty foot equivalents".format(ship.teu)
        return QVariant()


    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.TextAlignmentRole:
            if orientation == Qt.Horizontal:
                return QVariant(int(Qt.AlignLeft|Qt.AlignVCenter))
            return QVariant(int(Qt.AlignRight|Qt.AlignVCenter))
        if role != Qt.DisplayRole:
            return QVariant()
        if orientation == Qt.Horizontal:
            if section == NAME:
                return "Name"
            elif section == OWNER:
                return "Owner"
            elif section == COUNTRY:
                return "Country"
            elif section == DESCRIPTION:
                return "Description"
            elif section == TEU:
                return "TEU"
        return QVariant(int(section + 1))


    def rowCount(self, index=QModelIndex()):
        return len(self.ships)


    def columnCount(self, index=QModelIndex()):
        return 5


    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and 0 <= index.row() < len(self.ships):
            ship = self.ships[index.row()]
            column = index.column()
            if column == NAME:
                ship.name = value
            elif column == OWNER:
                ship.owner = value
            elif column == COUNTRY:
                ship.country = value
            elif column == DESCRIPTION:
                ship.description = value
            elif column == TEU:
                if str(value).isdecimal():
                    ship.teu=int(value)
            self.dirty = True
            self.dataChanged[QModelIndex,QModelIndex].emit(index,index)
            return True
        return False


    def insertRows(self, position, rows=1, index=QModelIndex()):
        self.beginInsertRows(QModelIndex(), position, position + rows - 1)
        for row in range(rows):
            self.ships.insert(position + row,
                              Ship(" Unknown", " Unknown", " Unknown"))
        self.endInsertRows()
        self.dirty = True
        return True


    def removeRows(self, position, rows=1, index=QModelIndex()):
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
        self.ships = (self.ships[:position] + self.ships[position + rows:])
        self.endRemoveRows()
        self.dirty = True
        return True


    def load(self):
        exception = None
        fh = None
        try:
            if not self.filename:
                raise IOError("no filename specified for loading")
            fh = QFile(self.filename)
            if not fh.open(QIODevice.ReadOnly):
                raise IOError(str(fh.errorString()))
            stream = QDataStream(fh)
            magic = stream.readInt32()
            if magic != MAGIC_NUMBER:
                raise IOError("unrecognized file type")
            fileVersion = stream.readInt16()
            if fileVersion != FILE_VERSION:
                raise IOError("unrecognized file type version")
            self.ships = []
            while not stream.atEnd():
                name = ""
                owner = ""
                country = ""
                description = ""
                name=stream.readQString()
                owner=stream.readQString()
                country=stream.readQString()
                description=stream.readQString()
                teu = stream.readInt32()
                self.ships.append(Ship(name, owner, country, teu,
                                       description))
                self.owners.add(str(owner))
                self.countries.add(str(country))
            self.dirty = False
        except IOError as e:
            exception = e
        finally:
            if fh is not None:
                fh.close()
            if exception is not None:
                raise exception


    def save(self):
        exception = None
        fh = None
        try:
            if not self.filename:
                raise IOError("no filename specified for saving")
            fh = QFile(self.filename)
            if not fh.open(QIODevice.WriteOnly):
                raise IOError(str(fh.errorString()))
            stream = QDataStream(fh)
            stream.writeInt32(MAGIC_NUMBER)
            stream.writeInt16(FILE_VERSION)
            stream.setVersion(QDataStream.Qt_5_7)
            for ship in self.ships:
                stream.writeQString(ship.name)
                stream.writeQString(ship.owner)
                stream.writeQString(ship.country)
                stream.writeQString(ship.description)
                stream.writeInt32(ship.teu)                
            self.dirty = False
        except IOError as e:
            exception = e
        finally:
            if fh is not None:
                fh.close()
            if exception is not None:
                raise exception


class ShipDelegate(QStyledItemDelegate):
    commitData = pyqtSignal(QWidget)
    closeEditor = pyqtSignal(QWidget)
    def __init__(self, parent=None):
        super(ShipDelegate, self).__init__(parent)


    def paint(self, painter, option, index):
        if index.column() == DESCRIPTION:
            text = str(index.model().data(index))
            palette = QApplication.palette()
            document = QTextDocument()
            document.setDefaultFont(option.font)
            if option.state & QStyle.State_Selected:
                #document.setHtml("{1}".format("#FF0000",text))
                document.setHtml("{1}".format(palette.highlightedText().color().name(),text))
            else:
                document.setHtml(text)
            color = (palette.highlight().color()
                     if option.state & QStyle.State_Selected
                     else QColor(index.model().data(index,
                                 Qt.BackgroundColorRole)))
            #print(palette.highlight().color().name())
            painter.save()
            painter.fillRect(option.rect, color)
            painter.translate(option.rect.x(), option.rect.y())
            document.drawContents(painter)
            painter.restore()
        else:
            QStyledItemDelegate.paint(self, painter, option, index)


    def sizeHint(self, option, index):
        fm = option.fontMetrics
        if index.column() == TEU:
            return QSize(fm.width("9,999,999"), fm.height())
        if index.column() == DESCRIPTION:
            text = str(index.model().data(index))
            document = QTextDocument()
            document.setDefaultFont(option.font)
            document.setHtml(text)
            return QSize(document.idealWidth() + 5, fm.height())
        return QStyledItemDelegate.sizeHint(self, option, index)


    def createEditor(self, parent, option, index):
        if index.column() == TEU:
            spinbox = QSpinBox(parent)
            spinbox.setRange(0, 200000)
            spinbox.setSingleStep(1000)
            spinbox.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
            #add by yrd
            spinbox.valueChanged.connect(self.commitAndCloseEditor)
            return spinbox
        elif index.column() == OWNER:
            combobox = QComboBox(parent)
            combobox.addItems(sorted(index.model().owners))
            combobox.setEditable(True)
            #add by yrd
            #combobox.currentTextChanged.connect(self.commitAndCloseEditor)
            combobox.editTextChanged.connect(self.commitAndCloseEditor)
            return combobox
        elif index.column() == COUNTRY:
            combobox = QComboBox(parent)
            combobox.addItems(sorted(index.model().countries))
            combobox.setEditable(True)
            #add by yrd
            combobox.editTextChanged.connect(self.commitAndCloseEditor)
            return combobox
        elif index.column() == NAME:
            editor = QLineEdit(parent)
            editor.returnPressed.connect(self.commitAndCloseEditor)
            return editor
        elif index.column() == DESCRIPTION:
            editor = richtextlineedit.RichTextLineEdit(parent)
            editor.returnPressed.connect(self.commitAndCloseEditor)
            return editor
        else:
            return QStyledItemDelegate.createEditor(self, parent, option,
                                                    index)


        
    def commitAndCloseEditor(self):
        editor = self.sender()
        if isinstance(editor, (QTextEdit, QLineEdit,QSpinBox,QComboBox)):
            self.commitData[QWidget].emit(editor)
            self.closeEditor[QWidget].emit(editor)
            
            



    def setEditorData(self, editor, index):
        text = index.model().data(index, Qt.DisplayRole)
        if index.column() == TEU:
            value=int(re.sub("[., ]","",text))
            editor.setValue(value)
        elif index.column() in (OWNER, COUNTRY):
            i = editor.findText(text)
            if i == -1:
                i = 0
            editor.setCurrentIndex(i)
        elif index.column() == NAME:
            editor.setText(text)
        elif index.column() == DESCRIPTION:
            editor.setHtml(text)
        else:
            QStyledItemDelegate.setEditorData(self, editor, index)


    def setModelData(self, editor, model, index):
        if index.column() == TEU:
            model.setData(index, editor.value())
        elif index.column() in (OWNER, COUNTRY):
            text = editor.currentText()
            if len(text) >= 3:
                model.setData(index, text)
        elif index.column() == NAME:
            text = editor.text()
            if len(text) >= 3:
                model.setData(index, text)
        elif index.column() == DESCRIPTION:
            model.setData(index, editor.toSimpleHtml())
        else:
            QStyledItemDelegate.setModelData(self, editor, model, index)


def generateFakeShips():
    for name, owner, country, teu, description in (
("Emma M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 151687,
 "W\u00E4rtsil\u00E4-Sulzer RTA96-C main engine,"
 "109,000 hp"),
("MSC Pamela", "MSC", "Liberia", 90449,
 "Draft 15m"),
("Colombo Express", "Hapag-Lloyd", "Germany", 93750,
 "Main engine, 93,500 hp"),
("Houston Express", "Norddeutsche Reederei", "Germany", 95000,
 "Features a twisted leading edge full spade rudder. "
 "Sister of Savannah Express"),
("Savannah Express", "Norddeutsche Reederei", "Germany", 95000,
 "Sister of Houston Express"),
("MSC Susanna", "MSC", "Liberia", 90449, ""),
("Eleonora M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 151687,
 "Captain Hallam"),
("Estelle M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 151687,
 "Captain Wells"),
("Evelyn M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 151687,
  "Captain Byrne"),
("Georg M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 97933, ""),
("Gerd M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 97933, ""),
("Gjertrud M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 97933, ""),
("Grete M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 97933, ""),
("Gudrun M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 97933, ""),
("Gunvor M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 97933, ""),
("CSCL Le Havre", "Danaos Shipping", "Cyprus", 107200, ""),
("CSCL Pusan", "Danaos Shipping", "Cyprus", 107200,
 "Captain Watts"),
("Xin Los Angeles", "China Shipping Container Lines (CSCL)",
 "Hong Kong", 107200, ""),
("Xin Shanghai", "China Shipping Container Lines (CSCL)", "Hong Kong",
 107200, ""),
("Cosco Beijing", "Costamare Shipping", "Greece", 99833, ""),
("Cosco Hellas", "Costamare Shipping", "Greece", 99833, ""),
("Cosco Guangzho", "Costamare Shipping", "Greece", 99833, ""),
("Cosco Ningbo", "Costamare Shipping", "Greece", 99833, ""),
("Cosco Yantian", "Costamare Shipping", "Greece", 99833, ""),
("CMA CGM Fidelio", "CMA CGM", "France", 99500, ""),
("CMA CGM Medea", "CMA CGM", "France", 95000, ""),
("CMA CGM Norma", "CMA CGM", "Bahamas", 95000, ""),
("CMA CGM Rigoletto", "CMA CGM", "France", 99500, ""),
("Arnold M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 93496,
 "Captain Morrell"),
("Anna M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 93496,
 "Captain Lockhart"),
("Albert M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 93496,
 "Captain Tallow"),
("Adrian M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 93496,
 "Captain G. E. Ericson"),
("Arthur M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 93496, ""),
("Axel M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 93496, ""),
("NYK Vega", "Nippon Yusen Kaisha", "Panama", 97825, ""),
("MSC Esthi", "MSC", "Liberia", 99500, ""),
("MSC Chicago", "Offen Claus-Peter", "Liberia", 90449, ""),
("MSC Bruxelles", "Offen Claus-Peter", "Liberia", 90449, ""),
("MSC Roma", "Offen Claus-Peter", "Liberia", 99500, ""),
("MSC Madeleine", "MSC", "Liberia", 107551, ""),
("MSC Ines", "MSC", "Liberia", 107551, ""),
("Hannover Bridge", "Kawasaki Kisen Kaisha", "Japan", 99500, ""),
("Charlotte M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
("Clementine M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
("Columbine M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
("Cornelia M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
("Chicago Express", "Hapag-Lloyd", "Germany", 93750, ""),
("Kyoto Express", "Hapag-Lloyd", "Germany", 93750, ""),
("Clifford M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
("Sally M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
("Sine M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
("Skagen M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
("Sofie M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
("Sor\u00F8 M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
("Sovereing M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
("Susan M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
("Svend M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
("Svendborg M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
("A.P. M\u00F8ller", "M\u00E6rsk Line", "Denmark", 91690,
 "Captain Ferraby"),
("Caroline M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
("Carsten M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
("Chastine M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
("Cornelius M\u00E6rsk", "M\u00E6rsk Line", "Denmark", 91690, ""),
("CMA CGM Otello", "CMA CGM", "France", 91400, ""),
("CMA CGM Tosca", "CMA CGM", "France", 91400, ""),
("CMA CGM Nabucco", "CMA CGM", "France", 91400, ""),
("CMA CGM La Traviata", "CMA CGM", "France", 91400, ""),
("CSCL Europe", "Danaos Shipping", "Cyprus", 90645, ""),
("CSCL Africa", "Seaspan Container Line", "Cyprus", 90645, ""),
("CSCL America", "Danaos Shipping ", "Cyprus", 90645, ""),
("CSCL Asia", "Seaspan Container Line", "Hong Kong", 90645, ""),
("CSCL Oceania", "Seaspan Container Line", "Hong Kong", 90645,
 "Captain Baker"),
("M\u00E6rsk Seville", "Blue Star GmbH", "Liberia", 94724, ""),
("M\u00E6rsk Santana", "Blue Star GmbH", "Liberia", 94724, ""),
("M\u00E6rsk Sheerness", "Blue Star GmbH", "Liberia", 94724, ""),
("M\u00E6rsk Sarnia", "Blue Star GmbH", "Liberia", 94724, ""),
("M\u00E6rsk Sydney", "Blue Star GmbH", "Liberia", 94724, ""),
("MSC Heidi", "MSC", "Panama", 95000, ""),
("MSC Rania", "MSC", "Panama", 95000, ""),
("MSC Silvana", "MSC", "Panama", 95000, ""),
("M\u00E6rsk Stralsund", "Blue Star GmbH", "Liberia", 95000, ""),
("M\u00E6rsk Saigon", "Blue Star GmbH", "Liberia", 95000, ""),
("M\u00E6rsk Seoul", "Blue Star Ship Managment GmbH", "Germany",
 95000, ""),
("M\u00E6rsk Surabaya", "Offen Claus-Peter", "Germany", 98400, ""),
("CMA CGM Hugo", "NSB Niederelbe", "Germany", 90745, ""),
("CMA CGM Vivaldi", "CMA CGM", "Bahamas", 90745, ""),
("MSC Rachele", "NSB Niederelbe", "Germany", 90745, ""),
("Pacific Link", "NSB Niederelbe", "Germany", 90745, ""),
("CMA CGM Carmen", "E R Schiffahrt", "Liberia", 89800, ""),
("CMA CGM Don Carlos", "E R Schiffahrt", "Liberia", 89800, ""),
("CMA CGM Don Giovanni", "E R Schiffahrt", "Liberia", 89800, ""),
("CMA CGM Parsifal", "E R Schiffahrt", "Liberia", 89800, ""),
("Cosco China", "E R Schiffahrt", "Liberia", 91649, ""),
("Cosco Germany", "E R Schiffahrt", "Liberia", 89800, ""),
("Cosco Napoli", "E R Schiffahrt", "Liberia", 89800, ""),
("YM Unison", "Yang Ming Line", "Taiwan", 88600, ""),
("YM Utmost", "Yang Ming Line", "Taiwan", 88600, ""),
("MSC Lucy", "MSC", "Panama", 89954, ""),
("MSC Maeva", "MSC", "Panama", 89954, ""),
("MSC Rita", "MSC", "Panama", 89954, ""),
("MSC Busan", "Offen Claus-Peter", "Panama", 89954, ""),
("MSC Beijing", "Offen Claus-Peter", "Panama", 89954, ""),
("MSC Toronto", "Offen Claus-Peter", "Panama", 89954, ""),
("MSC Charleston", "Offen Claus-Peter", "Panama", 89954, ""),
("MSC Vittoria", "MSC", "Panama", 89954, ""),
("Ever Champion", "NSB Niederelbe", "Marshall Islands", 90449,
 "Captain Phillips"),
("Ever Charming", "NSB Niederelbe", "Marshall Islands", 90449,
 "Captain Tonbridge"),
("Ever Chivalry", "NSB Niederelbe", "Marshall Islands", 90449, ""),
("Ever Conquest", "NSB Niederelbe", "Marshall Islands", 90449, ""),
("Ital Contessa", "NSB Niederelbe", "Marshall Islands", 90449, ""),
("Lt Cortesia", "NSB Niederelbe", "Marshall Islands", 90449, ""),
("OOCL Asia", "OOCL", "Hong Kong", 89097, ""),
("OOCL Atlanta", "OOCL", "Hong Kong", 89000, ""),
("OOCL Europe", "OOCL", "Hong Kong", 89097, ""),
("OOCL Hamburg", "OOCL", "Marshall Islands", 89097, ""),
("OOCL Long Beach", "OOCL", "Marshall Islands", 89097, ""),
("OOCL Ningbo", "OOCL", "Marshall Islands", 89097, ""),
("OOCL Shenzhen", "OOCL", "Hong Kong", 89097, ""),
("OOCL Tianjin", "OOCL", "Marshall Islands", 89097, ""),
("OOCL Tokyo", "OOCL", "Hong Kong", 89097, "")):
        yield Ship(name, owner, country, teu, description)



/home/yrd/eric_workspace/chap14/ships_delegate_ans/ships-delegate_ans.pyw


#!/usr/bin/env python3

import sys
import re
from PyQt5.QtCore import QFile, QIODevice, QRegExp, QTextStream,QTimer, Qt
from PyQt5.QtWidgets import (QApplication, QDialog, QFileDialog,QHBoxLayout, QLabel,
                             QMessageBox, QPushButton, QSplitter, QTableView, QVBoxLayout,
                             QWidget)
import ships_ans as ships

MAC = True
try:
    from PyQt5.QtGui import qt_mac_set_native_menubar
except ImportError:
    MAC = False


class MainForm(QDialog):

    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)

        self.model = ships.ShipTableModel("ships.dat")
        tableLabel1 = QLabel("Table &1")
        self.tableView1 = QTableView()
        tableLabel1.setBuddy(self.tableView1)
        self.tableView1.setModel(self.model)
        self.tableView1.setItemDelegate(ships.ShipDelegate(self))
        tableLabel2 = QLabel("Table &2")
        self.tableView2 = QTableView()
        tableLabel2.setBuddy(self.tableView2)
        self.tableView2.setModel(self.model)
        self.tableView2.setItemDelegate(ships.ShipDelegate(self))

        addShipButton = QPushButton("&Add Ship")
        removeShipButton = QPushButton("&Remove Ship")
        exportButton = QPushButton("E&xport...")
        quitButton = QPushButton("&Quit")
        if not MAC:
            addShipButton.setFocusPolicy(Qt.NoFocus)
            removeShipButton.setFocusPolicy(Qt.NoFocus)
            exportButton.setFocusPolicy(Qt.NoFocus)
            quitButton.setFocusPolicy(Qt.NoFocus)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(addShipButton)
        buttonLayout.addWidget(removeShipButton)
        buttonLayout.addWidget(exportButton)
        buttonLayout.addStretch()
        buttonLayout.addWidget(quitButton)
        splitter = QSplitter(Qt.Horizontal)
        vbox = QVBoxLayout()
        vbox.addWidget(tableLabel1)
        vbox.addWidget(self.tableView1)
        widget = QWidget()
        widget.setLayout(vbox)
        splitter.addWidget(widget)
        vbox = QVBoxLayout()
        vbox.addWidget(tableLabel2)
        vbox.addWidget(self.tableView2)
        widget = QWidget()
        widget.setLayout(vbox)
        splitter.addWidget(widget)
        layout = QVBoxLayout()
        layout.addWidget(splitter)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)

        for tableView in (self.tableView1, self.tableView2):
            header = tableView.horizontalHeader()
            header.sectionClicked[int].connect(self.sortTable)
        
        addShipButton.clicked.connect(self.addShip)
        removeShipButton.clicked.connect(self.removeShip)
        exportButton.clicked.connect(self.export)
        quitButton.clicked.connect(self.accept)

        self.setWindowTitle("Ships (delegate)")
        QTimer.singleShot(0, self.initialLoad)


    def initialLoad(self):
        if not QFile.exists(self.model.filename):
            self.model.beginResetModel()
            for ship in ships.generateFakeShips():
                self.model.ships.append(ship)
                self.model.owners.add(str(ship.owner))
                self.model.countries.add(str(ship.country))
            self.model.endResetModel()
            self.model.dirty = False
        else:
            try:
                self.model.load()
            except IOError as e:
                QMessageBox.warning(self, "Ships - Error",
                        "Failed to load: {0}".format(e))
        self.model.sortByName()
        self.resizeColumns()


    def resizeColumns(self):
        self.tableView1.resizeColumnsToContents()
        self.tableView2.resizeColumnsToContents()


    def reject(self):
        self.accept()


    def accept(self):
        if (self.model.dirty and
            QMessageBox.question(self, "Ships - Save?",
                    "Save unsaved changes?",
                    QMessageBox.Yes|QMessageBox.No) ==
                    QMessageBox.Yes):
            try:
                self.model.save()
            except IOError as e:
                QMessageBox.warning(self, "Ships - Error",
                        "Failed to save: {0}".format(e))
        QDialog.accept(self)

    
    def sortTable(self, section):
        if section in (ships.OWNER, ships.COUNTRY):
            self.model.sortByCountryOwner()
        elif section == ships.TEU:
            self.model.sortByTEU()
        else:
            self.model.sortByName()
        self.resizeColumns()


    def addShip(self):
        row = self.model.rowCount()
        self.model.insertRows(row)
        index = self.model.index(row, 0)
        tableView = self.tableView1
        if self.tableView2.hasFocus():
            tableView = self.tableView2
        tableView.setFocus()
        tableView.setCurrentIndex(index)
        tableView.edit(index)


    def removeShip(self):
        tableView = self.tableView1
        if self.tableView2.hasFocus():
            tableView = self.tableView2
        index = tableView.currentIndex()
        if not index.isValid():
            return
        row = index.row()
        name = self.model.data(
                    self.model.index(row, ships.NAME))
        owner = self.model.data(
                    self.model.index(row, ships.OWNER))
        country = self.model.data(
                    self.model.index(row, ships.COUNTRY))
        if (QMessageBox.question(self, "Ships - Remove",
                "Remove {0} of {1}/{2}?".format(name,owner,country),
                QMessageBox.Yes|QMessageBox.No) ==
                QMessageBox.No):
            return
        self.model.removeRows(row)
        self.resizeColumns()


    def export(self):
        filename = str(QFileDialog.getSaveFileName(self,
                "Ships - Choose Export File", ".", "Export files (*.txt)")[0])
        if not filename:
            return
        #htmlTags = QRegExp(r"<[^>]+>")
        htmlTags="<[^>]+>"
        #htmlTags.setMinimal(True)
        nonDigits ="[., ]"
        self.model.sortByCountryOwner()
        fh = None
        try:
            fh = QFile(filename)
            if not fh.open(QIODevice.WriteOnly):
                raise IOError(str(fh.errorString()))
            stream = QTextStream(fh)
            stream.setCodec("UTF-8")
            for row in range(self.model.rowCount()):
                name = self.model.data(
                        self.model.index(row, ships.NAME))
                owner = self.model.data(
                        self.model.index(row, ships.OWNER))
                country = self.model.data(
                        self.model.index(row, ships.COUNTRY))
                teu = self.model.data(
                        self.model.index(row, ships.TEU))
                teu = re.sub(nonDigits,"",teu)
                description = self.model.data(
                        (self.model.index(row, ships.DESCRIPTION)))
                description = re.sub(htmlTags,"",description)
                stream << name << "|" << owner << "|" << country \
                       << "|" << str(teu) << "|" << description << "\n"
        except EnvironmentError as e:
            QMessageBox.warning(self, "Ships - Error",
                    "Failed to export: {0}".format(e))
        finally:
            if fh:
                fh.close()
        QMessageBox.warning(self, "Ships - Export",
                "Successfully exported ship to {0}".format(filename))


app = QApplication(sys.argv)
form = MainForm()
form.show()
app.exec_()