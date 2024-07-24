# c(n) = c(0).c(n-1) + c(1).c(n-2) + c(2).c(n-3) ... c(n).c(0)

# memozation
def catalanNumber(n, mem=None):
    if n == 0 or n == 1:
        return 1

    if mem is None:
        mem = {}

    if n in mem:
        return mem[n]

    ans = 0
    for i in range(n):
        ans += catalanNumber(i, mem) * catalanNumber(n - i - 1, mem)

    mem[n] = ans
    return ans

# tabulation
def catalanNumberTab(n):
    tab = [0] * (n+1)
    tab[0], tab[1] = 1, 1
    
    for i in range(2,n+1):
        for j in range(0,i):
            tab[i] +=  tab[j] * tab[i-j-1]
    return tab[n]        
    
n = 5
print(f'Catalan Number for {n} is: {catalanNumber(n)}')
print(f'Catalan Number for {n} is: {catalanNumberTab(n)}')

