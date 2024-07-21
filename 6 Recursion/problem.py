def tiling(n):
    # base case 
    if n == 0 or n == 1:
        return 1
    #kaam
    # vertical choice 
    verticalTiles = tiling(n-1)
    
    # horizontal choice 
    horizontalTiles = tiling(n-2)
    
    totalways = verticalTiles + horizontalTiles
    return totalways

# def removeDuplicateInString(oldStr):
    
#     mapp = [0] * n
#     if i == len(oldStr)-1:
#         return  newStr
#     return

def friendPairing(n):
    if n == 1 or n == 2:
        return n
    
    return friendPairing(n-1)+ (n-1) * friendPairing(n-2)
 
def binaryString(n,lp,curr):
    if n == 0:
        return curr
    
    binaryString(n-1,0,curr.append(0))
    if lp == 0:
        binaryString(n-1,1,curr.append(1))
        
# print(tiling(4))

print(friendPairing(3))

print(binaryString(3,0,[]))