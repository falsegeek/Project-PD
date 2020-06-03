import os

class TXT(object):

    """def start():
        while True:
            function = int(input('Выберите функцию: 1 - вставить текст 2 - вынуть текст 3 - выйти \n'))
            if function == 1:
                encode()
            elif function == 2:
                decrypt()
            elif function == 3:
                break
            else:
                print('Такой функции нет ! \n')"""
    
    def __init__(self, rus_letters, eng_letters):
        self.rus_letters = "КАМОНВЕРХСТорухаес"
        self.eng_letters = "KAMOHBEPXCTopyxaec"

    def encode(self, source_txt, container_txt, output_txt, rus_letters, eng_letters):

        self.source_txt = open('t.txt', 'r')
        self.container_txt = open('elementary.txt', 'r')
        self.output_txt = open('encode_elementary.txt', 'w')
        self.rus_letters = rus_letters
        self.eng_letters = eng_letters
        letter_to_encode = 0
        encoded_bits: int = 8 # Программа сама решила добавить int хз

        """ source_txt = open('t.txt', 'r')
                container_txt = open('elementary.txt', 'r')
                output_txt = open('encode_elementary.txt', 'w')
        """
        
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

    def decrypt(self, encoded_txt, decoded_txt, symbols_to_read, rus_letters, eng_letters):
        self.encoded_txt = encoded_txt
        self.decoded_txt = decoded_txt
        self.symbols_to_read = symbols_to_read
        self.rus_letters = rus_letters
        self.eng_letters = eng_letters
        """encoded_txt = open('encode_elementary.txt', 'r')
        decoded_txt = open('encode_elementary11.txt', 'w', encoding='utf-8')
        symbols_to_read = int(input('Cколько символов закодированно \n'))"""
        read = 0
        bits_read = 0
        byte = 0

        while read < symbols_to_read:
            symbol = encoded_txt.read(1)
            if not symbol:
                encoded_txt.close()
                decoded_txt.close()

                return True

            if symbol in eng_letters:
                byte <<= 1
                bits_read += 1
            elif symbol in rus_letters:
                byte <<= 1
                byte |= 1
                bits_read += 1

            if bits_read == 8:
                decoded_txt.write(chr(byte))
                read += 1
                bits_read = byte = 0

                if chr(byte) == '\n' and len(os.linesep) == 2:
                    read += 1

        encoded_txt.close()
        decoded_txt.close()

        return True
