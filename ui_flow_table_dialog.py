# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'flow_table_dialogHTvowX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FlowTable(object):
    def setupUi(self, FlowTable):
        if not FlowTable.objectName():
            FlowTable.setObjectName(u"FlowTable")
        FlowTable.resize(800, 600)
        self.verticalLayout = QVBoxLayout(FlowTable)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(FlowTable)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.buttonBox = QDialogButtonBox(FlowTable)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(FlowTable)
        self.buttonBox.accepted.connect(FlowTable.accept)
        self.buttonBox.rejected.connect(FlowTable.reject)

        QMetaObject.connectSlotsByName(FlowTable)
    # setupUi

    def retranslateUi(self, FlowTable):
        FlowTable.setWindowTitle(QCoreApplication.translate("FlowTable", u"View Flow", None))
    # retranslateUi

