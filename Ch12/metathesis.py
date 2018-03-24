import anagram_sets
def metathesisPairs(d):
    for anagrams in d.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 < word2 and wordDistance(word1, word2) == 2:
                    print word1, word2

def wordDistance(word1, word2):
    assert(len(word1) == len(word2))
    count = 0
    t = zip(word1, word2)
    for t1, t2 in t:
        if t1 != t2:
            count += 1
    return count

if __name__ == '__main__':
    sets = anagram_sets.allAnagrams('words.txt')
    metathesisPairs(sets)