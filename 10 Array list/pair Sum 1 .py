def pair(n,targate):
    l,r = 0 , len(n)-1
    
    while l <= r:
        sum =  (n[l]+n[r])
        if targate == sum:
            return True
        elif sum > targate:
            r -= 1
        else: 
            l += 1    
    return False

nums = [1,2,3,4,5,6]
targate = 5
print(pair(nums,targate))    
        