#1
class Thing():
    pass
Thing()
example = Thing()
example

#2
class Thing2():
    pass
letters = 'abc'
print(letters)

#3
class Thing3():
    pass
letters = Thing3()
letters.text = 'xyz'
letters.text

#4
class Element():
    def __init__(self, name, symbol, number) -> None:
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return f'self.name, self.symbol, self.number'
ob = Element('Hydrogen', 'H', '1')
print(ob)
#5
dictionary = dict([['name','Hydrogen'], ['symbol', 'H'], ['number',1]])
hydrogen = Element(**dictionary)

#6
class Element():
    def __init__(self, name, symbol, number) -> None:
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number
dictionary = dict([['name','Hydrogen'], ['symbol', 'H'], ['number',1]])
hydrogen = Element(**dictionary)

#7
class Bear():
    def eats(self):
        print('berries')

class Rabbit():
    def eats(self):
        print('clover')

class Octothorpe():
    def eats(self):
        print('campers')
bear = Bear()
bear.eats()
rabbit = Rabbit()
rabbit.eats()
octo = Octothorpe()
octo.eats()

#8
class Laser():
    def does(self):
        print('disintegrate')

class Claw():
    def does(self):
        print('crush')

class SmartPhone():
    def does(self):
        print('ring')

class Robot():
    def __init__(self, laser, claw, phone):
        self.laser = laser
        self.claw = claw
        self.phone = phone
    def does(self):
        self.laser.does(),self.claw.does(),self.phone.does()
cl = Claw()
la = Laser()
pho = SmartPhone()
robo = Robot(la, cl, pho)
robo.does()
