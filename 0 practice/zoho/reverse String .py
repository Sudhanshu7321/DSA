# Input: 
s = ["h","e","l","l","o"]

class Solution:
    def solve(s):
       
        return s[len(s)-1::-1]          
    
print(f'Reverse String: {Solution.solve(s)}')    

