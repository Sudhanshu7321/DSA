def valid(s):
    close = [')','}',']']
    stack = []
    map = {
        ')' : '(',
        '}':'{',
        ']':'['
    }
    
    if not s or len(s) == 1 or s[0] in close:
        return False
    else:
        stack.append(s[0])
    
    for i in range(1,len(s)):
        
        if stack[-1] == map[s[i]]:
            stack.pop()
    if not stack:         
        return True
    else:
        return False
    
s='{{{[[]]}}}'
print(valid(s))