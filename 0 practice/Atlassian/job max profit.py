startTime = [1,2,3,3,1]
endTime = [3,4,5,6,0]
profit = [50,10,40,70,50]
final = [[startTime[i],endTime[i],profit[i]] for i in range(len(startTime))]  
final = sorted(final,key= lambda x : x[1])
print(final) 