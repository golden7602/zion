class JPEditFormDataMode(QObject):
    """本类为编辑窗口数据类型的枚举"""
    Edit = 1
    ReadOnly = 2
    New = 3

    def __init__(self):
        super().__init__()
        self.EditMode = JPEditFormDataMode.ReadOnly