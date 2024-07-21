    # Bubble Sort 
    # time complexity: O(n^2)
    # Pseudo Code
'''
for 0 to n-1 
    for 0 to n-1-term
     
     if nums[i] > nums[i+1]
     swap
'''
class Solution:
    
    @staticmethod

    def bubbleSort(nums):
        n = len(nums)
        for i in range(0,n-1):
            for j in range(0,n-1-i):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        
        return nums
    
    # selection Sort
    # time complexity: O(n^2)
    def selectionSort(nums):
        n = len(nums)
        for i in range(0,n-1):
            minPOs = i
            for j in range(i+1,n):
                if nums[minPOs] > nums[j]:
                    minPOs = j
            
            nums[minPOs],nums[i] = nums[i],nums[minPOs]        
        return nums   

    # Counting Sort
    # time complexity: O(n^2)
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

nums = [2,3,6,4,8,5]
nums = [5,4,1,3,2]

print(Solution.countingSort(nums))                