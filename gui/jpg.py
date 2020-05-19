from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog


class Ui_jpg_screen(object):
    def setupUi(self, jpg_screen):
        jpg_screen.setObjectName("jpg_screen")
        jpg_screen.resize(415, 303)
        self.groupBox_2 = QtWidgets.QGroupBox(jpg_screen)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 180, 391, 111))
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
        self.groupBox = QtWidgets.QGroupBox(jpg_screen)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 391, 161))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 301, 16))
        self.label.setObjectName("label")
        self.push_cript = QtWidgets.QPushButton(self.groupBox)
        self.push_cript.setGeometry(QtCore.QRect(10, 40, 75, 23))
        self.push_cript.setObjectName("push_cript")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 301, 16))
        self.label_2.setObjectName("label_2")
        self.radio_1 = QtWidgets.QRadioButton(self.groupBox)
        self.radio_1.setGeometry(QtCore.QRect(10, 100, 31, 17))
        self.radio_1.setObjectName("radio_1")
        self.radio_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radio_2.setGeometry(QtCore.QRect(40, 100, 31, 17))
        self.radio_2.setObjectName("radio_2")
        self.radio_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radio_4.setGeometry(QtCore.QRect(70, 100, 31, 17))
        self.radio_4.setObjectName("radio_4")
        self.radio_8 = QtWidgets.QRadioButton(self.groupBox)
        self.radio_8.setGeometry(QtCore.QRect(100, 100, 31, 17))
        self.radio_8.setObjectName("radio_8")
        self.start_cript = QtWidgets.QPushButton(self.groupBox)
        self.start_cript.setGeometry(QtCore.QRect(160, 120, 75, 23))
        self.start_cript.setObjectName("start_cript")

        self.retranslateUi(jpg_screen)
        QtCore.QMetaObject.connectSlotsByName(jpg_screen)
        self.push_cript.clicked.connect(self.file_browser)
        self.push_enc.clicked.connect(self.file_browser)

    def file_browser(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)

        with open(path, "r") as f:
            print(f.readline())

    def retranslateUi(self, jpg_screen):
        _translate = QtCore.QCoreApplication.translate
        jpg_screen.setWindowTitle(_translate("jpg_screen", "Приложение шифрования JPG"))
        self.groupBox_2.setTitle(_translate("jpg_screen", "Расшифровать"))
        self.label_3.setText(_translate("jpg_screen", "1. Выберите файл для расшифровки"))
        self.push_enc.setText(_translate("jpg_screen", "Файл"))
        self.start_enc.setText(_translate("jpg_screen", "Начать"))
        self.groupBox.setTitle(_translate("jpg_screen", "Зашифровать"))
        self.label.setText(_translate("jpg_screen", "1. Выберите данные для шифрования в формате \"txt\""))
        self.push_cript.setText(_translate("jpg_screen", "Файл"))
        self.label_2.setText(_translate("jpg_screen", "2. Выберите степень сжатия"))
        self.radio_1.setText(_translate("jpg_screen", "1"))
        self.radio_2.setText(_translate("jpg_screen", "2"))
        self.radio_4.setText(_translate("jpg_screen", "4"))
        self.radio_8.setText(_translate("jpg_screen", "8"))
        self.start_cript.setText(_translate("jpg_screen", "Начать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jpg_screen = QtWidgets.QWidget()
    ui = Ui_jpg_screen()
    ui.setupUi(jpg_screen)
    jpg_screen.show()
    sys.exit(app.exec_())
