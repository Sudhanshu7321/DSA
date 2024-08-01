def gp(s, open, close, n, result):
    if open == n and close == n:
        result.append(s)
        return


    if open < n:
        gp(s + '(', open + 1, close, n, result) 
        
        
    if open > close:
        gp(s + ')', open, close + 1, n, result)
           

n = 3
result = []
gp('', 0, 0, n, result)
print("Final result:", result)
