import  sys
import os

rus_alf = "КАМОНВЕРХСТорухаес"
eng_alf = "KAMOHBEPXCTopyxaec"

# выбор параметров функции*
def start():
    while True:
        function = int(input('Выберите функцию: 1 - вставить текст 2 - вынуть текст 3 - выйти \n'))
        if function == 1:
            encode()
        elif function == 2:
            decrypt()
        elif function == 3:
            break
        else:
            print('Такой функции нет ! \n')


def encode():
    # открываем/создаем нужыне файлы
    text = open('t.txt', 'r')
    elementary_txt = open('elementary.txt', 'r')
    encode_txt = open('encode_elementary.txt', 'w')

    alf_to_encode = 0
    encode_bits = 8

    while True:
        symvol = text.read(1)
        # закончились символы, конец цикла
        if not symvol:
            break

        if symvol in eng_alf:
            if encode_bits == 8:
                alf_to_encode = text.read(1)
                if not alf_to_encode:
                    encode_txt.write(symvol)
                    # закрываем файлы
                    text.close()
                    elementary_txt.close()
                    encode_txt.close()

                alf_to_encode = ord(alf_to_encode)
                encode_bits = 0

            bit_from_alf = (alf_to_encode & 0b10000000) >> 7

            if bit_from_alf:
                symvol = rus_alf[eng_alf.index(symvol)]

            alf_to_encode <<= 1
            alf_to_encode %= 256
            encode_bits += 1

        encode_txt.write(symvol)

    encode_txt.write(text.read())


    #закрываем файлы
    text.close()
    elementary_txt.close()
    encode_txt.close()

def decrypt():
    pass