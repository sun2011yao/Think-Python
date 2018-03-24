def signature(word):
    t = list(word)
    t.sort()
    res = ''.join(t)
    return res

def allAnagrams(filename):
    d = {}
    fd = open(filename)
    for line in fd:
        word = line.strip().lower()
        t = signature(word)
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d
def printAnagramSets(d):
    for k in d.values():
        if len(k) > 1:
            print len(k), k


if __name__ == '__main__':
    anagramMap = allAnagrams('words.txt')
    printAnagramSets(anagramMap)