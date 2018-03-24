
def readFile(filename):
    fd = open(filename)
    return fd.read()

def makeHistogram(s):
    res = {}
    for letter in s:
        res[letter] = res.get(letter, 0) + 1
    return res

def mostFrequent(s):
    hist = makeHistogram(s)
    t = []
    for letter, fre in hist.items():
        t.append((fre, letter))
    t.sort(reverse = True)
    res = []
    for fre, letter in t:
        res.append(letter)
    return res



if __name__ == '__main__':
    string = readFile('emma.txt')
    res = mostFrequent(string)
    for letter in res:
        print letter

