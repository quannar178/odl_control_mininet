import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from custom_ui import CusTom_MainWindow
def window():
   app = QApplication(sys.argv)
   w =  CusTom_MainWindow()
   w.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
   window()