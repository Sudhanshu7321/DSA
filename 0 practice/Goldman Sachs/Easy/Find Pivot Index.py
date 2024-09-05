class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

# first method
        # lsum , rsum = 0,0

        # for i in range(len(nums)):
        #     lsum = sum(nums[:i])
        #     rsum = sum(nums[i+1:])
        #     if lsum == rsum:
        #         return i
        # return -1        
# Second method

        totalSum = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            rightSum = totalSum - leftSum - nums[i]  # Calculate the right sum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]  # Update the left sum for the next iteration

        return -1