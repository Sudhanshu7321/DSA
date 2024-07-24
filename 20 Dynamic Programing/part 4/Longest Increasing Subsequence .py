def lis(arr):
    
    unickArr = sorted(list(set(arr)))
    m = len(arr)
    n = len(unickArr)
    
    tab = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if arr[i-1] != unickArr[j-1]:
                tab[i][j] = max(tab[i-1][j], tab[i][j-1])
            else:
                tab[i][j] = 1 + tab[i-1][j-1]  
    return tab[m][n]              
    
    

arr = [50,3,10,7,40,80]

print(f'Longest Increasing Subsequence : {lis(arr)}')