# Given 2 string s1 and s2 , return minimum number of operation requires to convert s1 to s2.
def editDistance(s1, s2):
    n = len(s1)
    m = len(s2)
    
    tab = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(n+1):
        tab[i][0] = i
        
    for i in range(m+1):
        tab[0][i] = i
    # [0, 1, 2, 3, 4], 
    # [1, 0, 0, 0, 0], 
    # [2, 0, 0, 0, 0], 
    # [3, 0, 0, 0, 0], 
    # [4, 0, 0, 0, 0]  
    
      
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1] == s2[j-1]:
                tab[i][j] = tab[i-1][j-1]
            else:
                tab[i][j] = min(tab[i][j-1], tab[i-1][j], tab[i-1][j-1]) + 1
                        # = min(left , up, diagonal) + 1
    return tab[n][m]                 
            
s1 = 'intention'
s2 = 'execution'

s1 = 'golu'
s2 = 'gold'

print(editDistance(s1, s2))