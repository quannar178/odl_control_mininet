# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_flow_windowYWbZaz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AddFlowWindow(object):
    def setupUi(self, AddFlowWindow):
        if not AddFlowWindow.objectName():
            AddFlowWindow.setObjectName(u"AddFlowWindow")
        AddFlowWindow.resize(561, 370)
        self.centralwidget = QWidget(AddFlowWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.formLayout = QFormLayout(self.tab)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.data_flow_id = QLineEdit(self.tab)
        self.data_flow_id.setObjectName(u"data_flow_id")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.data_flow_id)

        self.data_priority = QLineEdit(self.tab)
        self.data_priority.setObjectName(u"data_priority")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.data_priority)

        self.data_inport = QComboBox(self.tab)
        self.data_inport.setObjectName(u"data_inport")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.data_inport)

        self.data_outport = QComboBox(self.tab)
        self.data_outport.setObjectName(u"data_outport")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.data_outport)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.message = QLabel(self.centralwidget)
        self.message.setObjectName(u"message")

        self.verticalLayout.addWidget(self.message)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_cancel = QPushButton(self.centralwidget)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout_2.addWidget(self.btn_cancel)

        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")

        self.horizontalLayout_2.addWidget(self.btn_add)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        AddFlowWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AddFlowWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 561, 20))
        AddFlowWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AddFlowWindow)
        self.statusbar.setObjectName(u"statusbar")
        AddFlowWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddFlowWindow)

        QMetaObject.connectSlotsByName(AddFlowWindow)
    # setupUi

    def retranslateUi(self, AddFlowWindow):
        AddFlowWindow.setWindowTitle(QCoreApplication.translate("AddFlowWindow", u"Add Flow", None))
        self.label.setText(QCoreApplication.translate("AddFlowWindow", u"Flow ID", None))
        self.label_3.setText(QCoreApplication.translate("AddFlowWindow", u"Inport", None))
        self.label_4.setText(QCoreApplication.translate("AddFlowWindow", u"Outport", None))
        self.label_5.setText(QCoreApplication.translate("AddFlowWindow", u"Priority", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("AddFlowWindow", u"Port", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("AddFlowWindow", u"Tab 2", None))
        self.message.setText("")
        self.btn_cancel.setText(QCoreApplication.translate("AddFlowWindow", u"Cancel", None))
        self.btn_add.setText(QCoreApplication.translate("AddFlowWindow", u"Add", None))
    # retranslateUi

