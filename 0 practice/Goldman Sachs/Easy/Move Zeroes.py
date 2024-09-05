class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroPointer = -1
     

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroPointer = i
                break
        if zeroPointer != -1:
            for i in range(zeroPointer+1,len(nums)):
                if nums[i] != 0:
                   nums[i],nums[zeroPointer] = nums[zeroPointer],nums[i]
                   zeroPointer += 1
    
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]