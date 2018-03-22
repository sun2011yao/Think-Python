def isPalindrome(i, start, length):
    s = str(i)[start: start + length]
    return s[::-1] == s

def check(i):
    return (isPalindrome(i, 2, 4) and isPalindrome(i + 1, 1, 5) \
            and isPalindrome(i + 2, 1, 4) and isPalindrome(i + 3, 0, 6))

def checkAll():
    i = 100000
    while (i <= 999996):
        if check(i):
            print i
        i += 1
    
checkAll()

