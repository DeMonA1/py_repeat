def edit_word(words, func):
    for word in words:
        print(func(word))
words = ['letted','dasd','hello']
edit_word(words, lambda word: word.capitalize() + '!')

# the decorator
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

def add_ints(a,b):
    return a + b

add_ints(3,5)
cooler_add_ints = document_it(add_ints)     #create the decorator
cooler_add_ints(3,5)

#test 1
@document_it
def add_ints(a,b):
    return a + b
add_ints(3,5)

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

#test with the result
@document_it
@square_it
def add_ints(a, b):
    return a + b
add_ints(3,5)

@square_it
@document_it
def add_ints(a, b):
    return a + b
add_ints(3,5)
#recursion#recursion#recursion#recursion#recursion#recursion
def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            for subitem in flatten(item):
                yield subitem
        else:
            yield item
lol = [1,2, [3,4,5], [6,[7,8,9], []]]
list(flatten(lol))

def flatten1(lol):
    for item in lol:
        if isinstance(item, list):
            yield from flatten1(item)
        else:
            yield item
list(flatten1(lol))

def deco(func):
    def new_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_func

#a simple generator
@deco
def foo():
    def get_odds():
        for i in range(10):
            if i % 2 > 0:
                yield i
    count = 0           
    for i in get_odds():
        count += 1
        if count == 3:
            print(i)
            break
    return get_odds()
foo()

#an exception
class OopsException(BaseException):
    pass

def foo1():
    l = {1:'asd',2:'vvv'}
    try:
        raise OopsException()
    except:
        print('Caught an oops')

foo1()

def test(func):
    def new_era(*args, **kwargs):
        print('start')
        res = func(*args, **kwargs)
        print('end')
        return res
    return new_era
@test
def tera(l):
    print(l)

tera('das')
