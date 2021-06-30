from ui_flow_table_dialog import Ui_FlowTable
from PySide2.QtWidgets import QDialog

class CustomViewFlowTable(QDialog, Ui_FlowTable):
    def __init__(self, nodes) -> None:
        QDialog.__init__(self)
        self.setupUi(self)
        for node in nodes:
            self.textEdit.append("Node: %s :\n"%node.get_node_id())
            flows = node.get_flow()
            if(len(flows) == 0):
                self.textEdit.append("\t 0 flow\n")
            else:
                for flow in flows:
                    self.textEdit.append("\t%s\n"%flow)