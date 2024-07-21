def maxLenChain(pairs):
    
    sortPairs = sorted(pairs,key = lambda x:x[1])
    # initial stage 
    res = []
    count = 0
    
    # stage 1
    res.append(sortPairs[0])
    count += 1
    end = sortPairs[0][1]
    for i in range(1,len(pairs)):
        
        if sortPairs[i][0] >= end:
            end = sortPairs[i][1]
            count += 1
            res.append(sortPairs[i])
    print(f'Total Count : {count}')
    print(f'Total pairs : {res}')
            
            
        
    
    
pairs= [[5,24],[39,60],[5,28],[27,40],[50,90]]  
maxLenChain(pairs)  