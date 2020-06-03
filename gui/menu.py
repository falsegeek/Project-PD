from PyQt5 import QtCore, QtGui, QtWidgets

from bmp import Ui_bmp_screen
from txt import Ui_txt_screen
from jpg import Ui_jpg_screen
from wav import Ui_wav_screen

class Ui_menu(object):
    def setupUi(self, menu):
        menu.setObjectName("menu")
        menu.resize(412, 197)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        menu.setWindowIcon(icon)
        self.group_choose = QtWidgets.QGroupBox(menu)
        self.group_choose.setGeometry(QtCore.QRect(20, 10, 371, 171))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.group_choose.setFont(font)
        self.group_choose.setObjectName("group_choose")
        self.push_txt = QtWidgets.QPushButton(self.group_choose)
        self.push_txt.setGeometry(QtCore.QRect(60, 40, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.push_txt.setFont(font)
        self.push_txt.setObjectName("push_txt")
        self.push_wav = QtWidgets.QPushButton(self.group_choose)
        self.push_wav.setGeometry(QtCore.QRect(230, 40, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.push_wav.setFont(font)
        self.push_wav.setObjectName("push_wav")
        self.push_bmp = QtWidgets.QPushButton(self.group_choose)
        self.push_bmp.setGeometry(QtCore.QRect(190, 100, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.push_bmp.setFont(font)
        self.push_bmp.setObjectName("push_bmp")
        self.push_jpg = QtWidgets.QPushButton(self.group_choose)
        self.push_jpg.setGeometry(QtCore.QRect(100, 100, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.push_jpg.setFont(font)
        self.push_jpg.setObjectName("push_jpg")
        self.background = QtWidgets.QLabel(menu)
        self.background.setGeometry(QtCore.QRect(10, 10, 391, 181))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("images/Header_Encryption.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.background.raise_()
        self.group_choose.raise_()

        self.retranslateUi(menu)
        QtCore.QMetaObject.connectSlotsByName(menu)
        self.push_txt.clicked.connect(self.txt_screen)  # переход на окно шифрования txt
        self.push_bmp.clicked.connect(self.bmp_screen)  # переход на окно шифрования bmp
        self.push_jpg.clicked.connect(self.jpg_screen)  # переход на окно шифрования jpg
        self.push_wav.clicked.connect(self.wav_screen)  # переход на окно шифрования wv

    def txt_screen(self):  # переход на окно шифрования txt
        self.txt_screen = QtWidgets.QWidget()
        self.ui = Ui_txt_screen()
        self.ui.setupUi(self.txt_screen)
        self.txt_screen.show()

    def bmp_screen(self):  # переход на окно шифрования bmp
        self.bmp_screen = QtWidgets.QWidget()
        self.ui = Ui_bmp_screen()
        self.ui.setupUi(self.bmp_screen)
        self.bmp_screen.show()

    def jpg_screen(self):  # переход на окно шифрования jpg
        self.jpg_screen = QtWidgets.QWidget()
        self.ui = Ui_jpg_screen()
        self.ui.setupUi(self.jpg_screen)
        self.jpg_screen.show()

    def wav_screen(self):  # переход на окно шифрования wav
        self.wav_screen = QtWidgets.QWidget()
        self.ui = Ui_wav_screen()
        self.ui.setupUi(self.wav_screen)
        self.wav_screen.show()

    def retranslateUi(self, menu):
        _translate = QtCore.QCoreApplication.translate
        menu.setWindowTitle(_translate("menu", "Приложение шифрования"))
        self.group_choose.setTitle(_translate("menu", "Выберите тип шифруемого файла"))
        self.push_txt.setText(_translate("menu", "txt"))
        self.push_wav.setText(_translate("menu", "wav"))
        self.push_bmp.setText(_translate("menu", "bmp"))
        self.push_jpg.setText(_translate("menu", "jpg"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menu = QtWidgets.QWidget()
    ui = Ui_menu()
    ui.setupUi(menu)
    menu.show()
    sys.exit(app.exec_())
