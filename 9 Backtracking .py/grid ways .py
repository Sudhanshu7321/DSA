def gridWays(matrix,i,j,count):
    
    if i == len(matrix)-1 or j == len(matrix[0])-1: # Last Cell condition
        count += 1
        return count
    elif i == len(matrix) or j == len(matrix[0]): # Boundary Cross Condition
        return
    
    d =gridWays(matrix,i+1,j,count) # move Down
    r = gridWays(matrix,i,j+1,count) # move Right
    
    return d+r

def fac(n):
    if n == 0:
        return 1
    return n * fac(n-1)

def gridWays2(matrix):
    row, col = len(matrix)-1, len(matrix[0])-1
    return fac(row+col)// (fac(row)*fac(col))

n = 3
m = 3
matrix = [['X' for _ in range(n)] for _ in range(m)]
print(gridWays(matrix,0,0,0))
print(gridWays2(matrix))
    