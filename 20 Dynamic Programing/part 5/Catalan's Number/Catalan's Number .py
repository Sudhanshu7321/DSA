# c(n) = c(0).c(n-1) + c(1).c(n-2) + c(2).c(n-3) ... c(n).c(0)

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

n = 5
print(f'Catalan Number for {n} is: {catalanNumber(n)}')
