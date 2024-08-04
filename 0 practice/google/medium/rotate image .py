m1 = [[1,2,3],[4,5,6],[7,8,9]]
n = len(m1)
m2 = [[0 for _ in range(3)] for _ in range(n)]

# Tranpose of matrix
for i in range(n):
    for j in range(n):
        m2[i][j] = m1[j][i]

# reversed matrix    
for i in range(n):
    s, e = 0,n-1
    while s<e:
        m2[i][s], m2[i][e] = m2[i][e], m2[i][s]
        s +=  1
        e -=1
        
        
print(m2)        