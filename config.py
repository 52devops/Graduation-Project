# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!
import pickle
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_config_ui(object):
    def setupUi(self, config_ui):
        config_ui.setObjectName("config_ui")
        config_ui.resize(735, 475)
        config_ui.setStyleSheet("#config_ui {border-image: url(:/we/welcome.jpg);}")
        self.ui = config_ui
        self.buttonBox = QtWidgets.QDialogButtonBox(config_ui)
        self.buttonBox.setGeometry(QtCore.QRect(380, 430, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(config_ui)
        self.widget.setGeometry(QtCore.QRect(120, 120, 451, 270))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(2)
        self.formLayout.setVerticalSpacing(30)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(20, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.widget)
        config_ui.setWindowFlags(Qt.FramelessWindowHint)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setEchoMode(QLineEdit.Password)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.widget1 = QtWidgets.QWidget(config_ui)
        self.widget1.setGeometry(QtCore.QRect(640, -10, 101, 31))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.config_min = QtWidgets.QPushButton(self.widget1)
        self.config_min.setStyleSheet("#config_min {border-image: url(:/we/min.png);}")
        self.config_min.setText("")
        self.config_min.setObjectName("config_min")
        self.horizontalLayout.addWidget(self.config_min)
        self.config_close = QtWidgets.QPushButton(self.widget1)
        self.config_close.setStyleSheet("#config_close {border-image: url(:/we/close.png);}")
        self.config_close.setText("")
        self.config_close.setObjectName("config_close")
        self.horizontalLayout.addWidget(self.config_close)

        self.retranslateUi(config_ui)
        self.buttonBox.accepted.connect(self.save)
        self.buttonBox.rejected.connect(self.quit)
        self.config_close.clicked.connect(config_ui.close)
        self.config_min.clicked.connect(config_ui.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(config_ui)

    def save(self):
        data = {}
        data = {'mail':self.lineEdit.text(),
                'db_add':self.lineEdit_2.text(),
                'db_user':self.lineEdit_3.text(),
                'db_pass':self.lineEdit_4.text()}
        # print(len(data))
        # print(data.values())
        if '' in data.values():
            QMessageBox.warning(self.ui,'Warning','请输入正确的格式')
        else:
            pro = pickle.dumps(data)
            f = open('config.txt','wb')
            f.write(pro)
            f.close()
            self.ui.close()

    def quit(self):
        self.ui.close()





    def retranslateUi(self, config_ui):
        _translate = QtCore.QCoreApplication.translate
        config_ui.setWindowTitle(_translate("config_ui", "Dialog"))
        self.label_2.setText(_translate("config_ui", "数据库地址:"))
        self.label_3.setText(_translate("config_ui", "数据库账号："))
        self.label_4.setText(_translate("config_ui", "数据库密码："))
        self.label.setText(_translate("config_ui", "报警邮箱："))


from 毕设.毕设.My_class.Mainwin import *

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    bbb = Mainwin()
    ccc = Ui_config_ui()
    ccc.setupUi(bbb)
    bbb.show()
    app.exec_()