intervals = [[1,4],[5,6]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

def mergeInterval(intervals):
    res = []
    
    if not intervals:
        return res
    
    intervals = sorted(intervals, key= lambda x : x[0])   
       
    res.append(intervals[0])
    
    for i in range(1,len(intervals)):
        if res[i-1][1] < intervals[i][0]:
            res.append(intervals[i])
        else:
            res[i-1][1] =  intervals[i][1]
    return res

# print(mergeInterval(intervals))    

  
print(intervals)        