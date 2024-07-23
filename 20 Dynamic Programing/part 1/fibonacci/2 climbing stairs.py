# steps may 1 jump , 2 jump and 3 jump allow 

# memozation
def climbStairMem(n,mem = None):
    if n == 0:
        return 1
    if n == 1 or n == 2:
        return n
    
    if not mem:
        mem = {}
    
    if n in mem:
        return mem[n]           
    mem[n] = (climbStairMem(n-1,mem) +  climbStairMem(n-2,mem) + climbStairMem(n-3,mem))
    return mem[n] 

# tabulation
def climbStair(n):
    
    tab = [0] * (n+1)
    tab[0] = 1
    tab[1] = 1
    tab[2] = 2
    
    for i in range(3,n+1):
        
        tab[i] = tab[i-1] + tab[i-2] + tab[i-3]
        
    return tab[n]    

n = 5
print(f'For climb {n} stair you have: {climbStair(n)} ways.')
print(f'For climb {n} stair you have: {climbStairMem(n)} ways.')