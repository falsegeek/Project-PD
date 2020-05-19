from PyQt5 import QtCore, QtGui, QtWidgets

from menu import Ui_menu

class Ui_title(object):
    def setupUi(self, title):
        title.setObjectName("title")
        title.resize(371, 284)
        self.centralwidget = QtWidgets.QWidget(title)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 70, 331, 131))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.push_start = QtWidgets.QPushButton(self.centralwidget)
        self.push_start.setGeometry(QtCore.QRect(140, 220, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.push_start.setFont(font)
        self.push_start.setObjectName("push_start")
        title.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(title)
        self.statusbar.setObjectName("statusbar")
        title.setStatusBar(self.statusbar)

        self.retranslateUi(title)
        QtCore.QMetaObject.connectSlotsByName(title)
        self.push_start.clicked.connect(self.menu)

    def menu(self):
        self.menu = QtWidgets.QWidget()
        self.ui = Ui_menu()
        self.ui.setupUi(self.menu)
        self.menu.show()

    def retranslateUi(self, title):
        _translate = QtCore.QCoreApplication.translate
        title.setWindowTitle(_translate("title", "Приложение шифрования"))
        self.label.setText(_translate("title", "Приложение шифрования "))
        self.textBrowser.setHtml(_translate("title", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
