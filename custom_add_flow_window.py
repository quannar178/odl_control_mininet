from ui_add_flow_window import Ui_AddFlowWindow
from PySide2.QtWidgets  import QMainWindow

class CustomAddFlowWindow(QMainWindow, Ui_AddFlowWindow):
    def __init__(self, node, title) -> None:
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.node = node
        self.data_inport.addItems(node.get_terminate_id())
        self.data_outport.addItems(node.get_terminate_id())
        self.btn_add.clicked.connect(self.fn_add_flow)

    def fn_add_flow(self):
        global odl_ip
        global odl_port
        global odl_user
        global odl_password
        if( not str(self.data_flow_id.text()) or not str(self.data_priority.text())):
            self.message.setText("Missing data")
        # self.node.add_flow(odl_ip, odl_port, odl_user, odl_password, )