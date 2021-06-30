import logging
from PySide2.QtWidgets import QDialog
from ui_dialog import Ui_Dialog

class MyDiaLog(Ui_Dialog, QDialog):
    def __init__(self, is_success ,message) -> None:
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Notice")
        logging.info(message)
        self.lb_message.setText(message)
        if is_success == 1:
            self.lb_message.setStyleSheet("color:rgb(0, 204, 0);")
        else:
            self.lb_message.setStyleSheet("color:rgb(204, 0, 0);")