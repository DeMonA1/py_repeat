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

class Cat():
    pass