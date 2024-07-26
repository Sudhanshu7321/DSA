# Merge n1 and n2 initi a single array sorted in non-decreasing order.
# return n1 

def mergeArray(n1,n2,n,m):
    p1, p2, i = (n-1), (m-1), ((m+n)-1)
    
    while p1 >= 0 and p2 >= 0:
        
        if n1[p1] <= n2[p2]:
            n1[i] = n2[p2]
            p2 -= 1
        else:
            n1[i] = n1[p1]
            p1 -= 1
            
        i -= 1
        
    while p2 >= 0:
        n1[i] = n2[p2]
        i-= 1
        p2 -= 1
    return n1    
                    

n = 3
m = 5
n1 = [1,2,3,0,0,0,0,0]
n2 = [2,5,6,7,8]

print(mergeArray(n1,n2,n,m))