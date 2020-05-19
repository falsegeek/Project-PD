from PyQt5 import QtCore, QtGui, QtWidgets

from word import Ui_word_screen
from bmp import Ui_bmp_screen
from txt import Ui_txt_screen
from jpg import Ui_jpg_screen
from wav import Ui_wav_screen


class Ui_menu(object):
    def setupUi(self, menu):
        menu.setObjectName("menu")
        menu.resize(412, 200)
        self.label = QtWidgets.QLabel(menu)
        self.label.setGeometry(QtCore.QRect(40, 10, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.push_Word = QtWidgets.QPushButton(menu)
        self.push_Word.setGeometry(QtCore.QRect(60, 80, 75, 23))
        self.push_Word.setObjectName("push_Word")
        self.push_jpg = QtWidgets.QPushButton(menu)
        self.push_jpg.setGeometry(QtCore.QRect(110, 130, 75, 23))
        self.push_jpg.setObjectName("push_jpg")
        self.push_bmp = QtWidgets.QPushButton(menu)
        self.push_bmp.setGeometry(QtCore.QRect(220, 130, 75, 23))
        self.push_bmp.setObjectName("push_bmp")
        self.push_txt = QtWidgets.QPushButton(menu)
        self.push_txt.setGeometry(QtCore.QRect(170, 80, 75, 23))
        self.push_txt.setObjectName("push_txt")
        self.push_wav = QtWidgets.QPushButton(menu)
        self.push_wav.setGeometry(QtCore.QRect(280, 80, 75, 23))
        self.push_wav.setObjectName("push_wav")
        self.groupBox = QtWidgets.QGroupBox(menu)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 371, 171))
        self.groupBox.setObjectName("groupBox")
        self.groupBox.raise_()
        self.label.raise_()
        self.push_Word.raise_()
        self.push_jpg.raise_()
        self.push_bmp.raise_()
        self.push_txt.raise_()
        self.push_wav.raise_()

        self.retranslateUi(menu)
        QtCore.QMetaObject.connectSlotsByName(menu)
        self.push_Word.clicked.connect(self.word_screen)
        self.push_txt.clicked.connect(self.txt_screen)
        self.push_bmp.clicked.connect(self.bmp_screen)
        self.push_jpg.clicked.connect(self.jpg_screen)
        self.push_wav.clicked.connect(self.wav_screen)

    def txt_screen(self):
        self.txt_screen = QtWidgets.QWidget()
        self.ui = Ui_txt_screen()
        self.ui.setupUi(self.txt_screen)
        self.txt_screen.show()

    def word_screen(self):
        self.word_screen = QtWidgets.QWidget()
        self.ui = Ui_word_screen()
        self.ui.setupUi(self.word_screen)
        self.word_screen.show()

    def bmp_screen(self):
        self.bmp_screen = QtWidgets.QWidget()
        self.ui = Ui_bmp_screen()
        self.ui.setupUi(self.bmp_screen)
        self.bmp_screen.show()

    def jpg_screen(self):
        self.jpg_screen = QtWidgets.QWidget()
        self.ui = Ui_jpg_screen()
        self.ui.setupUi(self.jpg_screen)
        self.jpg_screen.show()

    def wav_screen(self):
        self.wav_screen = QtWidgets.QWidget()
        self.ui = Ui_wav_screen()
        self.ui.setupUi(self.wav_screen)
        self.wav_screen.show()

    def retranslateUi(self, menu):
        _translate = QtCore.QCoreApplication.translate
        menu.setWindowTitle(_translate("menu", "Приложение шифрования"))
        self.label.setText(_translate("menu", "Выберите тип шифруемого файла"))
        self.push_Word.setText(_translate("menu", "Word"))
        self.push_jpg.setText(_translate("menu", "jpg"))
        self.push_bmp.setText(_translate("menu", "bmp"))
        self.push_txt.setText(_translate("menu", "txt"))
        self.push_wav.setText(_translate("menu", "wav"))
        self.groupBox.setTitle(_translate("menu", "Зашифровать файл"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menu = QtWidgets.QWidget()
    ui = Ui_menu()
    ui.setupUi(menu)
    menu.show()
    sys.exit(app.exec_())
