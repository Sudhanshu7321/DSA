def q1(arr,i,key):
    if i == len(arr):
        return 
    
    if arr[i] == key:
        print(i)
        
    return q1(arr,i+1,key)

def q2(num,res):
    
    if num == '':
        return
    
# def q3(s,i,res,count):
#     if i == len(s):
#         return
    
#     if res[0] == res[-1]:
#         count += 1
#     return q3(s,i+1,res,count)

s = "aba"
# q3(s,0,[],0)    
        

q1([3, 2, 4, 5, 6, 2, 7, 2, 2],0,2)


def tower_of_hanoi(n, src, helper, dest):
    if n == 1:
        print(f"transfer disk {n} from {src} to {dest}")
        return
    
    # Transfer top n-1 disks from src to helper using dest as 'helper'
    tower_of_hanoi(n-1, src, dest, helper)
    
    # Transfer nth disk from src to dest
    print(f"transfer disk {n} from {src} to {dest}")
    
    # Transfer n-1 disks from helper to dest using src as 'helper'
    tower_of_hanoi(n-1, helper, src, dest)

if __name__ == "__main__":
    n = 4
    tower_of_hanoi(n, "A", "B", "C")
