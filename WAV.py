import os

WAV_HEADER_SIZE = 44

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
    input_wav_name = open('pip.wav', 'rb')
    output_wav_name =  open('pip_elementary.wav', 'wb')
    text_file = open('t.txt', 'r')
    degree = int(input('Выберите степерь шифрования 1/2/4/8/16\n'))

    if degree not in [1, 2, 4, 8, 16]:
        print("степерь шифрования 1/2/4/8/16")
        return False

    input_wav = open('pip.wav', 'rb')
    text_len = os.stat('t.txt').st_size

    wav_header = input_wav.read(WAV_HEADER_SIZE)
    data_size = int.from_bytes(wav_header[40:44], byteorder='little')

    if text_len > data_size * degree / 16:
        print("много")
        input_wav.close()
        return False

    text = open('t.txt', 'r')
    output_wav = open('pip_elementary.wav', 'wb')
    output_wav.write(wav_header)

    data = input_wav.read(data_size)
    text_mask, sample_mask = create_masks(degree)

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



def decrypt():
    input_wav_name = open('pip_elementary.wav', 'rb')
    text_file = open('t.txt', 'w')
    degree = int(input('Выберите степерь шифрования 1/2/4/8/16\n'))
    symbols_to_read = int(input('символ'))

    if degree not in [1, 2, 4, 8, 16]:
        print("степерь шифрования 1/2/4/8/16")
        return False

    input_wav = open('pip_elementary.wav', 'rb')

    wav_header = input_wav.read(WAV_HEADER_SIZE)
    data_size = int.from_bytes(wav_header[40:44], byteorder='little')

    if symbols_to_read >= data_size * degree / 16:
        print("Много")
        input_wav.close()
        return False

    text = open('t_elementary.txt', 'w', encoding='utf-8')

    _, sample_mask = create_masks(degree)
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


def create_masks(degree):

    text_mask = 0b1111111111111111
    sample_mask = 0b1111111111111111

    text_mask <<= (16 - degree)
    text_mask %= 65536
    sample_mask >>= degree
    sample_mask <<= degree

    return text_mask, sample_mask

start()
