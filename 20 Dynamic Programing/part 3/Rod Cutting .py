def rodCut(lengths,prices,rodLength):
    
    n = len(lengths)
    tab = [[0 for _ in range(rodLength+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        price = prices[i-1]
        length = lengths[i-1]
            
        for j in range(rodLength+1):
            
            if length <= j:
                tab[i][j] = max(price+tab[i][j-length] , tab[i-1][j])
            else:
                tab[i][j] = tab[i-1][j]
    return tab[n][rodLength]        

lengths = [1,2,3,4,5,6,7,8]
prices = [1,5,8,9,10,17,17,20]
rodLength = 8

print(f'Maximum : {rodCut(lengths,prices,rodLength)}')