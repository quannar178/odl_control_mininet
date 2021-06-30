from ui_main_ui import Ui_MainWindow
from constants import *
from PySide2.QtWidgets  import QApplication, QMainWindow
from utils import * 
class CusTom_MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.btn_check_info.clicked.connect(self.fn_check_info)
    
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

