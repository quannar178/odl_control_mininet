# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_uiRirIVT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 640)
        MainWindow.setMinimumSize(QSize(800, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_login = QWidget()
        self.tab_login.setObjectName(u"tab_login")
        self.formLayout = QFormLayout(self.tab_login)
        self.formLayout.setObjectName(u"formLayout")
        self.groupBox = QGroupBox(self.tab_login)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.edt_host_addr = QLineEdit(self.groupBox)
        self.edt_host_addr.setObjectName(u"edt_host_addr")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.edt_host_addr)

        self.edt_port_number = QLineEdit(self.groupBox)
        self.edt_port_number.setObjectName(u"edt_port_number")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.edt_port_number)

        self.edt_user_name = QLineEdit(self.groupBox)
        self.edt_user_name.setObjectName(u"edt_user_name")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.edt_user_name)

        self.edt_password = QLineEdit(self.groupBox)
        self.edt_password.setObjectName(u"edt_password")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.edt_password)


        self.horizontalLayout_6.addLayout(self.formLayout_2)


        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(3, QFormLayout.FieldRole, self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_check_info = QPushButton(self.tab_login)
        self.btn_check_info.setObjectName(u"btn_check_info")

        self.horizontalLayout.addWidget(self.btn_check_info)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_info = QLabel(self.tab_login)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setStyleSheet(u"color: rgb(255, 0, 0)")
        self.label_info.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_info)

        self.tabWidget.addTab(self.tab_login, "")
        self.tab_get_topo = QWidget()
        self.tab_get_topo.setObjectName(u"tab_get_topo")
        self.verticalLayout_6 = QVBoxLayout(self.tab_get_topo)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.edt_topo = QTextEdit(self.tab_get_topo)
        self.edt_topo.setObjectName(u"edt_topo")
        self.edt_topo.setEnabled(True)
        self.edt_topo.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.edt_topo)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.btn_get_topo = QPushButton(self.tab_get_topo)
        self.btn_get_topo.setObjectName(u"btn_get_topo")

        self.horizontalLayout_3.addWidget(self.btn_get_topo)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tab_get_topo, "")
        self.tab_control = QWidget()
        self.tab_control.setObjectName(u"tab_control")
        self.verticalLayout = QVBoxLayout(self.tab_control)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.message = QLabel(self.tab_control)
        self.message.setObjectName(u"message")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)
        self.message.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 12pt \"Sans Serif\";")
        self.message.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.message)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.cb_node = QComboBox(self.tab_control)
        self.cb_node.setObjectName(u"cb_node")

        self.verticalLayout.addWidget(self.cb_node)

        self.btn_view_flow = QPushButton(self.tab_control)
        self.btn_view_flow.setObjectName(u"btn_view_flow")

        self.verticalLayout.addWidget(self.btn_view_flow)

        self.btn_add_flow = QPushButton(self.tab_control)
        self.btn_add_flow.setObjectName(u"btn_add_flow")

        self.verticalLayout.addWidget(self.btn_add_flow)

        self.btn_delete_all_flow = QPushButton(self.tab_control)
        self.btn_delete_all_flow.setObjectName(u"btn_delete_all_flow")

        self.verticalLayout.addWidget(self.btn_delete_all_flow)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.cb_flow_id = QComboBox(self.tab_control)
        self.cb_flow_id.setObjectName(u"cb_flow_id")

        self.horizontalLayout_4.addWidget(self.cb_flow_id)

        self.btn_del_flow_id = QPushButton(self.tab_control)
        self.btn_del_flow_id.setObjectName(u"btn_del_flow_id")

        self.horizontalLayout_4.addWidget(self.btn_del_flow_id)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.tabWidget.addTab(self.tab_control, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Control Net", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Info", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Host address", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Port number", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.btn_check_info.setText(QCoreApplication.translate("MainWindow", u"Check Info", None))
        self.label_info.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_login), QCoreApplication.translate("MainWindow", u"Login", None))
        self.btn_get_topo.setText(QCoreApplication.translate("MainWindow", u"Update Topology", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_get_topo), QCoreApplication.translate("MainWindow", u"Get Topo", None))
        self.message.setText(QCoreApplication.translate("MainWindow", u"You must get topology first!", None))
        self.btn_view_flow.setText(QCoreApplication.translate("MainWindow", u"View all flow", None))
        self.btn_add_flow.setText(QCoreApplication.translate("MainWindow", u"Add flow", None))
        self.btn_delete_all_flow.setText(QCoreApplication.translate("MainWindow", u"Delete all flow", None))
        self.btn_del_flow_id.setText(QCoreApplication.translate("MainWindow", u"Delete specific", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_control), QCoreApplication.translate("MainWindow", u"Control Flow", None))
    # retranslateUi

