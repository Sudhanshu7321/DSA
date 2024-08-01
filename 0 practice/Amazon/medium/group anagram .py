def ga(strs):
    
    dic = {}
    for s in strs:
        sSort = ''.join(sorted(s))
        if sSort not in dic:
            dic[sSort] = []
        dic[sSort].append(s)    

        res = []
        for value in dic:
            res.append(dic[value])
    # return res
    return list(dic.values())
strs = ["eat","tea","tan","ate","nat","bat"]
# for i in dic:
print(ga(strs))