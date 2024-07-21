def q1(nums):
    s = sorted(nums)
    if nums == s:
        return True
    elif nums == sorted(nums,reverse=True):
        return True
    
    return False

nums = [6,5,4,4]
# nums = [1,2,2,3]
nums = [1,3,2]
# print(q1(nums))

def q2(nums):
    res = []
    dict = {}
    for i in range(len(nums)):
         
        if nums[i] not in dict:    
            dict[nums[i]] = 1
        else:
            dict[nums[i]] += 1
            
        if dict.get(nums[i]) == 1 and nums[i]+1 not in nums or nums[i]-1 not in nums:
            res.append(nums[i])    
    
        
    # for i in range(len(nums)):
    #     if :
    #         res.append(nums[i])
    
    return res

nums = [10,6,5,8]
nums = [1,3,5,3]
print(q2(nums))    


def beautiful_array(n):
    def construct_beautiful_array(nums):
        if len(nums) <= 2:
            return nums
        odd = construct_beautiful_array(nums[::2])
        even = construct_beautiful_array(nums[1::2])
        return odd + even

    nums = list(range(1, n + 1))
    return construct_beautiful_array(nums)

n = 4
print(beautiful_array(n))  # Sample Output: [2, 1, 4, 3]

n = 5
print(beautiful_array(n))  # Sample Output: [3, 1, 2, 5, 4]
    
        
            