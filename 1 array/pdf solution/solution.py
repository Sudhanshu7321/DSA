class Solution:
    
    @staticmethod
    
    def q1(arr):
        arr.sort()
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                return True
        return False 
    
    def q2(nums,target):
        if target not in nums:
            return -1
        else :
            return nums.index(target)
        
    def q3(prices):
        
        maxProfit = 0
        buyStock = max(prices)
        
        for i in range(len(prices)):
            if buyStock < prices[i]:
                profit = prices[i]-buyStock
                maxProfit = max(profit,maxProfit)
            else:
                buyStock = prices[i]
        
        return maxProfit            
  
    def q4(height):
        leftMaxBoundary = []
        rightMaxBoundary = [0] * len(height)
        trapWater = 0
        
        leftMaxBoundary.append( height[0])
        for i in range(1,len(height)):
            leftMaxBoundary.append(max(height[i],leftMaxBoundary[i-1]))
        
        rightMaxBoundary[-1] = height[-1]
        for i in range(len(height)-2,-1,-1):
            rightMaxBoundary[i] = max(rightMaxBoundary[i+1], height[i])
            
        for i in range(len(height)):
            trapWater += min(leftMaxBoundary[i],rightMaxBoundary[i]) - height[i]
        return trapWater                      
  
    def q5(nums):
        
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k] == 0:
                        val = sorted([nums[i],nums[j],nums[k]])
                        if val not in res:
                          res.append(val)   
                        
        return res
                       
# Question no 1       
nums = [1, 2, 3, 1]    
nums = [1, 2, 3, 4]
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# print(Solution.q1(nums))  

# Question no 2      
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
# print(Solution.q2(nums,target)) 

# Question no 3       
prices = [7, 1, 5, 3, 6, 4]
prices = [7, 6, 4, 3, 1]
# print(Solution.q3(prices))   

# Question no 4      
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [4, 2, 0, 3, 2, 5]
# print(Solution.q4(height)) 

# Question no 5      
nums = [-1, 0, 1, 2, -1, -4]
print(Solution.q5(nums)) 



  