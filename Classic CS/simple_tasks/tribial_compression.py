from sys import getsizeof

class NewInt:
    def __init__(self, value):
        self.value = value
        self.index = 0
        
    def bit_length(self):
        return self.value.bit_length()    
        
    def __getitem__(self, item):
        list1 = list(str(self.value))
        return int(list1[item])

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            result = list(str(self.value))[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result
            
        

i = NewInt(12310231023102312031023)
for c in i:
    print(c)
i[7]


class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)
        
    def _compress(self, gene: str) -> None:
        self.bit_String: NewInt = NewInt(1).value       # start mark
        for nucleotide in gene.upper():
            self.bit_String <<= 2       # shift left by 2 bits
            if nucleotide == 'A':       # change 2 last bits by 00
                self.bit_String |= 0b00
            elif nucleotide == 'C':     # change 2 last bits by 01
                self.bit_String |= 0b01
            elif nucleotide == 'G':     # change 2 last bits by 10
                self.bit_String |= 0b10
            elif nucleotide == 'T':     # change 2 last bits by 11
                self.bit_String |= 0b11
            else:
                raise ValueError('Invalid Nucleotide:{}'.format(nucleotide))
    
    def decompress(self) -> str:
        gene: str = ''
        for i in range(0, self.bit_String.bit_length() - 1, 2):
            # -1 to exclude mark
            bits: int = self.bit_String >> i & 0b11
            # get only 2 significant bits
            if bits == 0b00:        # A
                gene += 'A'
            elif bits == 0b01:      # C
                gene += 'C'
            elif bits == 0b10:      # G
                gene += 'G'
            elif bits == 0b11:      # T
                gene += 'T'
            else:
                raise ValueError('Invalid bits:{}'.format(bits))
        return gene[::-1]         
    
    def __str__(self) -> str:       # representation of string as a beautiful output
        return self.decompress()
    
    
if __name__ == '__main__':
    original: str = 'GTGCACGTAAAGGCTT' * 100
    print('original is {} bytes'.format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)       # compression
    print('compressed is {} bytes'.format(getsizeof(compressed.bit_String)))
    print(compressed)           # decompression
    print('original and decompressed are the same: {}'.format(original == 
                                                              compressed.decompress()))
    