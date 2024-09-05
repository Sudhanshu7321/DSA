
def solve1(s):
    dic = {}
    
    for i in s:
        dic[i] = dic.get(i,0)+1
    
    for i in s:
        if dic[i] ==  1:
            return s.index(i)
    return -1         
   
def solve2(s):
    
    alpha = [0]*26
    
    for i in s:
        alpha[ord(i) - ord('a')] += 1
        
    for i in s:
        if (alpha[ord(i) - ord('a')]) == 1:
            return  s.index(i)
           
    return -1


s = "aabb"
s = "loveleetcode"
print(solve2(s))