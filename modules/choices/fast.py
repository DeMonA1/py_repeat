from random import choice

places = ['McDonalds', 'KFC', 'Burger King', 'Taco Bell',
          'Wndys', 'Arbys', 'Pizza Hut']

def pick():
    """Return random fast food place"""
    return choice(places)