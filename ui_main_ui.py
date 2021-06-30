# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_uiArvxOD.ui'
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
        MainWindow.resize(600, 450)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
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
        self.btn_check_info = QPushButton(self.tab_login)
        self.btn_check_info.setObjectName(u"btn_check_info")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.btn_check_info)

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

        self.label_info = QLabel(self.tab_login)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setStyleSheet(u"color: rgb(255, 0, 0)")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_info)

        self.tabWidget.addTab(self.tab_login, "")
        self.tab_get_topo = QWidget()
        self.tab_get_topo.setObjectName(u"tab_get_topo")
        self.verticalLayout_6 = QVBoxLayout(self.tab_get_topo)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.treeView = QTreeView(self.tab_get_topo)
        self.treeView.setObjectName(u"treeView")

        self.verticalLayout_6.addWidget(self.treeView)

        self.pushButton_2 = QPushButton(self.tab_get_topo)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_6.addWidget(self.pushButton_2)

        self.tabWidget.addTab(self.tab_get_topo, "")
        self.tab_control = QWidget()
        self.tab_control.setObjectName(u"tab_control")
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
        self.btn_check_info.setText(QCoreApplication.translate("MainWindow", u"Check Info", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Info", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Host address", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Port number", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_info.setText(QCoreApplication.translate("MainWindow", u"fsfsadfa", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_login), QCoreApplication.translate("MainWindow", u"Login", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Update Topology", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_get_topo), QCoreApplication.translate("MainWindow", u"Get Topo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_control), QCoreApplication.translate("MainWindow", u"Control", None))
    # retranslateUi

