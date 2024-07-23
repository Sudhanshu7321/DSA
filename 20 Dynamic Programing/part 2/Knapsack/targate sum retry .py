def targateSum(nums,sum):
    n =len(nums)
    
    # create Table
    # [False, False, False, False, False] 
    # [False, False, False, False, False] 
    # [False, False, False, False, False] 
    # [False, False, False, False, False]
    tab = []
    for _ in range(n+1):
        arr = [False] * (sum+1)
        tab.append(arr)
    
    # Add Base Case 
    # [True, False, False, False, False]
    # [True, False, False, False, False] 
    # [True, False, False, False, False] 
    # [True, False, False, False, False]
    for i in range((n+1)):
        tab[i][0] = True    
    
    for i in range(1,(n+1)):
        for j in range(1,(sum+1)):
            v = nums[i-1]
            if v <= j and tab[i-1][j-v] == True:
                tab[i][j] = True
            if tab[i-1][j] == True:
                tab[i][j] = True        
        
    return tab[n][sum]
#   0      1       2       3      4
# 0 [True, False, False, False, False], 
# 1 [True, True,  False, False, False], 
# 2 [True, True,  True,  True,  False], 
# 3 [True, True,  True,  True,  True]

# Inputs
numbers = [4,2,7,1,3]
sum = 10

numbers = [1,2,3]
sum = 4

print(targateSum(numbers,sum))