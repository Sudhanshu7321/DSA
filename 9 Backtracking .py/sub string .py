def findSubString1(s,ans,i):
    # Base case 
    if i == len(s):
        print(ans,end=', ')
        return
    
    # Recursion 
    # Yes Choice 
    findSubString1(s,ans+s[i], i+1)
    # No Choice 
    findSubString1(s,ans, i+1)
    
def findSubString2(s, ans, i):
    # Base case
    if i == len(s):
        return [ans]
    
    # Recursion
    # Yes Choice
    res1 = findSubString2(s, ans + s[i], i + 1)
    # No Choice
    res2 = findSubString2(s, ans, i + 1)
    
    # Combine results
    return res1 + res2

print(findSubString2('123', '', 0))

    