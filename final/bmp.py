# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bmp.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import os

class Ui_bmp_screen(object):

    def setupUi(self, bmp_screen):
        bmp_screen.setObjectName("bmp_screen")
        bmp_screen.resize(415, 352)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        bmp_screen.setWindowIcon(icon)
        self.group_enc = QtWidgets.QGroupBox(bmp_screen)
        self.group_enc.setGeometry(QtCore.QRect(10, 10, 391, 161))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.group_enc.setFont(font)
        self.group_enc.setObjectName("group_enc")
        self.description_enc1 = QtWidgets.QLabel(self.group_enc)
        self.description_enc1.setGeometry(QtCore.QRect(10, 80, 301, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.description_enc1.setFont(font)
        self.description_enc1.setObjectName("description_enc1")
        self.description_enc2 = QtWidgets.QLabel(self.group_enc)
        self.description_enc2.setGeometry(QtCore.QRect(10, 20, 301, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.description_enc2.setFont(font)
        self.description_enc2.setObjectName("description_enc2")
        self.radio_1_enc = QtWidgets.QRadioButton(self.group_enc)
        self.radio_1_enc.setGeometry(QtCore.QRect(10, 50, 31, 17))
        self.radio_1_enc.setObjectName("radio_1_enc")
        self.radio_2_enc = QtWidgets.QRadioButton(self.group_enc)
        self.radio_2_enc.setGeometry(QtCore.QRect(40, 50, 31, 17))
        self.radio_2_enc.setObjectName("radio_2_enc")
        self.radio_4_enc = QtWidgets.QRadioButton(self.group_enc)
        self.radio_4_enc.setGeometry(QtCore.QRect(70, 50, 31, 17))
        self.radio_4_enc.setObjectName("radio_4_enc")
        self.radio_8 = QtWidgets.QRadioButton(self.group_enc)
        self.radio_8.setGeometry(QtCore.QRect(100, 50, 31, 17))
        self.radio_8.setObjectName("radio_8")
        self.start_enc = QtWidgets.QPushButton(self.group_enc)
        self.start_enc.setGeometry(QtCore.QRect(20, 110, 75, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.start_enc.setFont(font)
        self.start_enc.setObjectName("start_enc")
        self.bmp_img = QtWidgets.QLabel(self.group_enc)
        self.bmp_img.setGeometry(QtCore.QRect(300, 30, 81, 91))
        self.bmp_img.setText("")
        self.bmp_img.setPixmap(QtGui.QPixmap("images/bmp.png"))
        self.bmp_img.setScaledContents(True)
        self.bmp_img.setObjectName("bmp_img")
        self.group_dec = QtWidgets.QGroupBox(bmp_screen)
        self.group_dec.setGeometry(QtCore.QRect(10, 180, 391, 161))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.group_dec.setFont(font)
        self.group_dec.setObjectName("group_dec")
        self.description_dec = QtWidgets.QLabel(self.group_dec)
        self.description_dec.setGeometry(QtCore.QRect(10, 80, 301, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.description_dec.setFont(font)
        self.description_dec.setObjectName("description_dec")
        self.start_dec = QtWidgets.QPushButton(self.group_dec)
        self.start_dec.setGeometry(QtCore.QRect(20, 110, 75, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.start_dec.setFont(font)
        self.start_dec.setObjectName("start_dec")
        self.dec_img = QtWidgets.QLabel(self.group_dec)
        self.dec_img.setGeometry(QtCore.QRect(310, 40, 71, 71))
        self.dec_img.setText("")
        self.dec_img.setPixmap(QtGui.QPixmap("images/encryption (1).png"))
        self.dec_img.setScaledContents(True)
        self.dec_img.setObjectName("dec_img")
        self.radio_4_dec = QtWidgets.QRadioButton(self.group_dec)
        self.radio_4_dec.setGeometry(QtCore.QRect(70, 50, 31, 17))
        self.radio_4_dec.setObjectName("radio_4_dec")
        self.radio_2_dec = QtWidgets.QRadioButton(self.group_dec)
        self.radio_2_dec.setGeometry(QtCore.QRect(40, 50, 31, 17))
        self.radio_2_dec.setObjectName("radio_2_dec")
        self.radio_1_dec = QtWidgets.QRadioButton(self.group_dec)
        self.radio_1_dec.setGeometry(QtCore.QRect(10, 50, 31, 17))
        self.radio_1_dec.setObjectName("radio_1_dec")
        self.radio_8_dec = QtWidgets.QRadioButton(self.group_dec)
        self.radio_8_dec.setGeometry(QtCore.QRect(100, 50, 31, 17))
        self.radio_8_dec.setObjectName("radio_8_dec")
        self.description_enc2_2 = QtWidgets.QLabel(self.group_dec)
        self.description_enc2_2.setGeometry(QtCore.QRect(10, 20, 301, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.description_enc2_2.setFont(font)
        self.description_enc2_2.setObjectName("description_enc2_2")

        self.retranslateUi(bmp_screen)
        QtCore.QMetaObject.connectSlotsByName(bmp_screen)
        self.start_enc.clicked.connect(self.start_encode)  # выбор файла для зашифровки
        self.start_dec.clicked.connect(self.start_decrypt)  # выбор файла для расшифровки

    def start_elementaryBMP(self):
        with open("Temporary_fileBMP.bmp", "w+b") as f:
            f.write(b'BM')  # ID field (42h, 4Dh)
            f.write((154).to_bytes(4, byteorder="little"))  # 154 bytes (122+32) Size of the BMP file
            f.write((0).to_bytes(2, byteorder="little"))  # Unused
            f.write((0).to_bytes(2, byteorder="little"))  # Unused
            f.write((122).to_bytes(4,byteorder="little"))  # 122 bytes (14+108) Offset where the pixel array (bitmap data) can be found
            f.write((108).to_bytes(4, byteorder="little"))  # 108 bytes Number of bytes in the DIB header (from this point)
            f.write((4).to_bytes(4, byteorder="little"))  # 4 pixels (left to right order) Width of the bitmap in pixels
            f.write((2).to_bytes(4, byteorder="little"))  # 2 pixels (bottom to top order) Height of the bitmap in pixels
            f.write((1).to_bytes(2, byteorder="little"))  # 1 plane Number of color planes being used
            f.write((32).to_bytes(2, byteorder="little"))  # 32 bits Number of bits per pixel
            f.write((3).to_bytes(4, byteorder="little"))  # 3 BI_BITFIELDS, no pixel array compression used
            f.write((32).to_bytes(4, byteorder="little"))  # 32 bytes Size of the raw bitmap data (including padding)
            f.write((2835).to_bytes(4, byteorder="little"))  # 2835 pixels/metre horizontal Print resolution of the image,
            f.write((2835).to_bytes(4,byteorder="little"))  # 2835 pixels/metre vertical   72 DPI × 39.3701 inches per metre yields 2834.6472
            f.write((0).to_bytes(4, byteorder="little"))  # 0 colors Number of colors in the palette
            f.write((0).to_bytes(4, byteorder="little"))  # 0 important colors 0 means all colors are important
            f.write(b'\x00\x00\xFF\x00')  # 00FF0000 in big-endian Red channel bit mask (valid because BI_BITFIELDS is specified)
            f.write(b'\x00\xFF\x00\x00')  # 0000FF00 in big-endian Green channel bit mask (valid because BI_BITFIELDS is specified)
            f.write(b'\xFF\x00\x00\x00')  # 000000FF in big-endian Blue channel bit mask (valid because BI_BITFIELDS is specified)
            f.write(b'\x00\x00\x00\xFF')  # FF000000 in big-endian Alpha channel bit mask
            f.write(b' niW')  # little-endian "Win " LCS_WINDOWS_COLOR_SPACE
            f.write((0).to_bytes(36,byteorder="little"))  # CIEXYZTRIPLE Color Space endpoints	Unused for LCS "Win " or "sRGB"
            f.write((0).to_bytes(4, byteorder="little"))  # 0 Red Gamma Unused for LCS "Win " or "sRGB"
            f.write((0).to_bytes(4, byteorder="little"))  # 0 Green Gamma Unused for LCS "Win " or "sRGB"
            f.write((0).to_bytes(4, byteorder="little"))  # 0 Blue Gamma Unused for LCS "Win " or "sRGB"
            f.write(b'\xFF\x00\x00\x7F')  # 255 0 0 127 Blue (Alpha: 127), Pixel (1,0)
            f.write(b'\x00\xFF\x00\x7F')  # 0 255 0 127 Green (Alpha: 127), Pixel (1,1)
            f.write(b'\x00\x00\xFF\x7F')  # 0 0 255 127 Red (Alpha: 127), Pixel (1,2)
            f.write(b'\xFF\xFF\xFF\x7F')  # 255 255 255 127 White (Alpha: 127), Pixel (1,3)
            f.write(b'\xFF\x00\x00\xFF')  # 255 0 0 255 Blue (Alpha: 255), Pixel (0,0)
            f.write(b'\x00\xFF\x00\xFF')  # 0 255 0 255 Green (Alpha: 255), Pixel (0,1)
            f.write(b'\x00\x00\xFF\xFF')  # 0 0 255 255 Red (Alpha: 255), Pixel (0,2)
            f.write(b'\xFF\xFF\xFF\xFF')  # 255 255 255 255 White (Alpha: 255), Pixel (0,3)
            f.close()

    def start_encode(self):
        #text_size = os.stat('t.txt').st_size
        #image_size = os.stat('t.bmp').st_size
        # if text_size >= image_size * degree/8 -54:
        # print('Слишком большой текст\n')
        # return
        self.start_elementaryBMP()
        path = self.file_browser()



        text = open(path, 'r')
        elementary_bmp = open('Temporary_fileBMP.bmp', 'rb')  # rb - открытие на чтение в двоичном режим
        encode_bmp = open('EncryptedBMP.bmp', 'wb')  # wb - открытие на запись в двоичном режим

        text = open(path, 'r')

        message_length = os.stat(path).st_size

        print(message_length)

        message_length = str(message_length)
        message_length += str('@')

        print(message_length)

        source = text.read()
        newsource = message_length + source
        text.close()
        text = open(path, 'w')
        text.write(newsource)
        text.close()
        text = open(path, 'r')

        first54 = elementary_bmp.read(BMP_HEADER_SIZE) #заменено
        encode_bmp.write(first54)  # переписываем начальные байты

        text_mask, image_mask = self.masks(degree)

        while True:
            symvol = text.read(1)
            if not symvol:
                break
            symvol = ord(symvol)
            for byte_i in range(0, 8, degree):
                image_byte = int.from_bytes(elementary_bmp.read(1), sys.byteorder) & image_mask
                bits = symvol & text_mask
                bits >>= (8 - degree)
                image_byte |= bits
                encode_bmp.write(image_byte.to_bytes(1, sys.byteorder))
                symvol <<= degree

        encode_bmp.write(elementary_bmp.read())
        text.close()
        elementary_bmp.close()
        encode_bmp.close()

    def start_decrypt(self):

        #image_size = os.stat('encode_t.bmp').st_size
        #if to_size >= image_size * degree / 8 - 54:
            #print('Слишком большой текст\n')
            #return
        path = self.file_browser()
        text = open('DecryptedBMP.txt', 'w', encoding='utf-8')
        encode_bmp = open(path, 'rb')

        encode_bmp.seek(BMP_HEADER_SIZE)
        text_mask, image_mask = self.masks(degree)
        image_mask = ~image_mask

        size = 0
        to_size =2000
        read1 = ''
        read2 = ''
        while size < to_size:
            if read1 == '@':
                break
            symvol = 0
            for bits_size in range(0, 8, degree):
                image_byte = int.from_bytes(encode_bmp.read(1), sys.byteorder) & image_mask

                symvol <<= degree
                symvol |= image_byte
            if chr(symvol) == '\n' and len(os.linesep) == 2:
                size += 1
            print('символ #{0} и {1:c}'.format(size, symvol))
            size += 1
            text.write(chr(symvol))
            read1 = str(chr(symvol))
            if read1 != '@':
                read2 += read1


        to_size = int(read2)
        size = 0
        while size < to_size:
            symvol = 0
            for bits_size in range(0, 8, degree):
                image_byte = int.from_bytes(encode_bmp.read(1), sys.byteorder) & image_mask

                symvol <<= degree
                symvol |= image_byte
            if chr(symvol) == '\n' and len(os.linesep) == 2:
                size += 1
            print('символ #{0} и {1:c}'.format(size, symvol))
            size += 1
            text.write(chr(symvol))

        text.close()
        encode_bmp.close()

    def masks(self, degree):
        text_mask = 0b11111111
        image_mask = 0b11111111

        text_mask <<= (8 - degree)
        text_mask %= 256
        image_mask >>= degree
        image_mask <<= degree

        return text_mask, image_mask

    def retranslateUi(self, bmp_screen):
        _translate = QtCore.QCoreApplication.translate
        bmp_screen.setWindowTitle(_translate("bmp_screen", "Приложение шифрования: BMP"))
        self.group_enc.setTitle(_translate("bmp_screen", "Зашифровать"))
        self.description_enc1.setText(_translate("bmp_screen", "Выбрать данные в формате \"txt\" и начать шифровку:"))
        self.description_enc2.setText(_translate("bmp_screen", "Выбрать степень сжатия"))
        self.radio_1_enc.setText(_translate("bmp_screen", "1"))
        self.radio_2_enc.setText(_translate("bmp_screen", "2"))
        self.radio_4_enc.setText(_translate("bmp_screen", "4"))
        self.radio_8.setText(_translate("bmp_screen", "8"))
        self.start_enc.setText(_translate("bmp_screen", "Начать"))
        self.group_dec.setTitle(_translate("bmp_screen", "Расшифровать"))
        self.description_dec.setText(_translate("bmp_screen", "Выбрать данные в формате \"bmp\" и начать дешифровку:"))
        self.start_dec.setText(_translate("bmp_screen", "Начать"))
        self.radio_4_dec.setText(_translate("bmp_screen", "4"))
        self.radio_2_dec.setText(_translate("bmp_screen", "2"))
        self.radio_1_dec.setText(_translate("bmp_screen", "1"))
        self.radio_8_dec.setText(_translate("bmp_screen", "8"))
        self.description_enc2_2.setText(_translate("bmp_screen", "Выбрать степень сжатия"))

    def file_browser(self):  # функция для выбора файла (закрывает программу после выполнения*)
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)

        #with open(path, "r") as f:
            #print(f.readline())
        return path


if __name__ == "__main__":
    import sys
    degree = 4
    BMP_HEADER_SIZE = 54
    app = QtWidgets.QApplication(sys.argv)
    bmp_screen = QtWidgets.QWidget()
    ui = Ui_bmp_screen()
    ui.setupUi(bmp_screen)
    bmp_screen.show()
    sys.exit(app.exec_())
