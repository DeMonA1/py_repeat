"""#Unicode, #encoding and decoding, #HTML entitys """

import unicodedata, html
from html.entities import html5


#Unicode
def unicode_test(value):
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))
unicode_test('A')
unicode_test('$')
unicode_test('\u00a2')
unicode_test('\u2603')

place = 'café'
unicodedata.name('\u00e9')
unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE')
place = 'caf\u00e9'
u_umlaut = '\N{LATIN SMALL LETTER E WITH ACUTE}'
drink = 'Gew' + u_umlaut + 'rztraminer'
print('Now I can finally have my', drink, 'in a', place)

len('$') == len('\U0001f47b')
chr(8134)
ord('ῆ')


#encoding and decoding
snowman = '\u2603'
len(snowman)  # 1
ds = snowman.encode('utf-8')
len(ds)  # 3
snowman.encode('ascii','ignore') 
snowman.encode('ascii','replace')
snowman.encode('ascii','backslashreplace')
snowman.encode('ascii','xmlcharrefreplace')

place = 'caf\u00e9'
place_bytes = place.encode('utf-8')
place_bytes
type(place_bytes)
place2 = place_bytes.decode('utf-8')
place2
place4 = place_bytes.decode('latin-1')
place4
place5 = place_bytes.decode('windows-1252')
place5


#HTML entitys
html.unescape('&egrave;')
html.unescape('&#233;')
html.unescape('&#xe9;')
html5['egrave']
html5['egrave;']

char = '\u00e9'
dec_value = ord(char)
html.entities.codepoint2name[dec_value]
byte_value = place.encode('ascii', 'xmlcharrefreplace')
byte_value
byte_value.decode()

eacute1 = 'é' 
eacute2 = '\u00e9'
eacute3 = '\N{LATIN SMALL LETTER E WITH ACUTE}'
eacute4 = chr(233)
eacute5 = chr(0xe9)
eacute1, eacute2, eacute3, eacute4, eacute5
eacute1 == eacute2== eacute3==eacute4==eacute5  # TRUE
unicodedata.name(eacute1)
ord(eacute1)
0xe9
eacute_combined1 = 'e\u0301'
eacute_combined2 = 'e\N{COMBINING ACUTE ACCENT}'
eacute_combined3 = 'e' + '\u0301'
eacute_combined1, eacute_combined2, eacute_combined3
eacute_combined3 == eacute_combined2 == eacute_combined1
len(eacute_combined1) # 2
#BUT!!!!
eacute1 == eacute_combined1
eacute_normalized = unicodedata.normalize('NFC', eacute_combined1)
len(eacute_normalized)
eacute_normalized == eacute1
unicodedata.name(eacute_normalized)