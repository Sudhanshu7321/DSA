nums = [10,9,2,5,3,7,101,18]
# nums = [0,1,0,3,2,3]
# nums = [7,7,7,7,7,7,7]
maxcount = 0
n = len(nums)
for i in range(n):
    c = 1
    for j in range(i+1,n-1):
        if nums[j] > nums[i]:
            c += 1
    maxcount = max(maxcount,c)    
print(maxcount)         