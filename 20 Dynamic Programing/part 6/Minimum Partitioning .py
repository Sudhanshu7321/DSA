# Minimum Partitioning
# Minimum subset sum difference
# Partation subset

def mp(arr):
    n = len(arr)
    w = sum(arr)//2
    tab = [[0 for _ in range(w+1)] for _ in range(n+1)]
    
    for i in range(1,n+1):
        v = arr[i-1]
        for j in range(1,w+1):
            if v <= j:
                tab[i][j] = max(arr[i-1] + tab[i-1][j-v], tab[i-1][j])
            else:
                tab[i][j] = tab[i-1][j]
    set1 = tab[n][w]
    set2 = sum(arr) - set1
    return abs(set1 - set2)             
    

# Input 
arr = [1,6,11,15]
arr = [1, 2,3]
print(mp(arr))
# o/p = 1