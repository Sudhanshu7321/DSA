class Solution:
    def isPowerOfThree(self, n: int) -> bool:

# optimal approach
        if n <= 0: return False
        while n%3 == 0:
            n= n//3

        return  n == 1    

# Not optimal Approach
        # if n < 0: return False
        # i = 0
        # val = 0
        # while val < n:
        #     val = pow(3,i)
        #     i += 1
        #     if val == n: return True

        # return False    
        
        