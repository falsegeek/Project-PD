# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wav.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import struct
import datetime
import random
from PyQt5 import QtCore, QtGui, QtWidgets
import wave
import os
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog


class Ui_wav_screen(object):
    def setupUi(self, wav_screen):
        wav_screen.setObjectName("wav_screen")
        wav_screen.resize(416, 273)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        wav_screen.setWindowIcon(icon)
        self.group_enc = QtWidgets.QGroupBox(wav_screen)
        self.group_enc.setGeometry(QtCore.QRect(10, 10, 391, 131))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.group_enc.setFont(font)
        self.group_enc.setObjectName("group_enc")
        self.description_enc1 = QtWidgets.QLabel(self.group_enc)
        self.description_enc1.setGeometry(QtCore.QRect(10, 20, 301, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.description_enc1.setFont(font)
        self.description_enc1.setObjectName("description_enc1")
        self.start_enc = QtWidgets.QPushButton(self.group_enc)
        self.start_enc.setGeometry(QtCore.QRect(110, 60, 91, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.start_enc.setFont(font)
        self.start_enc.setObjectName("start_enc")
        self.wav_img = QtWidgets.QLabel(self.group_enc)
        self.wav_img.setGeometry(QtCore.QRect(300, 20, 81, 91))
        self.wav_img.setText("")
        self.wav_img.setPixmap(QtGui.QPixmap("images/wav.png"))
        self.wav_img.setScaledContents(True)
        self.wav_img.setObjectName("wav_img")
        self.group_dec = QtWidgets.QGroupBox(wav_screen)
        self.group_dec.setGeometry(QtCore.QRect(10, 150, 391, 111))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.group_dec.setFont(font)
        self.group_dec.setObjectName("group_dec")
        self.description_dec = QtWidgets.QLabel(self.group_dec)
        self.description_dec.setGeometry(QtCore.QRect(10, 20, 301, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.description_dec.setFont(font)
        self.description_dec.setObjectName("description_dec")
        self.start_dec = QtWidgets.QPushButton(self.group_dec)
        self.start_dec.setGeometry(QtCore.QRect(110, 60, 91, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.start_dec.setFont(font)
        self.start_dec.setObjectName("start_dec")
        self.dec_img = QtWidgets.QLabel(self.group_dec)
        self.dec_img.setGeometry(QtCore.QRect(300, 20, 71, 71))
        self.dec_img.setText("")
        self.dec_img.setPixmap(QtGui.QPixmap("images/encryption (1).png"))
        self.dec_img.setScaledContents(True)
        self.dec_img.setObjectName("dec_img")

        self.retranslateUi(wav_screen)
        QtCore.QMetaObject.connectSlotsByName(wav_screen)
        self.start_enc.clicked.connect(self.start_encode)  # выбор файла для зашифровки
        self.start_dec.clicked.connect(self.start_decrypt)  # выбор файла для расшифровки

    def start_elementaryWAV(self):

       ''' noise_output = wave.open('Temporary_file.wav', 'w')
        noise_output.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

        values = []

        for i in range(0, 2):
            value = random.randint(-32767, 32767)
            packed_value = struct.pack('h', value)
            values.append(packed_value)
            values.append(packed_value)

        value_str = ''.join(values)
        noise_output.writeframes(value_str)

        noise_output.close()'''

       SAMPLE_LEN = 44100 * 5  # 300 seconds of noise, 5 minutes

       print("Create file using wave and writeframes twice in each iteration")

       noise_output = wave.open('Temporary_file.wav', 'w')
       noise_output.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

       d1 = datetime.datetime.now()

       for i in range(0, SAMPLE_LEN):
           value = random.randint(-32767, 32767)
           packed_value = struct.pack('h', value)
           noise_output.writeframes(packed_value)
           noise_output.writeframes(packed_value)

       d2 = datetime.datetime.now()
       print(d2 - d1), "(time for writing frames)"

       noise_output.close()

       d3 = datetime.datetime.now()
       print(d3 - d2), "(time for closing the file)"

       # --------------



    def start_encode(self):
        self.start_elementaryWAV()
        path = self.file_browser()
        #input_wav_name = open('Temporary_file.wav', 'rb')
        #output_wav_name = open('Encrypted.wav', 'wb')
        #text_file = open(path, 'r')
        #degree = int(input('Выберите степерь шифрования 1/2/4/8/16\n'))

        #if degree not in [1, 2, 4, 8, 16]:
            #print("степерь шифрования 1/2/4/8/16")
            #return False

        #pathh = os.path.join(os.path.abspath(os.path.dirname(file)), 'Temporary_file.raw')
        #os.remove(pathh)
        #os.remove('Temporary_file.raw')

        input_wav = open('Temporary_file.wav', 'rb')
        text_len = os.stat(path).st_size

        wav_header = input_wav.read(WAV_HEADER_SIZE)
        data_size = int.from_bytes(wav_header[40:44], byteorder='little')

        if text_len > data_size * degree / 16:
            print("много")
            input_wav.close()
            return False

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

        output_wav = open('Encrypted.wav', 'wb')
        output_wav.write(wav_header)

        data = input_wav.read(data_size)
        text_mask, sample_mask = self.create_masks(degree)

        while True:
            txt_symbol = text.read(1)
            if not txt_symbol:
                break

            txt_symbol = ord(txt_symbol)
            txt_symbol <<= 8

            if degree == 16:
                another_symbol = text.read(1)
                if not another_symbol:
                    another_symbol = 0b0
                else:
                    print("another {0}, bin {1:b}".format(another_symbol, ord(another_symbol)))
                    another_symbol = ord(another_symbol)

                txt_symbol |= another_symbol

            for step in range(0, 16, degree):
                if step == 8 and not txt_symbol:
                    break

                sample = int.from_bytes(data[:2], byteorder='little') & sample_mask
                data = data[2:]

                bits = txt_symbol & text_mask
                bits >>= (16 - degree)

                sample |= bits

                output_wav.write(sample.to_bytes(2, byteorder='little'))
                txt_symbol = (txt_symbol << degree) % 65536

        output_wav.write(data)
        output_wav.write(input_wav.read())

        input_wav.close()
        output_wav.close()

        return True



    def start_decrypt(self):
        path = self.file_browser()
        #input_wav_name = open('Encrypted.wav', 'rb')
        #text_file = open(path, 'w')
        #degree = int(input('Выберите степерь шифрования 1/2/4/8/16\n'))
        #symbols_to_read = int(input('символ'))

        #if degree not in [1, 2, 4, 8, 16]:
            #print("степерь шифрования 1/2/4/8/16")
            #return False

        input_wav = open('Encrypted.wav', 'rb')

        wav_header = input_wav.read(WAV_HEADER_SIZE)
        data_size = int.from_bytes(wav_header[40:44], byteorder='little')



        #if symbols_to_read >= data_size * degree / 16:
            #print("Много")
            #input_wav.close()
            #return False

        text = open(path, 'w', encoding='utf-8')

        _, sample_mask = self.create_masks(degree)
        sample_mask = ~sample_mask

        data = input_wav.read(data_size)
        symbols_to_read = 200
        read = 0
        read1 = ''
        read2 = ''
        while read1 != '@':
            two_symbols = 0
            for step in range(0, 16, degree):
                sample = int.from_bytes(data[:2], byteorder='little') & sample_mask
                data = data[2:]

                two_symbols <<= degree
                two_symbols |= sample

            first_symbol = two_symbols >> 8
            text.write(chr(first_symbol))
            read += 1

            if chr(first_symbol) == '\n' and len(os.linesep) == 2:
                read += 1

            if symbols_to_read - read > 0:
                second_symbol = two_symbols & 0b0000000011111111
                text.write(chr(second_symbol))
                read1 = str(chr(second_symbol))
                if read1 != '@':
                    read2 += read1

                read += 1

                if chr(second_symbol) == '\n' and len(os.linesep) == 2:
                    read += 1



        symbols_to_read = int(read2)
        _, sample_mask = self.create_masks(degree)
        sample_mask = ~sample_mask

        data = input_wav.read(data_size)

        read = 0
        while read < symbols_to_read:
            two_symbols = 0
            for step in range(0, 16, degree):
                sample = int.from_bytes(data[:2], byteorder='little') & sample_mask
                data = data[2:]

                two_symbols <<= degree
                two_symbols |= sample

            first_symbol = two_symbols >> 8
            text.write(chr(first_symbol))
            read += 1

            if chr(first_symbol) == '\n' and len(os.linesep) == 2:
                read += 1

            if symbols_to_read - read > 0:
                second_symbol = two_symbols & 0b0000000011111111
                text.write(chr(second_symbol))
                read += 1

                if chr(second_symbol) == '\n' and len(os.linesep) == 2:
                    read += 1

        text.close()
        input_wav.close()
        return True

    def create_masks(sefl, degree):

        text_mask = 0b1111111111111111
        sample_mask = 0b1111111111111111

        text_mask <<= (16 - degree)
        text_mask %= 65536
        sample_mask >>= degree
        sample_mask <<= degree

        return text_mask, sample_mask

    def retranslateUi(self, wav_screen):
        _translate = QtCore.QCoreApplication.translate
        wav_screen.setWindowTitle(_translate("wav_screen", "Приложение шифрования: WAV"))
        self.group_enc.setTitle(_translate("wav_screen", "Зашифровать"))
        self.description_enc1.setText(_translate("wav_screen", "Выбрать данные в формате \"txt\" и начать шифровку:"))
        self.start_enc.setText(_translate("wav_screen", "Зашифровать"))
        self.group_dec.setTitle(_translate("wav_screen", "Расшифровать"))
        self.description_dec.setText(_translate("wav_screen", "Выбрать данные в формате \"wav\" и начать дешифровку:"))
        self.start_dec.setText(_translate("wav_screen", "Расшифровать"))

    def file_browser(self):  # функция для выбора файла (закрывает программу после выполнения*)
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)

        with open(path, "r") as f:
            print(f.readline())
        return path

if __name__ == "__main__":
    import sys
    WAV_HEADER_SIZE = 44
    degree = 16
    app = QtWidgets.QApplication(sys.argv)
    wav_screen = QtWidgets.QWidget()
    ui = Ui_wav_screen()
    ui.setupUi(wav_screen)
    wav_screen.show()
    sys.exit(app.exec_())
