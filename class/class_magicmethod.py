"""Magic methods, #composition, #namedtuple, #dataclass"""


from collections import namedtuple
from dataclasses import dataclass


#Magic methods
class Word():
    def __init__(self, text):
        self.text = text
    #def equals(self, word2):
        #return self.text.lower() == word2.text.lower()
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
    def __str__(self) -> str:
        return self.text
    def __repr__(self) -> str:
        return f'Word("{self.text}")'
first = Word('ha')
second = Word('HA')
third = Word('eh')
#first.equals(second)
#first.equals(third)
first == second
first == third
first #using repr
print(first) # using str


#composition
class Bill():
    def __init__(self, description):
        self.description = description
    
class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a',self.bill.description, 'bill and a',
              self.tail.length, 'tail')
a_tail = Tail('long')
a_bill = Bill('wide orange')
duck = Duck(a_bill, a_tail)
duck.about()


##namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('Wide orange', 'long')
duck
duck.bill
duck.tail

parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)
duck2

duck3 = duck2._replace(tail='magnificent', bill='crushing')
duck3


#dataclass
@dataclass
class TeenyDataClass:
    name: str

teeny = TeenyDataClass('bitsy')
teeny.name

@dataclass
class AnimalClass:
    name: str
    habitat: str
    teeth: int = 0
snowman = AnimalClass('yeti', 'Himalayas', 46)
duck = AnimalClass(habitat='lake', name='duck')
snowman
duck