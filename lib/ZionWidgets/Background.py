from PyQt5.QtWidgets import  QWidget
from Ui.Ui_FormBackGround import Ui_Form


class Form_Background(Ui_Form):
    def __init__(self, mainform):
        super().__init__()
        self.Widget = QWidget()
        self.setupUi(self.Widget)
        mainform.addForm(self.Widget)