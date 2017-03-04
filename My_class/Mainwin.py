from PyQt5.QtCore import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class Mainwin(QMainWindow):
    def __init__(self,parent=None):
        super(Mainwin,self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self,QEvent(174))
            event.accept()


    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

class My_dia(QDialog):
    def __init__(self,parent=None):
        super(My_dia,self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)

        def mousePressEvent(self, event):
            if event.button() == Qt.LeftButton:
                self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
                QApplication.postEvent(self, QEvent(174))
                event.accept()

        def mouseMoveEvent(self, event):
            if event.buttons() == Qt.LeftButton:
                self.move(event.globalPos() - self.dragPosition)
                event.accept()
