class Solution:
    
    @staticmethod
    # Brute Force method
    # time Complixity : O(n^3) 

    def maxSubArrSum(arr):
        n = len(arr)+1
        maxSum = 0
        for i in range(n):
            
            for j in range(i+1,n):
                currSum = 0
                
                for k in range(i,j):
                    currSum += arr[k]
                maxSum = max(currSum,maxSum) 
        
        return maxSum
    
    '''
    Optimal Solution
    '''
    
    # Kadane's Algorithm
    # time Complixity : O(n) 
    def maxSumArray(arr):
        maxSum , currentSum = 0,0
        for i in range(len(arr)):
            currentSum += arr[i]
            if currentSum < 0:
                currentSum = 0
            maxSum = max(currentSum,maxSum)
        
        return maxSum        
            
            
    
arr = [2,4,6,8,10]
arr = [1,-2,6,-1,3]
arr = [-2,-3,4,-1,-2,1,5,-3]

print(f'Maximum sum of sub array : {Solution.maxSubArrSum(arr)}')   
print(f'Maximum sum of sub array using Kadanes algofy : {Solution.maxSumArray(arr)}')                           