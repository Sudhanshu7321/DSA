def countMin(s):
    def ispal(s):
        return s == s[::-1]

    if ispal(s):
        return 0

    n = len(s)
    for i in range(n):
        if ispal(s[i:]):
            return i

print(countMin('abcd'))
b
