import math
def arrangeCoins(n: int) -> int:
        # By analysing and question 
        # k <= sqarroot of (2n+0.25) − 0.5 
        return int(math.sqrt(2*n+0.25)-0.5)

coin = 5    
print(arrangeCoins(coin))    