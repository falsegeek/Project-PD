from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog


class Ui_wav_screen(object):
    def setupUi(self, wav_screen):
        wav_screen.setObjectName("wav_screen")
        wav_screen.resize(416, 273)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        wav_screen.setWindowIcon(icon)

    # группа где находятся все элементы шифрования
        # описание самой группы
        self.group_enc = QtWidgets.QGroupBox(wav_screen)
        self.group_enc.setGeometry(QtCore.QRect(10, 10, 391, 131))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.group_enc.setFont(font)
        self.group_enc.setObjectName("group_enc")

        # описание окна с текстом 1
        self.description_enc1 = QtWidgets.QLabel(self.group_enc)
        self.description_enc1.setGeometry(QtCore.QRect(10, 20, 301, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.description_enc1.setFont(font)
        self.description_enc1.setObjectName("description_enc1")

        # кнопка выбора файла шифрования
        self.push_enc = QtWidgets.QPushButton(self.group_enc)
        self.push_enc.setGeometry(QtCore.QRect(10, 40, 75, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.push_enc.setFont(font)
        self.push_enc.setObjectName("push_enc")

        # кнопка начала шифрования
        self.start_enc = QtWidgets.QPushButton(self.group_enc)
        self.start_enc.setGeometry(QtCore.QRect(160, 90, 75, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.start_enc.setFont(font)
        self.start_enc.setObjectName("start_enc")

        # описание картинки
        self.wav_img = QtWidgets.QLabel(self.group_enc)
        self.wav_img.setGeometry(QtCore.QRect(300, 20, 81, 91))
        self.wav_img.setText("")
        self.wav_img.setPixmap(QtGui.QPixmap("images/wav.png"))
        self.wav_img.setScaledContents(True)
        self.wav_img.setObjectName("wav_img")

        # группа где находятся все элементы дешифрования
        # описание самой группы
        self.group_dec = QtWidgets.QGroupBox(wav_screen)
        self.group_dec.setGeometry(QtCore.QRect(10, 150, 391, 111))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.group_dec.setFont(font)
        self.group_dec.setObjectName("group_dec")

        # описание окна с текстом
        self.description_dec = QtWidgets.QLabel(self.group_dec)
        self.description_dec.setGeometry(QtCore.QRect(10, 20, 301, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.description_dec.setFont(font)
        self.description_dec.setObjectName("description_dec")

        # кнопка выбора файла дешифрования
        self.push_dec = QtWidgets.QPushButton(self.group_dec)
        self.push_dec.setGeometry(QtCore.QRect(10, 40, 75, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.push_dec.setFont(font)
        self.push_dec.setObjectName("push_dec")

        # кнопка начала дешифрования
        self.start_dec = QtWidgets.QPushButton(self.group_dec)
        self.start_dec.setGeometry(QtCore.QRect(160, 70, 75, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.start_dec.setFont(font)
        self.start_dec.setObjectName("start_dec")

        # описание картинки
        self.dec_img = QtWidgets.QLabel(self.group_dec)
        self.dec_img.setGeometry(QtCore.QRect(300, 20, 71, 71))
        self.dec_img.setText("")
        self.dec_img.setPixmap(QtGui.QPixmap("images/encryption (1).png"))
        self.dec_img.setScaledContents(True)
        self.dec_img.setObjectName("dec_img")

        self.retranslateUi(wav_screen)
        QtCore.QMetaObject.connectSlotsByName(wav_screen)
        self.push_enc.clicked.connect(self.file_browser)  # выбор файла для зашифровки
        self.push_dec.clicked.connect(self.file_browser)  # выбор файла для расшифровки

    def file_browser(self):  # функция для выбора файла (закрывает программу после выполнения*)
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)

        with open(path, "r") as f:
            print(f.readline())

    def retranslateUi(self, wav_screen):
        _translate = QtCore.QCoreApplication.translate
        wav_screen.setWindowTitle(_translate("wav_screen", "Приложение шифрования: WAV"))
        self.group_enc.setTitle(_translate("wav_screen", "Зашифровать"))
        self.description_enc1.setText(_translate("wav_screen", "1. Выберите данные для шифрования в формате \"txt\""))
        self.push_enc.setText(_translate("wav_screen", "Файл"))
        self.start_enc.setText(_translate("wav_screen", "Начать"))
        self.group_dec.setTitle(_translate("wav_screen", "Расшифровать"))
        self.description_dec.setText(_translate("wav_screen", "1. Выберите файл для расшифровки"))
        self.push_dec.setText(_translate("wav_screen", "Файл"))
        self.start_dec.setText(_translate("wav_screen", "Начать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wav_screen = QtWidgets.QWidget()
    ui = Ui_wav_screen()
    ui.setupUi(wav_screen)
    wav_screen.show()
    sys.exit(app.exec_())
