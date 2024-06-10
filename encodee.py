
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