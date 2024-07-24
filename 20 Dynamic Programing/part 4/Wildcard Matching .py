def wildCardMatching(s,p):
    n = len(s)
    m = len(p)
    
    tab = [[False for _ in range(m+1)] for _ in range(n+1)]
    tab[0][0] = True
    
    for i in range(1,n+1):
        tab[i][0] = False
    
    for i in range(1,m+1):
        if p[i-1] == '*':
            tab[0][i] = tab[0][i-1]
                     
    # [[True, True], 
    # [False, False], 
    # [False, False]]   
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            
            if s[i-1] == p[j-1] or p[j-1] == '?':
                tab[i][j] = tab[i-1][j-1]
            else:
                if tab[i-1][j] or tab[i][j-1]:
                    tab[i][j] = True
    return tab                    
                
            

s = 'aa'
p = ''

print(wildCardMatching(s,p))