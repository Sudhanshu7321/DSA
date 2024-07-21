# class Solution:
    
#     @staticmethod
#     def bitAnd():
#         return (5 & 6)
    
#     def bitOr():
#         return (5|6)
    
#     def bitXor():
#         '''
#         0 ^ 0 = 0
#         0 ^ 1 = 1
#         1 ^ 0 = 1
#         1 ^ 1 = 1
#         '''
#         return (5^6)
    
#     def onesComplemenr():
#         return ~5
    
#     def leftShift():
#         return 5<<2 #  ans = a * 2^b = 20
    
#     def rightShift():
#         return 6>>1 # ans = a/2^b
    
#     def oddOrEven(n):
#         bitMask = 1
#         if n & bitMask == 0:
#             return "Even Number"
#         else:
#             return "Odd Number"
    
#     def getIthBit(number,place):
#         if number & (1<<place) == 0:
#             return 0
#         else:
#             return 1
        
#     def setIthBit(number,place):
#         return number | (1<<place)
    
#     def clearIthBit(number,place):
#         return number & ~(1<<place)
    
#     def clearLastIthBit(number,place):
#         return number & ~0 << place
#         # return number & -1 << place
        
#     def isPowerOfTwo(n):
#         if n <= 0:
#             return False
#         return (n & (n - 1)) == 0
    
#     def countSetBitInNumber(n):
#         count = 0
#         while n > 0:
            
#             if n & 1 != 0:
#                 count +=1
#             n = n >> 1    
            
#         return count
    
#     def addOne(n):
#         return -(~n)


        
        
        
# # print(Solution.bitAnd())    
# # print(Solution.bitOr())
# # print(Solution.bitXor())
# # print(Solution.onesComplemenr())
# # print(Solution.leftShift())
# # print(Solution.rightShift())

# # print(Solution.oddOrEven(10))
# # print(Solution.getIthBit(10,2))
        
# # print(Solution.setIthBit(10,2))
# # print(Solution.clearIthBit(10,1))

# # print(Solution.clearLastIthBit(15,2))
# # print(Solution.isPowerOfTwo(8))
# # print(Solution.countSetBitInNumber(17))
# print(Solution.addOne(17))
        
   
print(chr(97))        
        