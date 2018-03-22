from inlist import makeWordList, in_bisect

def interLock(wordList, word):
    evens = word[::2]
    odds = word[1::2]
    return in_bisect(wordList, evens) and in_bisect(wordList, odds)

if __name__ == '__main__':
    wordList = makeWordList()
    for word in wordList:
        if interLock(wordList, word):
            print word, word[::2], word[1::2]
