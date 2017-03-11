# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from 毕设.毕设.config import *
from 毕设.毕设.Icon import icon
from 毕设.毕设.Readme import Ui_Readme
from 毕设.毕设.Opera_DB import My_DB
from 毕设.毕设.ProgressBar import ProgressBar
import re
import pickle
class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        self.ui = mainwindow
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(939, 584)
        mainwindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        mainwindow.setStyleSheet("#mainwindow {border-image: url(:/we/welcome.jpg);}")
        self.BBB = QtWidgets.QWidget(mainwindow)
        self.BBB.setStyleSheet("#BBB {border-image: url(:/we/welcome.jpg);}")
        self.BBB.setObjectName("BBB")
        self.ReadMe = QtWidgets.QPushButton(self.BBB)
        self.ReadMe.setGeometry(QtCore.QRect(0, 480, 111, 41))
        self.ReadMe.setObjectName("ReadMe")
        self.Upload = QtWidgets.QPushButton(self.BBB)
        self.Upload.setGeometry(QtCore.QRect(700, 480, 111, 41))
        self.Upload.setObjectName("Upload")
        self.Config = QtWidgets.QPushButton(self.BBB)
        self.Config.setGeometry(QtCore.QRect(120, 480, 111, 41))
        self.Config.setObjectName("Config")
        self.Start = QtWidgets.QPushButton(self.BBB)
        self.Start.setGeometry(QtCore.QRect(820, 480, 111, 41))
        self.Start.setObjectName("Start")
        self.author = QtWidgets.QLabel(self.BBB)
        self.author.setGeometry(QtCore.QRect(400, 480, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.author.setFont(font)
        self.author.setObjectName("author")
        self.ui_exit = QtWidgets.QPushButton(self.BBB)
        self.ui_exit.setGeometry(QtCore.QRect(890, 0, 51, 21))
        self.ui_exit.setStyleSheet("#ui_exit {border-image: url(:/we/close.png);}")
        self.ui_exit.setText("")
        self.ui_exit.setFlat(False)
        self.ui_exit.setObjectName("ui_exit")
        self.ui_hit = QtWidgets.QPushButton(self.BBB)
        self.ui_hit.setGeometry(QtCore.QRect(840, 0, 51, 21))
        self.ui_hit.setStyleSheet("#ui_hit {border-image: url(:/we/min.png);}")
        self.ui_hit.setText("")
        self.ui_hit.setObjectName("ui_hit")
        self.Welcome_tite = QtWidgets.QLabel(self.BBB)
        self.Welcome_tite.setGeometry(QtCore.QRect(235, 1, 480, 52))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Welcome_tite.setFont(font)
        self.Welcome_tite.setObjectName("Welcome_tite")
        self.ReadMe.raise_()
        self.Upload.raise_()
        self.Config.raise_()
        self.Start.raise_()
        self.ui_hit.raise_()
        self.ui_exit.raise_()
        self.Welcome_tite.raise_()
        self.author.raise_()
        mainwindow.setCentralWidget(self.BBB)
        self.menubar = QtWidgets.QMenuBar(mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 939, 26))
        self.menubar.setObjectName("menubar")
        mainwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainwindow)
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainwindow)
        self.ui_exit.clicked.connect(mainwindow.close)
        self.Config.clicked.connect(self.config)
        self.ui_hit.clicked.connect(mainwindow.showMinimized)
        self.ReadMe.clicked.connect(self.readme)
        self.Upload.clicked.connect(self.upload)
        self.Start.clicked.connect(self.start)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)
        self.LoadData()
        # mainwindow.set

    def LoadData(self):
        try:
            f = open('config.txt', 'rb')
            data = pickle.loads(f.read())
            if '' in data.values():
                raise
            else:
                self.data = data
        except:
            QMessageBox.warning(self.ui, 'Warning', '请检查相关配置是否完整')

    def config(self):
        sec = My_dia()
        config = Ui_config_ui()
        config.setupUi(sec)
        sec.exec_()

    def readme(self):
        third = My_dia()
        Readme = Ui_Readme()
        Readme.setupUi(third)
        third.exec_()

    def upload(self):
        files, ok1 = QFileDialog.getOpenFileNames(self.ui,
                                                  "多文件选择",
                                                  "C:/",
                                                  "All Files (*)")
        db = My_DB()
        for i in files:
            filename = re.sub(".*/","",i)
            path = i
            db.push(filename,path)

    def start(self):
        fourth = My_dia()
        Start = ProgressBar(fourth)
        fourth.exec_()

        #     print('')
        # fourth.exec_()

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "MainWindow"))
        self.ReadMe.setText(_translate("mainwindow", "使用说明"))
        self.Upload.setText(_translate("mainwindow", "上传匹配数据"))
        self.Config.setText(_translate("mainwindow", "配置"))
        self.Start.setText(_translate("mainwindow", "开始"))
        self.author.setText(_translate("mainwindow", "Author_By：王耀华"))
        self.Welcome_tite.setText(_translate("mainwindow", "欢迎使用智能安防系统"))


from 毕设.毕设.My_class.Mainwin import *

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    bbb = Mainwin()
    ccc = Ui_mainwindow()
    ccc.setupUi(bbb)
    bbb.show()
    app.exec_()
