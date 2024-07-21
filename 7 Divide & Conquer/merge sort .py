def mergeSort(arr , start,end):
    if start >= end:
        return
    
    # kaam
    mid = (start + end)//2
    
    mergeSort(arr,start,mid)
    mergeSort(arr,mid+1,end)
    merge(arr,start,end)

def merge(arr,start,mid, end):
    tem = [0] * len(end-start+1)
    i = start
    j = mid+1
    k = 0
    
    return

arr = [6,3,9,5,2,8]    
mergeSort(arr,0,len(arr)-1)    