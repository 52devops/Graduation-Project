# # -*- coding: utf-8 -*-
#
# # Form implementation generated from reading ui file 'ttt.ui'
# #
# # Created by: PyQt5 UI code generator 5.4.1
# #
# # WARNING! All changes made in this file will be lost!
#
# from PyQt5 import QtCore, QtGui, QtWidgets
# import sys
# class Ui_Dialog(object):
#     def setupUi(self, Dialog):
#         Dialog.setObjectName("Dialog")
#         Dialog.resize(200, 50)
#         self.pushButton = QtWidgets.QPushButton(Dialog)
#         self.pushButton.setGeometry(QtCore.QRect(40, 160, 93, 28))
#         self.pushButton.setObjectName("pushButton")
#         self.progressBar = QtWidgets.QProgressBar(Dialog)
#         self.progressBar.setGeometry(QtCore.QRect(40, 100, 271, 21))
#         self.progressBar.setProperty("value", 24)
#         self.progressBar.setObjectName("progressBar")
#
#         self.retranslateUi(Dialog)
#         QtCore.QMetaObject.connectSlotsByName(Dialog)
#
#     def retranslateUi(self, Dialog):
#         _translate = QtCore.QCoreApplication.translate
#         Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
#         self.pushButton.setText(_translate("Dialog", "PushButton"))
#
#
# from 毕设.毕设.My_class.Mainwin import *
#
# if __name__=='__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     bbb = Mainwin()
#     ccc = Ui_Dialog()
#     ccc.setupUi(bbb)
#     bbb.show()
#     app.exec_()
#
import pickle
f = open('config.txt','rb')
a = pickle.load(f)
f.close()
print(a)