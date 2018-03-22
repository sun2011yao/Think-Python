""" 
think python 2nd
exercise 9-7

"""
def isTripleDouble(word):
    i = 0
    count = 0
    while i < len(word) - 1 :
        if word[i] == word[i+1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            i += 1
            count = 0
    return False

def findTripleDouble():
    fd = open('words.txt')
    for line in fd:
        word = line.strip()
        if isTripleDouble(word):
            print word

print('Here are all the words in the list that have')
print('three consecutive double letters.')
findTripleDouble()
print('')