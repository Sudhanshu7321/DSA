def meetingRoom(arr):
    
    count = 0
    for i in range(len(arr)-1):
        if arr[1] > arr[0]:
            count += 1
    return count        

arr = [[0,30],[5,10],[15,20]]

print(f'Meenting Conference : {meetingRoom(arr)}')