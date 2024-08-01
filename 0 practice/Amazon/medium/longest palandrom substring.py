def ispalendrom(s):
    return s == ''.join(reversed(s))

def lps(s):
    rs = ''.join(reversed(s))
    n = len(s)
    tab = [['' for _ in range(n+1)] for _ in range(n+1)]
    ans = ''
    for i in  range(1,n+1):
        for j in range(1,n+1):
            if s[i-1] == rs[j-1]:
                newS = s[i-1] + tab[i-1][j-1] 
                tab[i][j]= newS
                if ispalendrom(newS):
                    if len(ans) < len(newS):
                        ans = newS
                    
            else:
                tab[i][j] = tab[i-1][j-1]  
    return ans              
                
                   
[['', '',  '', '', '', ''], 
 ['', '',  '', 'b', '', 'b'], 
 ['', '',  'a', '', 'ab', ''], 
 ['', '',  '', 'ba', '', 'bab'], 
 ['', '',  'a', '', 'aba', ''], 
 ['', 'd', '', 'a', '', 'aba']]

s = 'aacabdkacaa'
print(lps(s))