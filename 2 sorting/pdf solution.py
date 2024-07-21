class Solution:
    
    @staticmethod 
    def bubbleSort(nums):
        n = len(nums)
        for i in range(0,n-1):
            for j in range(0,n-1-i):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        return nums
    
    def selectionSort(nums):
        n = len(nums)
        for i in range(0,n-1):
            minPos = i
            for j in range(i+1,n):
                if nums[minPos] > nums[j]:
                    minPos = j            
            
            nums[minPos],nums[i] = nums[i],nums[minPos]      
        return nums
    
    def countingSort(nums):
        
        count = [0] * (max(nums)+1)
        
        for num in nums:
            count[num] += 1
        
        j = 0    
        for i in range(len(count)):
            while count[i] > 0:
                
                nums[j] = i
                j += 1
                count[i] -= 1  
        return nums   
    
nums = [5,4,1,3,2]

print(f'Bubble :{Solution.bubbleSort(nums)}')          
print(f'Selection :{Solution.bubbleSort(nums)}')          
print(f'Counting :{Solution.bubbleSort(nums)}')          
          
        
              