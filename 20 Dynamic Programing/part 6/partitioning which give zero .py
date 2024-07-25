# write a programm which can partion the array in a way that difference give 0 return True other wise false

def pz(arr):
    n = len(arr)
    s = sum(arr)
    w = s//2
    
    tab = [[0 for _ in range(w+1)] for _ in range(n+1)]
    
    for i in range(1,n+1):
        v = arr[i-1]
        for j in range(1,w+1):
            if v <= j:
                tab[i][j] = max(v + tab[i-1][j-v], tab[i-1][j])
            else:
                tab[i][j] = tab[i-1][j]
        sum1 = tab[n][w]
        sum2 = s - sum1
        return sum1 == sum2            
    
    
arr = [1,2,3] #True
# arr = [1,2,3,4,5] #False
# arr = [0,0] #True


print(pz(arr))