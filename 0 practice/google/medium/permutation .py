def permutation(s, ans):
    res = []
    if len(s) == 0:
        res.append(ans)
        return res

    for i in range(len(s)):
        cur = s[i]
        newS = s[:i] + s[i+1:]
        res += permutation(newS, ans + cur)
    
    return res    

# Call the function and print the results
result = permutation('abc', '')
print(result)
      
