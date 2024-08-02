s = "pwwkew"

def ls(s):
    n = len(s)
    tab = [['' for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if s[i-1] == s[j-1] and s[i-1] not in tab[i-1][j-1]:
                tab[i][j] = tab[i-1][j-1] + s[i-1]
            else:
                tab[i][j] = tab[i-1][j-1]
    return (tab[n][n])   

print(ls(s))