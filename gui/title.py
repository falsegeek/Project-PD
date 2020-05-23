from PyQt5 import QtCore, QtGui, QtWidgets

from menu import Ui_menu


class Ui_title(object):
    def setupUi(self, title):
        title.setObjectName("title")
        title.resize(375, 243)
        title.setMinimumSize(QtCore.QSize(375, 0))
        title.setMaximumSize(QtCore.QSize(375, 279))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        title.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(title)
        self.centralwidget.setObjectName("centralwidget")
        self.h1 = QtWidgets.QLabel(self.centralwidget)
        self.h1.setGeometry(QtCore.QRect(40, 10, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.h1.setFont(font)
        self.h1.setObjectName("h1")
        self.description = QtWidgets.QTextBrowser(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(20, 60, 331, 131))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.description.setFont(font)
        self.description.setObjectName("description")
        self.push_start = QtWidgets.QPushButton(self.centralwidget) # переход на старинцу с выбором формата
        self.push_start.setGeometry(QtCore.QRect(140, 200, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_start.setFont(font)
        self.push_start.setObjectName("push_start")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 381, 271))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/Cryptography-512.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.h1.raise_()
        self.description.raise_()
        self.push_start.raise_()
        title.setCentralWidget(self.centralwidget)


        self.retranslateUi(title)
        QtCore.QMetaObject.connectSlotsByName(title)
        self.push_start.clicked.connect(self.menu) # переход на старинцу с выбором формата

    def menu(self):    # переход на старинцу с выбором формата
        self.menu = QtWidgets.QWidget()
        self.ui = Ui_menu()
        self.ui.setupUi(self.menu)
        self.menu.show()

    def retranslateUi(self, title):
        _translate = QtCore.QCoreApplication.translate
        title.setWindowTitle(_translate("title", "Приложение шифрования"))
        self.h1.setText(_translate("title", "Приложение шифрования "))
        self.description.setHtml(_translate("title", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">      Данная программа позволяет шифровать текст в один из предложенных форматов файлов, с последующей расшифровкой.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">      Список поддерживаем форматов:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">           - Word;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">           - bmp;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">           - jpg;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">           - wav;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">           - txt.</span></p></body></html>"))
        self.push_start.setText(_translate("title", "Начать"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    title = QtWidgets.QMainWindow()
    ui = Ui_title()
    ui.setupUi(title)
    title.show()
    sys.exit(app.exec_())
