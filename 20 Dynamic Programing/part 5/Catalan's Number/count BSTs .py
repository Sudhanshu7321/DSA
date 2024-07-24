def numTrees(n):
# Catalan Number
    tab = [0]*(n+1)
    tab[0],tab[1] = 1, 1
    for i in range(2,n+1):
        for j in range(0,i):
            tab[i] += tab[j] * tab[i-j-1]
    return tab[n]   


n = 5
print(numTrees(n))