from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog


class Ui_txt_screen(object):
    def setupUi(self, txt_screen):
        txt_screen.setObjectName("txt_screen")
        txt_screen.resize(416, 257)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        txt_screen.setWindowIcon(icon)

    # группа где находятся все элементы дешифрования
        # описание самой группы
        self.group_dec = QtWidgets.QGroupBox(txt_screen)
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
        self.dec_img.setGeometry(QtCore.QRect(310, 20, 71, 71))
        self.dec_img.setText("")
        self.dec_img.setPixmap(QtGui.QPixmap("images/encryption (1).png"))
        self.dec_img.setScaledContents(True)
        self.dec_img.setObjectName("dec_img")

    # группа где находятся все элементы шифрования
        # описание самой группы
        self.group_enc = QtWidgets.QGroupBox(txt_screen)
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
        self.txt_img = QtWidgets.QLabel(self.group_enc)
        self.txt_img.setGeometry(QtCore.QRect(300, 10, 81, 91))
        self.txt_img.setText("")
        self.txt_img.setPixmap(QtGui.QPixmap("images/txt.png"))
        self.txt_img.setScaledContents(True)
        self.txt_img.setObjectName("txt_img")


        self.retranslateUi(txt_screen)
        QtCore.QMetaObject.connectSlotsByName(txt_screen)
        self.push_enc.clicked.connect(self.file_browser)  # выбор файла для зашифровки
        self.push_dec.clicked.connect(self.file_browser)  # выбор файла для расшифровки

        self.start_enc.clicked.connect(self.start_encode) # старт шифровки
        # self.start_dec.clicked.connect(self.start_decrypt)

    def start_elementaryTXT(self):

        container_txt = open('elementary.txt', 'w')
        container_txt.write('Hello! I am Jane. I am 21. I am a student. I consider it to be a special time in my life. Student life is always full of fun, new impressions and knowledge. I like being a student. Each day I learn something new and communicate with my friends. We meet almost every day. Sometimes we stay at the university after classes to prepare our homework for the next day or just to talk about our student life.I like spending time with my friends. We often visit each other. I can talk with them for hours. They can help me and support me in any situation. I can say the same about my parents, with whom I live. My mother is a very wise woman. She understands me. We are not only close relatives, but also close friends. We have the same favourite colours — green and blue. These are the colours of nature and the sky. Our family hobby is travelling. We like seeing new places, meeting new people, exchanging our impressions. We often travel in summer and in winter. I adore Turkey, Egypt, and France. These countries have their ownr')
        container_txt.write('ditions, unique nature and culture.My other hobbies are music and theatre. I often visit the theatre. I sympathize with the characters on the stage. I try to understand them and, finally, I find it easier to solve my own problems watching the play. I understand my family and friends better. I am grateful to them for being so close to me, for their understanding and support. a well-known fact, that the geographical position very often influences the climate and weather of any country. The United States is no exception. Here, the Cascade Mountains and the Sierra Nevada Mountains, due to their being close to the west coast, catch the largest share of the rain off the Pacific Ocean. As a result there is too little rain for almost the whole western half of the Unites States, which lies in the of the mountains. In a great part of that territory farmers must depend on irrigation water from the snows or rains. One of the most important geographic boundaries in the United States is the 50-centimeter rainfall line. It ')
        container_txt.write('runs north and south almost through the middle of the country. East of the line, farming here is easy and the population is relatively large. West of the line, you can find man-made irrigation systems, dry-farming and grazing. There are fewer people living here. West of the RockyMountains, there are vast areas without any trees. In this part of the country are the deserts which receive as little as over 12 centimeters of rainfall a year. If there were no mountains or oceans, then the amount of the heat would progress from north to south. Instead, there are all kinds of unexpected differences in climate. For example, all along the western coast, the temperature changes little between summer and winter. The climate along the northern part of this coast is similar to that of England.But in the north central part of the country, summer and winter are very different. There the average difference between July and January is 36 degrees centigrade The variations in temperature within the United States have had a mark')
        container_txt.write('ed effect on the country’s economy and living standards. There is a long crop-growing season along the south-east coast where cotton is a principal product. In some of the cooler climates or in climates which combine coolness and humidity, people grow apples, wheat and corn. This gives the United States a large variety of agricultural products.music culture would be incomplete without blues music. Thought it was created in the early decades of the 20th century, blues music has had a huge influence on American popular music up to the present days. In fact, many key elements we hear in pop, soul, rhythm and blues, rock and roll, have their beginnings in blues music. It has never been the leader in music sales. Blues music has retained a significant presence not only in concerts and festivals throughout the United States, but in the daily life of every person on the planet, as well. One can hear the sound of the blues in unexpected places, from a television commercial to a new country or western song.The best kn')
        container_txt.write('own blues musician today is B.B. King. His fame is well-deserved. Born in Indianola, Mississippi in 1925, he earned the nicknamewhile playing on radio programs in Memphis, Tennessee. From the 1940s through the 1960s, he played mostly in clubs in the South that had only black audiences. In 1948, he had a hit record with and toured steadily thereafter. His fame spread as he played at blues festivals, concert halls, universities, and on television shows across the country. No other blues artist has worked harder, than B. B. King in his many years of playing over three hundred shows a year. By the late 1960s, B. B. had perfected his famous guitar style of vibrating the fingers of his left hand as he played, and bending notes to achieve the blues notes, that are such an integral part of blue music. This singing guitar sound, coupled with his expressive tenor voice, brought King great success in 1969 with the recording of The song broke through the limited sales of the blues market to achieve mainstream success and')
        container_txt.write('brought B.B. a Grammy award.long and distinguished career includes many musical collaborations. Young rock musicians, in particular, appreciate his contributions to their genre. In 1988 B.B. played guitar and sang on the hit song In a nutshell')
        container_txt.close()

    def start_encode(self, filename):
        self.start_elementaryTXT()
        rus_letters = "КАМОНВЕРХСТорухаес"
        eng_letters = "KAMOHBEPXCTopyxaec"
        source_txt = open(filename, 'r')
        container_txt = open('elementary.txt', 'r')
        output_txt = open('encode_elementary.txt', 'w')

        letter_to_encode = 0
        encoded_bits = 8

        while True:
            symbol_from_text = container_txt.read(1)
            if not symbol_from_text:
                break

            if symbol_from_text in eng_letters:
                if encoded_bits == 8:
                    letter_to_encode = source_txt.read(1)
                    if not letter_to_encode:
                        output_txt.write(symbol_from_text)

                        source_txt.close()
                        container_txt.close()
                        output_txt.close()

                        return True

                    letter_to_encode = ord(letter_to_encode)
                    encoded_bits = 0

                bit_from_letter = (letter_to_encode & 0b10000000) >> 7

                if bit_from_letter:
                    symbol_from_text = rus_letters[eng_letters.index(symbol_from_text)]

                letter_to_encode <<= 1
                letter_to_encode %= 256
                encoded_bits += 1

            output_txt.write(symbol_from_text)

        output_txt.write(source_txt.read())

        source_txt.close()
        container_txt.close()
        output_txt.close()

        return True

    def file_browser(self):  # функция для выбора файла (закрывает программу после выполнения*)
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)

        with open(path, "r") as f:
            print(f.readline())

    def retranslateUi(self, txt_screen):
        _translate = QtCore.QCoreApplication.translate
        txt_screen.setWindowTitle(_translate("txt_screen", "Приложение шифрования: TXT"))
        self.group_dec.setTitle(_translate("txt_screen", "Расшифровать"))
        self.description_dec.setText(_translate("txt_screen", "1. Выберите файл для расшифровки"))
        self.push_dec.setText(_translate("txt_screen", "Файл"))
        self.start_dec.setText(_translate("txt_screen", "Начать"))
        self.group_enc.setTitle(_translate("txt_screen", "Зашифровать"))
        self.description_enc.setText(_translate("txt_screen", "1. Выберите данные для шифрования в формате \"txt\""))
        self.push_enc.setText(_translate("txt_screen", "Файл"))
        self.start_enc.setText(_translate("txt_screen", "Начать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    txt_screen = QtWidgets.QWidget()
    ui = Ui_txt_screen()
    ui.setupUi(txt_screen)
    txt_screen.show()
    sys.exit(app.exec_())
