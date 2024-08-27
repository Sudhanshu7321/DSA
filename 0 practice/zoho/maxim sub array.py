nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]

class Solution:
    def solve(arr):
        
        sum = 0
        res = []
        maxSum = arr[0]
        for n in arr:
            if sum < 0:
                sum = 0
            
            sum += n
            maxSum = max(maxSum,sum)
        return maxSum            
    
print(f'Maximun Sum: {Solution.solve(nums)}')    

