from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog


class Ui_txt_screen(object):
    def setupUi(self, txt_screen):
        txt_screen.setObjectName("txt_screen")
        txt_screen.resize(416, 257)
        self.groupBox_2 = QtWidgets.QGroupBox(txt_screen)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 130, 391, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 301, 16))
        self.label_3.setObjectName("label_3")
        self.push_enc = QtWidgets.QPushButton(self.groupBox_2)
        self.push_enc.setGeometry(QtCore.QRect(10, 40, 75, 23))
        self.push_enc.setObjectName("push_enc")
        self.start_enc = QtWidgets.QPushButton(self.groupBox_2)
        self.start_enc.setGeometry(QtCore.QRect(160, 70, 75, 23))
        self.start_enc.setObjectName("start_enc")
        self.groupBox_3 = QtWidgets.QGroupBox(txt_screen)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 391, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 301, 16))
        self.label_4.setObjectName("label_4")
        self.push_cript = QtWidgets.QPushButton(self.groupBox_3)
        self.push_cript.setGeometry(QtCore.QRect(10, 40, 75, 23))
        self.push_cript.setObjectName("push_cript")
        self.start_cript = QtWidgets.QPushButton(self.groupBox_3)
        self.start_cript.setGeometry(QtCore.QRect(160, 70, 75, 23))
        self.start_cript.setObjectName("start_cript")

        self.retranslateUi(txt_screen)
        QtCore.QMetaObject.connectSlotsByName(txt_screen)
        self.push_cript.clicked.connect(self.file_browser)
        self.push_enc.clicked.connect(self.file_browser)

    def file_browser(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)

        with open(path, "r") as f:
            print(f.readline())

    def retranslateUi(self, txt_screen):
        _translate = QtCore.QCoreApplication.translate
        txt_screen.setWindowTitle(_translate("txt_screen", "Приложение шифрования TXT"))
        self.groupBox_2.setTitle(_translate("txt_screen", "Расшифровать"))
        self.label_3.setText(_translate("txt_screen", "1. Выберите файл для расшифровки"))
        self.push_enc.setText(_translate("txt_screen", "Файл"))
        self.start_enc.setText(_translate("txt_screen", "Начать"))
        self.groupBox_3.setTitle(_translate("txt_screen", "Зашифровать"))
        self.label_4.setText(_translate("txt_screen", "1. Выберите данные для шифрования в формате \"txt\""))
        self.push_cript.setText(_translate("txt_screen", "Файл"))
        self.start_cript.setText(_translate("txt_screen", "Начать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    txt_screen = QtWidgets.QWidget()
    ui = Ui_txt_screen()
    ui.setupUi(txt_screen)
    txt_screen.show()
    sys.exit(app.exec_())