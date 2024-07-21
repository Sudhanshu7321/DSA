class Solution:
    
    @staticmethod
    
    def subarray(arr,n):
        result = []
        for i in range(n+1): # Start point
            
            for j in range(i+1,n+1): # End point
                tem = []
                
                for k in range(i,j):
                    tem.append(arr[k])
                result.append(tem)  
                
        return result  
    
    
    
arr = [2,4,6,8,10]
n = len(arr)

print(Solution.subarray(arr,n))
print(f'Total subarray : {n*(n+1)//2}')            
                    