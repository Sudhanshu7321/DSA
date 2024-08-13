# solved by using sliding window 


def solution(s,maxLetters,minSize,maxSize):
    
    fre = {}
    for i in range(len(s)-minSize+1):
        subString = s[i:i+minSize]
        if len(set(subString)) <= maxLetters:
            fre[subString] = fre.get(subString,0)+1
            
    # fre = dict(sorted(fre.items() ,key= lambda x:x[1],reverse=True))
    
    for d in fre:
        return fre[d]

s = "aaaaacbc"
maxLetters = 2
minSize = 4
maxSize = 6

print(solution(s,maxLetters,minSize,maxSize))