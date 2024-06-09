#propertys
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('insside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)
don = Duck('Donald')
don.get_name()
don.set_name('Donna')
don.get_name()
don.name
don.name = 'DONNNN'
don.name
don.get_name()

#second variant
class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('insside the setter')
        self.__name = input_name
fowl = Duck('Hoawrd')
fowl.name
fowl.name = 'Donald'
fowl.name


class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius
c = Circle(5)
c.radius
c.diameter
c.radius = 7
c.diameter


#attributes of a class
class Fruit():
    color = 'red'
blueberry = Fruit()
Fruit.color
blueberry.color
#but
blueberry.color = 'blue'
blueberry.color
Fruit.color
#and
Fruit.color = 'orange'
Fruit.color
blueberry.color
new_fruit = Fruit()
new_fruit.color

# @classmethod
class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")
easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()


#@staticmethod
class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')
CoyoteWeapon.commercial()


#duck typization
class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'
    
class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'
hunter = Quote('Epmer Fludd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())
hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunted1.who(), 'says:', hunted1.says())
hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunted2.who(), "says:", hunted2.says())

class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'
brook = BabblingBrook()

def who_says(obj):
    print(obj.who(), 'says', obj.says())
who_says(hunter)
who_says(hunted1)
who_says(hunted2)
who_says(brook)