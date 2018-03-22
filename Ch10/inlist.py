
def in_bisect(wordList, word):
    if len(wordList) == 0:
        return False
    i = len(wordList) // 2
    if word == wordList[i]:
        return True
    elif word < wordList[i]:
        return in_bisect(wordList[:i], word)
    else:
        return in_bisect(wordList[i+1:], word)

def makeWordList():
    wordList = []
    fd = open('words.txt')
    for line in fd:
        word = line.strip()
        wordList.append(word)
    return wordList

if __name__ == '__main__':
    wordList = makeWordList()
    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_bisect(wordList, word))
