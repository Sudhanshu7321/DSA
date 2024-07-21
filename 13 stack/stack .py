def reverseString(s):
    stack = []
    for i in range(len(s)):
        stack.append(s[i])
    
    for i in range(len(stack)):
        print(stack.pop(),end='')
        
# reverseString('abc')        

def reverseAstack(stack):
    if not stack:
        return
    top = stack.pop()
    reverseAstack(stack)
    stack.insert(0,top)  
      
        
# s = [1,2,3,4]
# print(s)
# reverseAstack(s)  
# print(s)          

def stockSpan(stocks,span):
    stack = []
    span[0] = 1
    stack.append(0)
    for i in range(1,len(stocks)):
        currPrice = stocks[i]
        
        while  stack and currPrice >= stocks[stack[-1]]:
            stack.pop()
        
        if not stack:
            span[i] = i+1
        else:
            preHigh = stack[-1]   
            span[i] = i - preHigh    
         
        stack.append(i)    
            
stocks = [100,80,60,70,60,85,100]
span = [0] * len(stocks)
print(span)
stockSpan(stocks,span)
print(span)