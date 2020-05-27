import  sys
import os

BMP_HEADER_SIZE = 54

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
    degree = int(input('Выберите степерь шифрования 1/2/4/8\nЧем больше тем хуже изображение ! \n'))
    text_size = os.stat('t.txt').st_size
    image_size = os.stat('t.bmp').st_size
    #if text_size >= image_size * degree/8 -54:
        #print('Слишком большой текст\n')
        #return

    text = open('t.txt', 'r')
    elementary_bmp = open('t.bmp', 'rb') # rb - открытие на чтение в двоичном режим
    encode_bmp = open('encode_t.bmp', 'wb')# wb - открытие на запись в двоичном режим

    first54 = elementary_bmp.read(54)
    encode_bmp.write(first54)# переписываем начальные байты

    text_mask, image_mask = masks(degree)


    while True:
        symvol = text.read(1)
        if not symvol:
            break
        symvol = ord(symvol)
        for byte_i in range(0, 8, degree):
            image_byte = int.from_bytes(elementary_bmp.read(1), sys.byteorder) & image_mask
            bits = symvol & text_mask
            bits >>= (8-degree)
            image_byte |= bits
            encode_bmp.write(image_byte.to_bytes(1, sys.byteorder))
            symvol <<= degree

    encode_bmp.write(elementary_bmp.read())
    text.close()
    elementary_bmp.close()
    encode_bmp.close()

def masks(degree):
    text_mask = 0b11111111
    image_mask = 0b11111111

    text_mask <<= (8-degree)
    text_mask %= 256
    image_mask >>= degree
    image_mask <<= degree

    return text_mask, image_mask

def decrypt():
    degree = int(input('Выберите шифрование 1/2/4/8\n'))
    to_size = int(input('Cколько символов закодированно \n'))
    image_size = os.stat('encode_t.bmp').st_size
    if to_size >= image_size * degree / 8 - 54:
        print('Слишком большой текст\n')
        return

    text = open('encode_t.txt', 'w', encoding='utf-8')
    encode_bmp = open('encode_t.bmp', 'rb')

    encode_bmp.seek(BMP_HEADER_SIZE)
    text_mask, image_mask = masks(degree)
    image_mask = ~image_mask

    size = 0
    while size < to_size:
        symvol = 0
        for bits_size in range(0,8, degree):
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

start()

