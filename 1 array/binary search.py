# Pseudo Code
'''
start = 0
end = n-1

while (start <= end)
 	
	find mid = (start+end)/2
 
	compare mid & key:
		
		mid == key #Found
		mid > key  #Left
		mid < key  #Right
'''
# Time Complaxity : O( log n )
class Solution:
    
    def binarySearch(arr,key):
        
        start, end= 0, len(arr)-1
        
        while start <= end:
            
            mid = (start + end)//2   
            if key == arr[mid]:
                return mid
            
            if arr[mid] > key:
                end = mid-1
            else:
                start = mid +1
        return -1        
                
            
arr = [2,4,6,10,12,14]
key = 14
print(f'{key} found at index: {Solution.binarySearch(arr,key)}')        