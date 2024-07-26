import heapq

stones = []

stones = [-s for s in stones]

heapq.heapify(stones)

while len(stones) > 1 :
    firstStone = heapq.heappop()
    secondStone = heapq.heappop()
    if firstStone < secondStone:
        heapq.heappush(firstStone - secondStone)
    elif secondStone < firstStone:
        heapq.heappush(secondStone - firstStone)  

return abs(heapq.heappop())          