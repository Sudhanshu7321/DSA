n = 3
def pascalsTriangle(n):
    if n == 0:
        return []

    t = [0]*n
    t[0] = 1
    for i in range(n):
        for j in range(i,0,-1):
            t[j] = t[j] + t[j-1]
    return t    
print(pascalsTriangle(n))        