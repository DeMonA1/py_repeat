"""#re"""

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