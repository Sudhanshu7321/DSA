# def permutation(s,ans):
    
#     # Base Case 
#     if len(s) == 0:
#         print(ans)
#         return 
    
#     # recursion 
#     for i in range(len(s)):
        
#         curr = s[i]
#         newStr = s[:i] + s[i+1:]
#         permutation(newStr,ans+curr)
    
    
# permutation("abc",'')    

# def permutation(s, ans):
#     # Base Case 
#     if len(s) == 0:
#         return [ans]
    
#     # Collect results in a list
#     result = []
    
#     # Recursion 
#     for i in range(len(s)):
#         curr = s[i]
#         newStr = s[:i] + s[i+1:]
#         result.extend(permutation(newStr, ans + curr))
    
#     return result

# # Call the function and print the results
# result = permutation("abc", '')
# print(result)

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
      
