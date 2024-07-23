def coinChange(coins,sum):
    n = len(coins)
     
    #  create table
    tab = [[0 for j in range(sum+1)] for i in range(n+1)]
    
    # fill 0^th col with 1
    for i in range(n+1):
        tab[i][0] = 1
    
    # fill table
    for i in range(1,n+1):
        for j in range(1,sum+1):
            coin = coins[i-1]
            if coin <= j:
                tab[i][j] = tab[i][j-coin] + tab[i-1][j]
            else:
                tab[i][j] = tab[i-1][j]        
    return tab[n][sum]

# Input 1
Coins = [1,2,3]
sum = 4

# Input 2
Coins = [2,5,3,6]
sum = 10

print(coinChange(Coins,sum))