def break_words(stuff):
    #this func wil break words up
    words = stuff.split(' ')
    return words

def sort_words(words):
    #sort the sort_words
    return sorted(words)

def print_first_word(word):
    word = word.pop(0)
    print word

def print_last_word(words):
    word = words.pop(-1)
    print word

def sort_sentance(sentance):
    words = break_words(sentance)
    return sort_sentance(words)

def print_firs_and_last(sentance):
    words = break_words(sentance)
    print_first_word(words)
    print_last_word(words)

def print_firs_and_last_sorted(sentance):
    words= sort_sentance(sentance)
    print_first_word(word)
    print_last_word(word)
