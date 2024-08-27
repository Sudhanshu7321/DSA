# Input: 
s = "anagram"
t = "nagaraa"
import collections
class Solution:
    def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t): return False

        sCount = collections.Counter(s)
        tCount = collections.Counter(t)

        for c in sCount:
            if c not in tCount:
                return False
            if tCount[c] != sCount[c]:
                return False

        return True  
    
print(Solution.isAnagram(s,t))    

