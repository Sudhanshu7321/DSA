def q2(s):
    stack = []
    sList = list(map(str, s.split("/")))
    for i in sList:
        
        if '..' == i:
            stack.pop()
        elif '' != i:
            stack.append(i)
                
    return '/'+'/'.join(stack)

s = '/apnacollege/'
print(q2(s))  # Output: ['', 'apnacollege', '']
