import random
import string

def process_file(filename, skip_header):
    fd = open(filename)
    if skip_header == True:
        skip_func(fd)
    hist = {}
    for line in fd:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1
    

def skip_func(fd):
    for line in fd:
        if line.startswith('*END*THE SMALL PRINT!'):
            break

def total_words(hist):
    return sum(hist.values())

def different_words(hist):
    return len(hist)

def most_common(hist):
    t = []
    for word, fre in hist.items():
        t.append((fre, word))
    t.sort(reverse = True)
    return t

def subtract(set1, set2):
    diff = []
    for k in set1:
        if k not in set2:
            diff.append(k)
    return diff

def random_word(hist):
    t = []
    for word, fre in hist.items():
        t.extend([word]*fre)
    return random.choice(t)

if __name__ == '__main__':

    hist = process_file('emma.txt', skip_header=True)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:20]:
        print word, '\t', freq
    words = process_file('words.txt', skip_header=False)
    diff = subtract(hist, words)
    print("The words in the book that aren't in the word list are:")
    for word in diff:
        print word,
    
    print("\n\nHere are some random words from the book")
    for i in range(100):
        print random_word(hist),