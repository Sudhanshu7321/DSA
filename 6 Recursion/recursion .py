    
def decPrint(n):
    
    if n == 1 :
        print(n)
        return 
    
    print(n,end=" ")
    decPrint(n-1)
    
def incPrint(n):
    
    if n == 1 :
        print(n,end=" ")
        return 
    
    incPrint(n-1)
    print(n,end=" ")
    
def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n-1)

def sumOfN(n):
    if n == 1:
        return 1
    return n + sumOfN(n-1)

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    # fibn = fib(n-1) + fib(n-2)
    return fibonacci(n-1) + fibonacci(n-2)

def isSorted(arr,i):
    if i == len(arr)-1:
        return True
    
    if arr[i] > arr[i+1]:
        return False
    
    return isSorted(arr,i+1)
        
def firstOccurence(arr,i,key):
    if i == len(arr)-1:
        return -1
    
    if arr[i] == key:
        return i
    
    return firstOccurence(arr,i+1,key)

def lastOccurence(arr,i,key):
    if i < 0:
        return -1
    
    if arr[i] == key:
        return i
    
    return lastOccurence(arr,i-1,key)

def pow(x,n):
    if n == 1:
        return x
    return x * pow(x,n-1)

def optimizedPow(x,n):
    if n == 0:
        return 1
    halfPow = optimizedPow(x,n//2)
    halfpower = halfPow * halfPow
    
    if n % 2 != 0:
        halfpower = x * halfpower
    
    return halfpower    

# decPrint(10)    
# incPrint(10)
# print(factorial(5))
# print(sumOfN(100))
# print(fibonacci(20))
# print(isSorted([1,2,3,4,5],0))

# arr = [8,3,6,9,5,10,10,2,5,3]
# key = 10
# print(lastOccurence(arr,len(arr)-1,key))

print(optimizedPow(2,10))
