# def fin(arr):
#     s = set(arr)
#     for i in range(0,max(arr)+1):
#         if i not in s:
#             return i

def fin(arr):
    n = len(arr)
    ans = n
    for i in range(n):
        ans ^= arr[i]
        ans ^= i
        
    return ans    

arr = [3,0,1,4,5,2,7]   
print(f'Missing Number: {fin(arr)}')    