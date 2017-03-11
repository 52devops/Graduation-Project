from PyQt5.QtWidgets import QApplication, QProgressBar, QPushButton
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QBasicTimer
import sys

class ProgressBar(QtWidgets.QWidget):
    def __init__(self,ddd):
        QtWidgets.QWidget.__init__(self)
        self.resize(100, 100)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('获取远端数据')
        self.pbar = QProgressBar(ddd)
        self.pbar.setGeometry(20, 30, 250, 25)

        self.button = QPushButton('获取数据', ddd)
        self.button.setFocusPolicy(Qt.NoFocus)
        self.button.move(20, 100)
        self.button1 = QPushButton('退出', ddd)
        self.button1.setFocusPolicy(Qt.NoFocus)
        self.button1.move(130, 100)

        self.button.clicked.connect(self.onStart)
        self.button1.clicked.connect(self.toExit)
        self.timer = QBasicTimer()
        self.step = 0

    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            return
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def onStart(self):
        self.timer.start(100, self)
        # if self.timer.isActive():
        #     self.timer.stop()
        #     self.button.setText('Start')
        # else:
        #     self.timer.start(100, self)
            # self.button.setText('Exit')
    def toExit(self):
        pass
    def Bhow(xxx):
        app = QApplication(sys.argv)
        qb = ProgressBar()
        qb.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    qb = ProgressBar()
    qb.show()
    sys.exit(app.exec_())