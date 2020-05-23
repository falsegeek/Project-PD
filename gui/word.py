from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog


class Ui_word_screen(object):
    def setupUi(self, word_screen):
        word_screen.setObjectName("word_screen")
        word_screen.resize(415, 253)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        word_screen.setWindowIcon(icon)

    # группа где находятся все элементы дешифрования
        # описание самой группы
        self.group_dec = QtWidgets.QGroupBox(word_screen)
        self.group_dec.setGeometry(QtCore.QRect(10, 130, 391, 111))
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

    # группа где находятся все элементы шифрования
        # описание самой группы
        self.group_enc = QtWidgets.QGroupBox(word_screen)
        self.group_enc.setGeometry(QtCore.QRect(10, 10, 391, 111))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.group_enc.setFont(font)
        self.group_enc.setObjectName("group_enc")

        # описание окна с текстом
        self.description_enc = QtWidgets.QLabel(self.group_enc)
        self.description_enc.setGeometry(QtCore.QRect(10, 20, 301, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.description_enc.setFont(font)
        self.description_enc.setObjectName("description_enc")

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
        self.start_enc.setGeometry(QtCore.QRect(160, 70, 75, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.start_enc.setFont(font)
        self.start_enc.setObjectName("start_enc")

        # описание картинки
        self.word_img = QtWidgets.QLabel(self.group_enc)
        self.word_img.setGeometry(QtCore.QRect(300, 10, 81, 91))
        self.word_img.setText("")
        self.word_img.setPixmap(QtGui.QPixmap("images/doc.png"))
        self.word_img.setScaledContents(True)
        self.word_img.setObjectName("word_img")


        self.retranslateUi(word_screen)
        QtCore.QMetaObject.connectSlotsByName(word_screen)
        self.push_enc.clicked.connect(self.file_browser)  # выбор файла для зашифровки
        self.push_dec.clicked.connect(self.file_browser)  # выбор файла для расшифровки

    def file_browser(self):  # функция для выбора файла (закрывает программу после выполнения*)
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)

        with open(path, "r") as f:
            print(f.readline())

    def retranslateUi(self, word_screen):
        _translate = QtCore.QCoreApplication.translate
        word_screen.setWindowTitle(_translate("word_screen", "Приложение шифрования: Word"))
        self.group_dec.setTitle(_translate("word_screen", "Расшифровать"))
        self.description_dec.setText(_translate("word_screen", "1. Выберите файл для расшифровки"))
        self.push_dec.setText(_translate("word_screen", "Файл"))
        self.start_dec.setText(_translate("word_screen", "Начать"))
        self.group_enc.setTitle(_translate("word_screen", "Зашифровать"))
        self.description_enc.setText(_translate("word_screen", "1. Выберите данные для шифрования в формате \"txt\""))
        self.push_enc.setText(_translate("word_screen", "Файл"))
        self.start_enc.setText(_translate("word_screen", "Начать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    word_screen = QtWidgets.QWidget()
    ui = Ui_word_screen()
    ui.setupUi(word_screen)
    word_screen.show()
    sys.exit(app.exec_())
