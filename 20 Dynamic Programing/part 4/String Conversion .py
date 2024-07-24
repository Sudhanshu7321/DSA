# Convert s1 to s2 with only Insert & deletion.
# And print Number of Insertion & Deletions

# s1 => s2 
#  /\
# /  delete = s2 - LSC 
# insert = s2 - LSC
# where LSC : Longest Common Subsequence

def stringConversion(s1,s2):
    n, m = len(s1), len(s2)
    
    tab = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(1,n+1):
        for j  in range(1,m+1):
            if s1[i-1] == s2[j-1]:
                tab[i][j] = 1 + tab[i-1][j-1]
            else:
                tab[i][j] = max(tab[i-1][j] , tab[i][j-1])
    
    d = len(s1) - tab[n][m]
    i = len(s2) - tab[n][m]
    return [d,i]                
    

s1 = 'pear'
s2 = 'sea'
s1 = 'abcdef'
s2 = 'aceg'

print(stringConversion(s1,s2))