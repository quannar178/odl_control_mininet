# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_flow_dialogcANnyx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AddFlowDialog(object):
    def setupUi(self, AddFlowDialog):
        if not AddFlowDialog.objectName():
            AddFlowDialog.setObjectName(u"AddFlowDialog")
        AddFlowDialog.resize(800, 600)
        AddFlowDialog.setMinimumSize(QSize(400, 300))
        self.verticalLayout = QVBoxLayout(AddFlowDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(AddFlowDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.formLayout_2 = QFormLayout(self.tab)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.data_inport = QComboBox(self.tab)
        self.data_inport.setObjectName(u"data_inport")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.data_inport)

        self.data_outport = QComboBox(self.tab)
        self.data_outport.setObjectName(u"data_outport")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.data_outport)

        self.data_flow_id = QLineEdit(self.tab)
        self.data_flow_id.setObjectName(u"data_flow_id")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.data_flow_id)

        self.data_priority = QLineEdit(self.tab)
        self.data_priority.setObjectName(u"data_priority")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.data_priority)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.message = QLabel(AddFlowDialog)
        self.message.setObjectName(u"message")

        self.verticalLayout.addWidget(self.message)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_close = QPushButton(AddFlowDialog)
        self.btn_close.setObjectName(u"btn_close")

        self.horizontalLayout.addWidget(self.btn_close)

        self.btn_add_flow = QPushButton(AddFlowDialog)
        self.btn_add_flow.setObjectName(u"btn_add_flow")

        self.horizontalLayout.addWidget(self.btn_add_flow)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(AddFlowDialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AddFlowDialog)
    # setupUi

    def retranslateUi(self, AddFlowDialog):
        AddFlowDialog.setWindowTitle(QCoreApplication.translate("AddFlowDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("AddFlowDialog", u"flow_id", None))
        self.label_2.setText(QCoreApplication.translate("AddFlowDialog", u"inport", None))
        self.label_3.setText(QCoreApplication.translate("AddFlowDialog", u"outport", None))
        self.label_4.setText(QCoreApplication.translate("AddFlowDialog", u"priority", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("AddFlowDialog", u"Port", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("AddFlowDialog", u"Tab 2", None))
        self.message.setText("")
        self.btn_close.setText(QCoreApplication.translate("AddFlowDialog", u"Close", None))
        self.btn_add_flow.setText(QCoreApplication.translate("AddFlowDialog", u"Add flow", None))
    # retranslateUi

