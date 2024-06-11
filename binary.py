"""#bytes and bytearray"""

import struct, binascii, unicodedata, re, binascii


#bytes and bytearray
blist = [1,2,3,255]
the_bytes = bytes(blist)
the_bytes
the_byte_array = bytearray(blist)
the_byte_array
the_byte_array[1] = 127
the_byte_array
the_bytes = bytes(range(0, 256))
the_byte_array = bytearray(range(0, 256))
the_bytes


valid_png_header =  b'\x89PNG\r\n\x1a\n'
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
if data[:8] == valid_png_header:
    width,height = struct.unpack('>LL', data[16:24])
    print('Valid PNG, width', width, 'heaight', height)
else:
    print('Not a valid PNG')

data[16:20]
data[20:24]
struct.pack('>L',154)
struct.pack('>L',141)
struct.unpack('>2L', data[16:24])
struct.unpack('>16x2L6x', data)


print(binascii.hexlify(valid_png_header))  # b'89504e470d0a1a0a'
print(binascii.unhexlify(b'89504e470d0a1a0a'))

mystery =  '\U0001f4a9'
unicodedata.name( '\U0001f4a9')
unicodedata.lookup('PILE OF POO')
pop_bytes = mystery.encode('utf-8')
pop_bytes
pop_string = pop_bytes.decode('utf-8')
pop_string == pop_bytes
mammoth = """
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.
All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.
Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.
May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.
Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.
We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.
"""
re.findall(r'\bc\w*\b', mammoth)
re.findall(r'\bc\w{3}\b', mammoth)
re.findall(r'\b\w*r\b', mammoth)
re.findall(r'\b\w*[eyuioa]{3}\w*\b', mammoth)
gif = binascii.unhexlify('47494638396101000100800000000000ffffff21f9'+
'0401000000002c000000000100010000020144003b')
gif = b'GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff!' + \
b'\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x01D\x00;'
struct.unpack('<HH',gif[6:10])

