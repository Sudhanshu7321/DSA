class Solution:
    
    @staticmethod
    def pair(arr,n):
        
        result = []
        for i in range(n):
            for j in range(i+1,n):
                result.append([arr[i],arr[j]])
        return result
    
arr = [2,4,6,8,10]
n = len(arr)
print(Solution.pair(arr,n)) 
print(f'Total Numbers of pair : {n*(n-1)//2}') # sum of n-1 numbers formula        
                