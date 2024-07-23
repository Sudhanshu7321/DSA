# recursion 
def knapsack(weights,values,w,n):
    # Base Case 
    if n== 0 or w == 0:
        return 0
    
    if weights[n] <= w:
        # include
        ans1 = values[n] + knapsack(weights, values, (w-weights[n]), (n-1))
        # exclude
        ans2 = knapsack(weights, values, w, (n-1))
        return max(ans1,ans2)
    else:
        return knapsack(weights, values, w, (n-1))
    
# memozation
def knapsackMem(weights,values,w,n,mem):
    if n == 0 or w == 0:
        return 0
    
    if mem[n][w] != None:
        return mem[n][w]
    
    if weights[n] <= w:
        # include
        val1 = values[n] + knapsackMem(weights,values,(w-weights[n]),n-1,mem)

        # exclude
        val2 = knapsackMem(weights,values,w,n-1,mem)
        mem[n][w] = max(val1,val2)
        return mem[n][w]
    
    else:
        mem[n][w] = knapsackMem(weights,values,w,n-1,mem)
        return mem[n][w]
    
# tabulation 

# wrong code 
def knapsackTab(weights,values,wt,n,tab):
    
    # Base case 
    for i in range(wt+1):
        tab[0][i] = 0 
    for i in range(len(weights)+1):
        tab[i][0] = 0   

    for i in range(1,n+1):
        for j in range(1,wt+1):
            v = values[i-1]
            w = weights[i-1]
            # valid
            if w <= j:
                val1 = v + tab[i-1][j-w]
                val2 = tab[i-1][j]
                tab[i][j] = max(val1,val2)
            else:
                tab[i][j] = tab[i-1][j]   
                
    return tab[n][wt] 
 
              
        
# Inputs     
w = 7    
weights = [2,5,1,3,4,2]    
values = [15,14,10,45,30,50]
values = [15,14,10,45,30]
weights = [2,5,1,3,4]
w = 7
# recursion 
ansRec = knapsack(weights,values,w,len(weights)-1)
print(f'MAximum weight : {ansRec}')

# memozation
mem = []
for i in range(0,len(weights)+1):
    mem.append([])
    for j in range(0,w+1):
        mem[i].append(None)
    
ansMem = knapsackMem(weights,values,w,len(weights)-1,mem)
print(f'MAximum weight : {ansMem}')

# tabulation 
tab = []
for i in range(0,len(weights)+1):
    tab.append([])
    for j in range(0,w+1):
        tab[i].append(0)
        
ansTab = knapsackTab(weights,values,w,len(weights),tab)
print(f'MAximum weight : {ansTab}')

# [[0,   0,    0,   0,    0,     0,    0,    0 ], 
#  [0, None, None, None, None, None, None, None], 
#  [0, None, None, None, None, None, None, None], 
#  [0, None, None, None, None, None, None, None], 
#  [0, None, None, None, None, None, None, None], 
#  [0, None, None, None, None, None, None, None], 
#  [0, None, None, None, None, None, None, None]]