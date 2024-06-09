"""#setdefaul and defaultdict, #Counter, #deque, #itertools, #pprint"""


from collections import defaultdict, Counter, deque
import itertools, pprint, random

#setdefaul and defaultdict
periodic_table = {'Hydrogen':1, 'Helium': 2}
carbon = periodic_table.setdefault('Carbon', 12)
carbon
helium = periodic_table.setdefault('Helium',947)
helium
periodic_table
periodic_table = defaultdict(int)
periodic_table['Hydrogen'] = 1
periodic_table['Lead']
periodic_table

def no_idea():
    return 'Huh?'

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
bestiary['A']
bestiary['B']
bestiary['C']

bestiary = defaultdict(lambda: 'Huh?')
bestiary['E']

food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1
for food, count in food_counter.items():
    print(food, count)


#Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
breakfast_counter
#!!!
breakfast_counter.most_common()
breakfast_counter.most_common(1)
lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
lunch_counter
#!!!
breakfast_counter + lunch_counter
breakfast_counter - lunch_counter
lunch_counter - breakfast_counter
lunch_counter & breakfast_counter
lunch_counter | breakfast_counter


#OrderedDict - doesn't actual

#deque
def palindrom(word):
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True
palindrom('radar')
#or
def another_palindrom(word):
    return word == word[::-1]
another_palindrom('radar')


#itertools
for item in itertools.chain([1,2], ['a','b']):
    print(item) #1 2 a b

for item in itertools.cycle([1,2]):
    print(item)  #eternal cycle

for item in itertools.accumulate([1,2,3,4]):
    print(item)

for item in itertools.accumulate([1,2,3,4], lambda a,b: a * b):
    print(item)


#pprint
quotes = dict([('Moe', 'A wise guy, huh?'),
               ('Larry', 'Ow!'),
               ('Curly', 'yuk yuk!')
               ])
pprint.pprint(quotes)
print(quotes)


#random
random.choice([23,9,46,'dasdsad',0x123abc])
random.choice(range(100))

random.sample([23,9,46,'dasdsad',0x123abc], 3)
random.sample(('a','one','one-e','two'),2)
random.sample('alphabet',7)

random.randint(38,222)
random.randint(22,9090)

random.randrange(34,333)
random.randrange(38,111, 10)

random.random()
random.random()

