class EncoderDNA:

    encode_map = {'A': 0b00, 'C': 0b01, 'G': 0b10, 'T': 0b11}
    decode_map = {0b00: 'A', 0b01: 'C', 0b10: 'G', 0b11: 'T'}

    def encode(self, dna):
        bits = 1
        for nucleotide in dna.upper():
            if nucleotide not in EncoderDNA.encode_map.keys():
                raise ValueError(f'Invalid nucleotide: {nucleotide}')
            bits <<= 2
            bits |= EncoderDNA.encode_map[nucleotide]
        return bits

    def decode(self, encoded_dna):
        decoded_dna = ''
        for i in range(0, encoded_dna.bit_length() - 1, 2):
            bits = encoded_dna >> i & 0b11
            if bits not in EncoderDNA.decode_map.keys():
                raise ValueError(f'Invalid bits: {bits}')
            decoded_dna = EncoderDNA.decode_map[bits] + decoded_dna
        return decoded_dna
