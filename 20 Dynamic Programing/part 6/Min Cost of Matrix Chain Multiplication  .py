# let matrix of : AxB , CxD
# Then Cost = A*B*D  (where B=C)
# And if multiply the above matrix then resultan matrix of size = AxD

# Recursion 
def mcm(arr, i , j):
    if i == j:
        return 0
    
    ans = float('inf')
    for k in range(i,j):
        
        cost1 = mcm(arr,i,k)
        cost2 = mcm(arr,k+1,j)
        cost3 = arr[i-1] * arr[k] * arr[j]
        final = cost1 + cost2 + cost3
        ans = min(ans, final)  
         
    return ans    

# Memozation
def mcm1(arr,i,j,mem):
    if i == j:
        return 0
    
    if mem[i][j]:
        return mem[i][j]
    
    ans = float('inf')
    
    for k in range(i,j):
        cost1 = mcm1(arr, i, k, mem)
        cost2 = mcm1(arr, k+1, j, mem)
        cost3 = arr[i-1] * arr[k] * arr[j]
        final = cost1 + cost2 + cost3
        ans  = min(ans,final)       
    mem[i][j] = ans
    return mem[i][j]
# Input 
arr = [1,2,3,4,3]
# recursion call 
print(f'Minimum cost of MCM : {mcm(arr,1,len(arr)-1)}')

# Memozation Call 
n = len(arr)
mem = [[None for _ in range(n)] for _ in range(n)]
print(f'Minimum cost of MCM : {mcm1(arr,1,n-1,mem)}')