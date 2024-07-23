def UnboundedKnapsack(values, weights, w):
    
    n = len(weights)
    
    # create table
    tab = []
    for _ in range(n+1):
        arr = [0] * (w+1)
        tab.append(arr)
    # tab = [[0 for _ in range(w + 1)] for _ in range(n + 1)]

    # Base Case 
    for i in range(n+1):
        tab[i][0] = 0
    for i in range(w+1):
        tab[0][i] = 0

    # after table look like 
    # [0,  0,  0,  0,  0,  0,  0,  0] 
    # [0, -1, -1, -1, -1, -1, -1, -1] 
    # [0, -1, -1, -1, -1, -1, -1, -1] 
    # [0, -1, -1, -1, -1, -1, -1, -1] 
    # [0, -1, -1, -1, -1, -1, -1, -1]
    # [0, -1, -1, -1, -1, -1, -1, -1]
         
                
    for i in range(1,n+1):
        v = values[i-1]
        weight = weights[i-1]
        for j in range(1,w+1):
            if weight <= j:
                tab[i][j] = max((v + tab[i][j-weight]) , (tab[i-1][j]))
            else:
                tab[i][j] = tab[i-1][j]    
    return tab[n][w]  
    

        
values = [15,14,10,45,30]
weights = [2,5,1,3,4]
w = 7


print(f'Maximum Profit in Unbounded Knapsack is: {UnboundedKnapsack(values,weights,w)}')
# output = 100