from logging import setLoggerClass
from ui_add_flow_dialog import Ui_AddFlowDialog
from PySide2.QtWidgets import QDialog
from constants import *

class CustomAddFlowDialog(Ui_AddFlowDialog, QDialog):
    def __init__(self, node) -> None:
        QDialog.__init__(self)
        self.setupUi(self)
        self.node = node
        print(node)
        self.data_inport.addItems(node.get_terminate_id())
        self.data_outport.addItems(node.get_terminate_id())
        self.btn_add_flow.clicked.connect(self.fn_add_flow)
        self.btn_close.clicked.connect(self.fn_close)
    
    def fn_add_flow(self):
        global odl_ip
        global odl_port
        global odl_user
        global odl_password

        if( not str(self.data_flow_id.text()) or not str(self.data_priority.text())):
            self.message.setText("Missing data")
        else:
            if(self.node.add_flow(odl_ip, odl_port, odl_user, odl_password, self.data_flow_id.text(), self.data_inport.currentText(), self.data_outport.currentText(), self.data_priority.text())):
                self.message.setText("Success add flow!")
            else:
                self.message.setText("Program error!")

    def fn_close(self):
        self.close()