def selectActivity(start,end):
    ans = []
    maxActivity = 1
    ans.append(0)
    lastEnd = end[0]
    for i in range(len(end)):
        if start[i] >= lastEnd:
            maxActivity += 1
            ans.append(i)
            lastEnd = end[i]
    print(f'Max Activity is : {maxActivity}')
    print(f'And activities are: {ans}')        
    

start = [1,3,0,5,8,5]
end = [2,4,6,7,9,9] 

schedule = []
for i in range(len(start)):
    col = [i,start[i], end[i]]
    schedule.append(col)     
print(schedule)

# sort 

shortSchedule = sorted(schedule,key = lambda x:x[2])
print(shortSchedule)
        

        

# selectActivity(start,end)