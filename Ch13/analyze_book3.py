import random
from bisect import bisect
from analyze_book1 import process_file

def random_word(hist):
    words = []
    freqs = []
    total = 0
    for word in hist:
        total += hist[word]
        words.append(word)
        freqs.append(total)
    t = random.randint(0, total)
    index = bisect(freqs, t)
    return words[index]


if __name__ == '__main__':
    hist = process_file('emma.txt', skip_header=True)

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print random_word(hist),