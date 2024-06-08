class Cat():
    def __init__(self, name) -> None:
        self.name = name
furball = Cat('Grumpy')
# print('Our latest addition: ', furball.name)


class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm Yugo! Much like a Car, but more Yugo-ish.")
    def need_a_push(self):
        print('A little help here?')
# issubclass(Yugo,Car)
give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_yugo.need_a_push()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

#1
class Person():
    def __init__(self,name):
        self.name = name

class MDPerson(Person):
    def __init__(self, name):
        self.name = "doctor " + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"

person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
print(person.name)
print(doctor.name)
print(lawyer.name)

#2
class EmailPerson(Person):
    def __init__(self,email):
        super().__init__()
        self.email = email
bob = EmailPerson('Bob Frapples', 'bob@rapples.com')
bob.name
bob.email

#3
class Animal:
    def says(self):
        return 'I speak!'
    
class Horse(Animal):
    def says(self):
        return 'Neigh!'

class Donkey(Animal):
    def says(self):
        return 'Hee=haw!'

class Mule(Donkey,Horse):
    pass

class Hinny(Horse, Donkey):
    pass
Mule.mro()
Hinny.mro()
mule = Mule()
hinny = Hinny()
mule.says()
hinny.says()

#mixing
class PrettyMixin():
    def dump(self):
        import pprint
        pprint.pprint(vars(self))

class Thing(PrettyMixin):
    pass

t = Thing()
t.name = 'Nyarlathotep'
t.feature = 'ichor'
t.age = 'eldritch'
t.dump()

a_car = Car()
Car.exclaim(a_car)

#access
class Duck:
    def __init__(self, input_name):
        self.name = input_name
fowl = Duck('Daffy')
fowl.name
fowl.name = 'Daphne'
fowl.name

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('insside the setter')
        self.hidden_name = input_name
don = Duck('Donald')
don.get_name()
don.set_name('Donna')
don.get_name()