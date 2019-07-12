# -*- coding: utf-8 -*-


# 原名  JPExceptionFieldNull
class FieldNullError(Exception): 
    def __init__(self, obj, msg=None):
        self.Message = obj if isinstance(obj,
                                         str) else "字段的【{}】值不能为空值！".format(msg)

    def __str__(self):
        return self.Message