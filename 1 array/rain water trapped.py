class Solution:
    
    @staticmethod
    def rainWater(arr):
        if not arr:
            return 0

        rightMaxBoundary = [0] * len(arr)
        trapWater = 0
        
        # Calculate leftMaxBoundary
        leftMaxBoundary = [arr[0]]
        for i in range(1, len(arr)):
            leftMaxBoundary.append(max(leftMaxBoundary[i-1], arr[i]))
                
        # Calculate rightMaxBoundary
        rightMaxBoundary[-1] = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            rightMaxBoundary[i] = max(rightMaxBoundary[i+1], arr[i])
        
        # Calculate trapped water
        for k in range(len(arr)):
            height = arr[k]
            trapWater += min(leftMaxBoundary[k], rightMaxBoundary[k]) - height #(waterHeight - height) * width
            
        return trapWater    

arr = [4, 2, 0, 6, 3, 2, 5]
print(Solution.rainWater(arr))
