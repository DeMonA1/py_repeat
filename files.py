import os,shutil, glob
from pathlib import Path

fout = open('oops.txt','wt')
print('Oops, I created a file.', file=fout)
fout.close()
poem =  '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''
len(poem)
fout = open('relativity', 'wt')
fout.write(poem)
fout.close()
fout = open('relativity', 'wt')
print(poem, file=fout, sep='', end='')
fout.close()

fout = open('relativity','wt')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset+chunk])
    offset += chunk
fout.close()

try:
    fout = open('relativity', 'xt')
    fout.write('stomp stomp stomp')
except FileExistsError:
    print('relativity already exists! That was a close one.')

fin = open('relativity', 'rt')
poem = fin.read()
fin.close()
len(poem)

poem = ''
fin = open('relativity', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment
fin.close()
len(poem)

poem = ''
fin = open('relativity', 'rt')
chunk = 100
while True:
    fragment = fin.readline(chunk)
    if not fragment:
        break
    poem += fragment
fin.close()
len(poem)

poem = ''
fin = open('relativity', 'rt')
for line in fin:
    poem += line
fin.close()
len(poem)

fin = open('relativity', 'rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')
for line in lines:
    print(line, end='')


bdata = bytes(range(0, 256))
len(bdata)
fout = open('bfile', 'wb')
fout.write(bdata)
fout.close()

fout = open('bfile','wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(bdata[offset:offset + chunk])
    offset += chunk
fout.close()

fin = open('bfile', 'rb')
bdata = fin.read()
len(bdata)
fin.close()

with open('relativity','wt') as fout:
    fout.write(poem)

fin = open('bfile', 'rb')
fin.tell()
fin.seek(255)
bdata = fin.read()
len(bdata)
bdata[0]


os.SEEK_SET
os.SEEK_CUR
os.SEEK_END
fin = open('bfile','rb')
fin.seek(-1,2)
fin.tell()
bdata = fin.read()
len(bdata)
bdata[0]

fin = open('bfile','rb')
fin.seek(254, 0)
fin.tell()
fin.seek(1,1)
fin.tell()
bdata = fin.read()
len(bdata)
bdata[0]



os.path.exists('oops.txt')
os.path.exists('./oops.txt')
os.path.exists('waffles')
os.path.exists('.')
os.path.exists('..')

name = 'oops.txt'
os.path.isfile(name)
os.path.isdir(name)
os.path.isdir('.')
os.path.isabs(name)
os.path.isabs('/b/b/b/b')
os.path.isabs('b/b/b/b')


shutil.copy('oops.txt', 'ohno.txt')
os.rename('ohno.txt', 'ohwell.txt')
os.link('oops.txt','yikex.txt')
os.path.isfile('yikex.txt') #TRUE
os.path.islink('yikex.txt')     #FALSE
os.symlink('oops.txt', 'jeepers.txt')
os.path.islink('jeepers.txt')
os.remove('oops.txt')
os.path.exists('oops.txt')



os.mkdir('poems')
os.path.exists('poems')
os.rmdir('poems')
os.path.exists('poems')

os.mkdir('poems')
os.listdir('poems')
os.mkdir('poems/mcintyre')
os.listdir('poems')
fout = open('poems/mcintyre/the_good_man', 'wt')
fout.write("""'Cheerful and happy was his mood,
He to the poor was kind and good,
And he oft' times did find them food,
Also supplies of coal and wood,
He never spake a word was rude,
And cheer'd those did o'er sorrows brood,
He passed away not understood,
Because no poet in his lays
Had penned a sonnet in his praise,
'Tis sad, but such is world's ways.
""")
fout.close()
os.listdir('poems/mcintyre')


os.chdir('poems')
os.listdir('.')
glob.glob('m*')
glob.glob('??')
glob.glob('m??????e')
glob.glob('[klm]*e')


os.path.abspath('oops.txt')
os.symlink('oops.txt', 'jeepers.txt')
os.path.islink('jeepers.txt')
os.path.realpath('jeepers.txt')
win_file = os.path.join('py_re', 'poems')
win_file = os.path.join(win_file, 'today')
win_file


file_path = Path('py_repeat') / 'poems'/ 'lll.txt'
file_path
print(file_path)
file_path.name
file_path.suffix
file_path.stem

glob.glob('*.txt')

os.chdir('..')
glob.glob('*.txt')

test1 = "This is a test of the emergency text system"
os.chdir('./py_repeat')
os.getcwd()
with open('testinh.txt', 'wt') as fe:
    fe.write(test1)
    print('close')
with open('testinh.txt', 'r') as fe:
    test2 = fe.read()
test1 == test2
import datetime, time
a = time.localtime()
time.strftime('%H:%M; %d:%m:%Y',a)