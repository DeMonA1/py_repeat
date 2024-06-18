import dbm


db = dbm.open('definition', 'c')
db['mustard'] = 'yellow'
db['ketchup'] = 'red'
db['pesto'] = 'green'
len(db)
db['pesto']
db.close()
db = dbm.open('definition','r')
db['mustard']


