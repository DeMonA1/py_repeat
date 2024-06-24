"""#re"""
import struct, binascii, unicodedata, re, binascii
import re, string

#re
result = re.match('You','Young Frankenstein')
youpattern = re.compile('You')
result = youpattern.match('Young Frankenstein')
source = 'Young Frankenstein'
m = re.match('You', source)
if m:
    print(m.group())
if m := re.match('Frank', source):
    print(m.group())
if m := re.match('.*Frank', source):
    print(m.group())

if m := re.search('Frank', source):
    print(m.group())

m = re.findall('n', source)
m # list
print('Found', len(m), 'matches')
m = re.findall('n.', source)
m
m = re.findall('n.?', source)
m

m = re.split('n', source)
m

m = re.sub('n', '?', source)
m

printable = string.printable
len(printable)
printable[0:50]
printable[50:]
re.findall(r'\d', printable)
re.findall(r'\w', printable)
re.findall(r'\s', printable)
x = 'abc' + '-/*' + '\u00ea' + '\u0115'
re.findall(r'\w', x)


source = """I wish I may, I wish I might
    Have a dish of fish tonight."""
re.findall('wish', source)
re.findall('wish|fish', source)
re.findall('^wish', source)
re.findall('^I wish', source)
re.findall('fish tonight.$', source)
re.findall('[wf]ish', source)
re.findall('[wsh]+', source)
re.findall(r'ght\W', source)
re.findall('I (?=wish)', source)
re.findall(' (?<=I) wish', source)
re.findall(r'\bfish', source)

m = re.search(r'(.dish\b).*(\bfish)', source)
m.group()
m.groups()

m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
m.group()
m.groups()
m.group('DISH')
m.group('FISH')

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
