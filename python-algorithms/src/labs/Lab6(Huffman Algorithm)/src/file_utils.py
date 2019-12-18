import huffmon_code
import os


class FileUtils:

    def __init__(self, path):
        self.path = path
        self.huffman_dictionary = {}

    def compress(self):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + ".bin"

        with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
            text = file.read()
            text = text.rstrip()
            self.huffman_dictionary, byte_array = huffmon_code.get_huffman_code(text)
            output.write(bytes(byte_array))
        return output_path

    def decompress(self, input_path):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + "_decompressed" + ".txt"

        with open(input_path, 'rb') as file, open(output_path, 'w') as output:
            bit_string = ""

            byte = file.read(1)
            while len(byte) > 0:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)

            decompressed_text = huffmon_code.decode_huffman_code(bit_string, self.huffman_dictionary)
            output.write(decompressed_text)


file_utils = FileUtils('../data/little_prince')
output_path = file_utils.compress()
file_utils.decompress(output_path)