def pair(nums,targate):
    n = len(nums)
    breakAt = nums.index(max(nums))
    l,r = (breakAt+1)% n ,breakAt
    
    while l != r:
        sum = nums[l]+nums[r]
        if sum == targate:
            return True
        elif sum > targate:
            r = (n+r-1)%n
        else:
            l = (l+1)%n
    return False

nums = [11,15,6,8,9,10]
targate = 15
print(pair(nums,targate))               