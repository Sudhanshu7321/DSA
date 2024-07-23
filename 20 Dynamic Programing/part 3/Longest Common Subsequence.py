def lcs(text1,text2):
    m = len(text1)
    n = len(text2)
    
    tab = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            
            if text1[i-1] != text2[j-1]:
                tab[i][j] = max(tab[i-1][j] , tab[i][j-1]) #maX of tab UP,LEFT
            else:
                tab[i][j] = 1 + tab[i-1][j-1]
    return tab[m][n]            
text1 = "abcde"
text2 = "ace" 

print(f'Output : {lcs(text1,text2)}')