# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *

################################################

import re
################################################
class mycla():
    items_list = [[
        "C", "C++", "Java", "Python", "JavaScript", "C#", "Swift", "go",
        "Ruby", "Lua", "PHP"
    ],["C1", "C++1", "Java", "Python", "JavaScript", "C#", "Swift", "go", "Ruby",
      "Lua", "PHP"]]



    def __getitem__(self, index: int):
        return self.items_list[index]


if __name__ == "__main__":
    s="""   select  * from 
     where 
    
    kjdfgjkl """
    p = r"\s*SELECT\s*.*from\s*(\S+)\s*where\s*(\S+)\s*"
    m=re.match(p,s,re.I)
    print(m.groups())