def lcs(text1, text2):
    m = len(text1)
    n = len(text2)
    ans = ''
    tab = [['' for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if text1[i-1] == text2[j-1]:
                tab[i][j] = tab[i-1][j-1] + text1[i-1]
                if len(ans) < len(tab[i][j]):
                    ans = tab[i][j]
                    
    return ans                
                


# Inputs:
text1 = 'abcde'
text2 = 'abgce'

text1 = 'acdghsr'
text2 = 'abcdghss'

print(f'Longest Common Substring : {lcs(text1,text2)}')