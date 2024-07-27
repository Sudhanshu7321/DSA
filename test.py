import heapq

nums = [3,2,3,1,2,4,5,5,6]
k = 4
nums = list(set(nums))
heapq.heapify(nums)
print(nums)
print(nums[-(k-1)])
# abs(heapq.heappop(nums,k))