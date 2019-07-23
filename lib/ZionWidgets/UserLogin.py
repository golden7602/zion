from os import getcwd
from sys import path as jppath
jppath.append(getcwd())

from lib.JPDatabase.Database import JPDb
from Ui.Ui_formUserLogin import U