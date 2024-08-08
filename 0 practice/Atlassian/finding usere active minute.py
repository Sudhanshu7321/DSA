logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5

dic = {}
val = []
res = [0]*len(logs)

for i in range(len(logs)):
    if logs[i][0] not in dic:
        dic[logs[i][0]] = set()   
    dic[logs[i][0]].add(logs[i][1])  
    
for l in dic:
    res[len(dic[l])-1] += 1   

print(res)    