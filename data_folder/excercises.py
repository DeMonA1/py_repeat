import csv, sqlite3, sqlalchemy


#1
text = """author, book
J R R Tolkien, The Hobbit
Lynne Truss, "Eats, Shoots & Leaves" """

x = text.split('\n')
for i in range(len(x)):
    x[i] = [x[i]]

with open('books.csv', 'wt') as bo:
    csvout = csv.writer(bo)
    csvout.writerows(x)


#2
with open('books.csv', 'rt') as bo:
    book = csv.DictReader(bo)
    books = [i for i in book]
print(books)


#3
text1 = """title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992"""
x = text1.split('\n')
for i in range(len(x)):
    x[i] = [x[i]]
with open('books1.csv', 'wt', encoding='utf-8') as bo:
    writer = csv.writer(bo)
    writer.writerows(x)


#4
table = sqlite3.connect('books.db')
cur = table.cursor()
cur.execute("""CREATE TABLE books
            (title VARCHAR(1000) PRIMARY KEY,
            author VARCHAR(1000),
            year INT)""")


#5
ins = 'REPLACE INTO books(title, author, year) VALUES(?, ?, ?)'
with open('books1.csv', encoding='utf-8') as bp:
    reader = csv.reader(bp)
    data = [i for i in reader if i]
for i in data[1:]:
    b = i[0].split(',')
    cur.execute(ins, (b[0], b[1], b[2]))
table.commit()
cur.close()
table.close()
#cur.execute(f'INSERT INTO books VALUES({b[0]}, {b[1]}, {b[2]})')    


cur.execute('SELECT * FROM books ORDER BY year ASC')
rows = cur.fetchall()            
print(rows)



#6
engine = sqlalchemy.create_engine('sqlite:///C:\\Users\\Дима\\PycharmProjects\\py_repeat\\data_folder\\books.db')
with engine.connect() as connection:
    result = connection.execute(sqlalchemy.text('SELECT title FROM books ORDER BY title ASC'))
    print([i for i in result])#SELECT title FROM books ORDER BY title ASC