class Solution:
    @staticmethod
    def stock(price):
        maxProfit = 0
        buyPrice = max(price)
        
        for i in range(len(price)):
            if buyPrice < price[i]:
                profit = price[i] - buyPrice
                maxProfit = max(profit,maxProfit)
            else:
                buyPrice = price[i]
                
        return maxProfit            
        


arr = [7,1,5,3,6,4]     
# arr =  [7, 6, 4, 3, 1]     

print(Solution.stock(arr))   