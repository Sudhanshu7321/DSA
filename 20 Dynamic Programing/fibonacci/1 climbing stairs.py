# recursion 
def climbingStairRec(n):
    if n == 1 or n == 2:
        return n
    
    return climbingStairRec(n-1) + climbingStairRec(n-2)

# Memozation
def climbingStairMem(n,mem =None):
    if n == 1 or n == 2:
        return n
    
    if not mem:
        mem = {}
        
    if n in mem:
        return mem[n]
        
    mem[n] = climbingStairMem(n-1) + climbingStairMem(n-2)
    return mem[n]   
        
# tabulation

def climbingStairTab(n):
    
    if n == 1 or n == 2:
        return n
    
    tab = [0]*(n+1)
    tab[1] = 1
    tab[2] = 2
    
    for i in range(3,n+1):
        tab[i] = tab[i-1] + tab[i-2]
        
    return tab[5]
n = 5
print(f'No. of ways in {n} stair is: {climbingStairRec(n)}')
print(f'No. of ways in {n} stair is: {climbingStairMem(n)}')
print(f'No. of ways in {n} stair is: {climbingStairTab(n)}')
    