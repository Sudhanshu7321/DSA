def targateSum(numbers, sum, tab):
    n = len(numbers)
    for i in range(1,n+1):
        print("_"*8+" i = "+str(i))
        for j in range(1,sum+1):
            v = numbers[i-1]
            print(f'J = {j} V = {v}')
            if v <= j and tab[i-1][j-v] == True:
                tab[i][j] = True
            if tab[i-1][j] == True:   
                tab[i][j] = True
    for i in range(n+1):
        print(tab[i])        
    return tab[n][sum] 

# Inputs
numbers = [4,2,7,1,3]
sum = 10

numbers = [1,2,0]
sum = 4

n = len(numbers)
tab = [''] * (n+1)
for i in range(n+1):
    arr = [False]*(sum+1)
    tab[i] = arr

for i in range(n+1):
    tab[i][0] = True 

      
print(targateSum(numbers, sum, tab))

# [[True, False, False, False, False, False, False, False, False, False, False], 
#  [True, False, False, False, False, False, False, False, False, False, False], 
#  [True, False, False, False, False, False, False, False, False, False, False], 
#  [True, False, False, False, False, False, False, False, False, False, False], 
#  [True, False, False, False, False, False, False, False, False, False, False], 
#  [True, False, False, False, False, False, False, False, False, False, False]]