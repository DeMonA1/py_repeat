def edit_word(words, func):
    for word in words:
        print(func(word))
words = ['letted','dasd','hello']
edit_word(words, lambda word: word.capitalize() + '!')