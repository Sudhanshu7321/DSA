def pt(n):
    triangle = [0] * (n + 1)
    triangle[0] = 1

    for i in range(n):
        for j in range(i, 0, -1):
            triangle[j] = triangle[j] + triangle[j - 1]
        print(' '.join(map(str, triangle[:i + 1])))

pt(5)
