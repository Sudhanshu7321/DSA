# //  Maximum profit after buying and selling stocks with transaction fees
# //  We have an array of positive integers containing the price of stocks and transaction fee, the
# //  task is to find the maximum profit and the difference of days on which you are getting the
# //  maximum profit.

def stock(arr,fee):
    n = len(arr)
    
    tab = [[0 for _ in range(fee+1)] for _ in range(n+1)]
    
    
    for i in range(1,n+1):
        tab[i][0] = arr[i-1]
    print(tab)
    for i in range(1,n+1):
        p = arr[i-1]
        for j in range(1,fee+1):
            if p <= j:
                tab[i][j] = max(p+tab[i-1][j-p],tab[i-1][j] )
            else:
                tab[i][j] = tab[i-1][j]
    return tab             
            
    

# //  Input: 
arr = [6, 1, 7, 2, 8, 4] 
transactionFee = 2
# //  Output: 81
# //  Input: 
arr = [7, 1, 5, 3, 6, 4] 
transactionFee = 1
# //  Output: 51
print(stock(arr,transactionFee))

[0, 0], 
[7, 0], 
[1, 0], 
[5, 0], 
[3, 0], 
[6, 0], 
[4, 0]