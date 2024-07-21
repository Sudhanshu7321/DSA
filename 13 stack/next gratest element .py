def nextGratest(nums):
    stack = []
    res = [0] * len(nums) 
    for i in range(len(nums)-1,-1,-1):
        
        while stack and stack[-1] <= nums[i]:
            stack.pop()
            
        if not stack:
            res[i] = -1
        else:
            res[i] = stack[-1]
        
        stack.append(nums[i])   
    return res    

nums= [6,8,0,1,3]        
print(nextGratest(nums))               