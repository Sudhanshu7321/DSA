def changeArry(arr , i ,val):
    
    # Base case 
    if i == len(arr):
        return
    
    # Recursion (Kaam) 
    arr[i] = val
    changeArry(arr,i+1,val+1) #fxn call step
    arr[i] -= 2 # backtracking  step
    
arr = [0]*5
changeArry(arr,0,1)
print(arr)    
    