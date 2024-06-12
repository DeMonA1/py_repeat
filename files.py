import os,shutil

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