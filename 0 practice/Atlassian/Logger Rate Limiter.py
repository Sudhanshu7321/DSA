def LRL(log):
    dic = {}
    res = []
    for i in range(len(log)):
        if log[i][1] not in dic:
            dic[log[i][1]] = log[i][0]
            res.append(True)
        else:
            if (log[i][0] - dic[log[i][1]]) == 10:
                res.append(True)
            else:
                res.append(False)
        dic[log[i][1]] = log[i][0]
    
    return res

# Test cases

log1 = [[1, 'foo'], [11, 'foo'], [21, 'foo'], [31, 'foo'], [41, 'foo']]
print(f"Log: {log1}, Output: {LRL(log1)}")  # Expected: [True, True, True, True, True]

log2 = [[1, 'foo'], [2, 'foo'], [12, 'foo'], [22, 'foo'], [32, 'foo']]
print(f"Log: {log2}, Output: {LRL(log2)}")  # Expected: [True, False, True, True, True]

log3 = [[1, 'foo'], [3, 'bar'], [11, 'foo'], [21, 'foo'], [25, 'bar']]
print(f"Log: {log3}, Output: {LRL(log3)}")  # Expected: [True, True, True, True, False]

log4 = [[5, 'foo'], [15, 'foo'], [25, 'foo'], [30, 'foo'], [40, 'foo']]
print(f"Log: {log4}, Output: {LRL(log4)}")  # Expected: [True, True, True, False, True]

log5 = [[1, 'a'], [2, 'b'], [3, 'c'], [12, 'a'], [22, 'a']]
print(f"Log: {log5}, Output: {LRL(log5)}")  # Expected: [True, True, True, True, True]                 