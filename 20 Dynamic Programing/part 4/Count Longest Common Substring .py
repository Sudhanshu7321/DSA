def lcs(text1, text2):
    ans = 0
    m = len(text1)
    n = len(text2)
    
    tab = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            
            if text1[i-1] == text2[j-1]:
                tab[i][j] = 1 + tab[i-1][j-1]
                ans = max(ans,tab[i][j])
    return ans            
# Inputs:
text1 = 'abcde'
text2 = 'abgce'
text1 = 'acdghr'
text2 = 'abcdgh'

print(f'Longest Common Substring : {lcs(text1,text2)}')