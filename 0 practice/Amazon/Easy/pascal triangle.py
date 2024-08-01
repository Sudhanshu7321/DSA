# return  pascal triangle n row

def pascalTriangle(n):
    
    triangle = [0] * (n+1 )
    triangle[0] = 1
    
    for i in range(1,n+1):
        for j in range(i,0,-1):
            triangle[j] = triangle[j] + triangle[j-1]
    return triangle

n = 8

print(pascalTriangle(n))        