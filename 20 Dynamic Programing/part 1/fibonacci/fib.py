# Memoziation (top to bottam)
def fibonacci(n, memo=None):
    if n == 0 or n == 1:
        return n
    
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]

    
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# tabulation  (bottam to up)

def fib(n):
    tab = [0]* (n+1)
    tab[0] = 0
    tab[1] = 1
    for i in range(2,n+1):
        tab[i] = tab[i-1] + tab[i-2]
    return tab[n] 
     
n = 6
print(f"Fibonacci number at position {n} is {fibonacci(n)}")
print(f"Fibonacci number at position {n} is {fib(n)}")
