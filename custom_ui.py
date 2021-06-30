from logging import info, log
from NodeClass import NodeClass
from PySide2.QtWidgets  import QApplication, QMainWindow
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_main_ui import Ui_MainWindow
from constants import *
from utils import *
from custom_dialog import MyDiaLog
from custom_add_flow_dialog import CustomAddFlowDialog
from custom_flow_table import CustomViewFlowTable

class CusTom_MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.btn_check_info.clicked.connect(self.fn_check_info)
        self.btn_get_topo.clicked.connect(self.fn_show_topo)
        self.edt_host_addr.setText('192.168.56.4')
        self.edt_port_number.setText('8181')
        self.edt_user_name.setText('admin')
        self.edt_password.setText('admin')
        self.net = []
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.cb_node.currentIndexChanged.connect(self.fn_change_cb_flow_id)
        self.btn_delete_all_flow.clicked.connect(self.fn_del_all_flow)
        self.btn_add_flow.clicked.connect(self.fn_add_flow)
        self.btn_del_flow_id.clicked.connect(self.fn_del_flow_id)
        self.btn_del_flow_id.setEnabled(False)
        self.btn_view_flow.clicked.connect(self.fn_view_flow)

    def fn_check_info(self):
        global odl_ip
        global odl_port
        global odl_user
        global odl_password

        odl_ip = self.edt_host_addr.text()
        odl_port = self.edt_port_number.text()
        odl_user = self.edt_user_name.text()
        odl_password = self.edt_password.text()

        logging.info("odl_ip %s" %odl_ip)
        logging.info("odl_port %s" %odl_port)
        logging.info("odl_user %s" %odl_ip)
        logging.info("odl_password %s" %odl_password)

        if(is_server_open(odl_ip, odl_port)):
            if(is_auth(auth_uri, odl_ip, odl_port, odl_user, odl_password)):
                self.label_info.setText('<p style="color:rgb(0, 204, 0);">Information is correct!</p>')
            else:
                self.label_info.setText("Host address or port number is open! \n User name or password is NOT correct")
        else:
            self.label_info.setText('Host address or port number is NOT open!')

    def fn_show_topo(self):
        _, my_topology = get_url(get_topo_uri, odl_ip, odl_port, odl_user, odl_password)
        my_topology = node_structure(my_topology)
        self.edt_topo.setReadOnly(True)
        self.edt_topo.setText(json.dumps(my_topology, indent=2,))
        self.message.setHidden(True)

        # construct net
        self.net.clear()
        self.cb_node.clear()
        self.cb_flow_id.clear()
        self.cb_node.addItem("Choose node:")
        for node in my_topology:
            port_id = []
            for port in node["port"]:
                port_id.append(str(port).split(":")[2])
            self.net.append(NodeClass(node["node_id"], port_id))
            self.cb_node.addItem(node["node_id"])
        for node in self.net:
            logging.info("%s" %node)
        self.cb_flow_id.addItem("Choose flow id:")
        self.cb_node.model().item(0).setEnabled(False)
        self.cb_flow_id.model().item(0).setEnabled(False)
    
    def fn_change_cb_flow_id(self):
        logging.info("Update flow id")
        for node in self.net:
            if(self.cb_node.currentText() == node.get_node_id()):
                if(len(node.get_flow()) == 0):
                    self.cb_flow_id.clear()
                    self.cb_flow_id.addItem("No flow")
                    
                    self.cb_flow_id.model().item(0).setEnabled(False)
                    self.btn_del_flow_id.setEnabled(False)
                else:
                    self.cb_flow_id.clear()
                    self.cb_flow_id.addItem("Choose flow id:")
                    self.cb_flow_id.addItems(node.get_flow())
                    self.cb_flow_id.model().item(0).setEnabled(False)
                    self.btn_del_flow_id.setEnabled(True)
                break
    def fn_del_all_flow(self):
        print(self.cb_node.currentIndex())
        if(self.cb_node.currentIndex() == 0):
            self.message.setText("You must choose node!")
            self.message.setHidden(False)
            return
        global odl_ip
        global odl_port
        global odl_user
        global odl_password
        self.message.setHidden(True)
        for node in self.net:
            if(self.cb_node.currentText() == node.get_node_id()):
                logging.info("Delete all flow %s" %node.get_node_id())
                is_success = node.delete_table(odl_ip, odl_port, odl_user, odl_password)
                if(is_success):
                    dialog = MyDiaLog(1,"Sucess")
                else:
                    dialog = MyDiaLog(0, "Error")
                dialog.exec_()
                break

        self.fn_change_cb_flow_id()

    def fn_add_flow(self):
        if(self.cb_node.currentIndex() == 0):
            self.message.setText("You must choose node!")
            self.message.setHidden(False)
            return
        self.message.setHidden(True)
        for node in self.net:
            if(self.cb_node.currentText() == node.get_node_id()):
                dialog = CustomAddFlowDialog(node)
                dialog.exec_()
                break
        self.fn_change_cb_flow_id()

    def fn_del_flow_id(self):
        self.message.setHidden(True)
        id_flow = json.loads(self.cb_flow_id.currentText())["id"]
        for node in self.net:
            if(self.cb_node.currentText() == node.get_node_id()):
                logging.info("Delete flow %s" %id_flow)
                is_success = node.delete_flow(id_flow, odl_ip, odl_port, odl_user, odl_password)
                if(is_success):
                    dialog = MyDiaLog(1,"Sucess")
                else:
                    dialog = MyDiaLog(0, "Error")
                dialog.exec_()
                break
        self.fn_change_cb_flow_id()

    def fn_view_flow(self):
        self.message.setHidden(True)
        dialog = CustomViewFlowTable(self.net)
        dialog.exec_()
