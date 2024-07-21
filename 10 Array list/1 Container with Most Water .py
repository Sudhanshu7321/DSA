# T.C : O(n^2) 
def maxContainerWater(heights):
    maxWater = 0
    n = len(heights)
    for i in range(0,n-1):
        for j in range(i+1,n):
            height = min(heights[i], heights[j])
            width = j - i
            maxWater = max(maxWater, height * width)   
    return maxWater


# T.C : O(n) 
def maxContainerWater2(heights):
    l , r = 0 ,len(heights)-1
    maxWater = 0
    while l <=r :
        width = r-l
        height = min(heights[r],heights[l])
        water = height * width
        maxWater = max(maxWater,water)
        
        if heights[l] < heights[r]:
            l+=1
        else:
            r -= 1
    return maxWater            
        
height = [1,8,6,2,5,4,8,3,7]
print(f'Ans is: {maxContainerWater2(height)}')        
            