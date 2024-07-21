def q1(l,r,k):
    arr = []
    for i in range(l,r+1):
        
        if (i % 2) != 0 :
            arr.append(i)
    arr = sorted(arr,reverse=True)    
    return arr[:k]

# Input 
l = -3
r = 3
k = 1 
# print(q1(l,r,k)) 

def q2(k):
    res = ''
    alphaArr = [0] * 27
    
    for i in range(1,len(alphaArr)):
        alphaArr[i] = chr(ord('a')+i-1)
    
    for i in range(1,len(alphaArr)):
        if k > i:
            while k >= i:
                res += alphaArr[i] 
                k -= i  
    print(f'Result is : {res}')    
             
k= 25          
q2(k)   

def q3(prices):
    maxPro = 0
    for i in range(len(prices)-1):
        max_val = max(prices[i+1:])
        if prices[i] < max_val:
            pro = max_val - prices[i]
            maxPro = max(pro, maxPro)
    print(maxPro)

prices = [7, 1, 5, 3, 6, 4]
q3(prices)

        