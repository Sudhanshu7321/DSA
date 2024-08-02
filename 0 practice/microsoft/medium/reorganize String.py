import heapq
def rs(s):   
    count = {}
    fre = [0]*26
    for f in s:
        fre[ord(f) - ord('a')] += 1
        count[f] = count.get(f,0)+1
    pq = []
    for i in count:
        pq.append((i,count[i]))
    heapq.heapify(pq)
    
    c= heapq.heap(pq)
    return c
        
print(rs("aaaaabbbbcccdddddd"))        