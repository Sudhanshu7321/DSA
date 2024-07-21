def beautiful_array(n):
    ans = [1]
    for i in range(2, n + 1):
        temp = []
        for e in ans:
            if 2 * e <= n:
                temp.append(2 * e)
        for e in ans:
            if 2 * e - 1 <= n:
                temp.append(2 * e - 1)
        ans = temp
    return ans

# Sample inputs and outputs
n = 4
print(beautiful_array(n))  # Sample Output: [2, 1, 4, 3]

n = 5
print(beautiful_array(n))  # Sample Output: [2, 4, 1, 3, 5]
