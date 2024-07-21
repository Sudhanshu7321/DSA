import heapq

class  Node:
    def __init__(self,s,d,w):
        self.s = s
        self.d = d
        self.w = w
        
class Graph:
    def __init__(self):
        self.graph = {}
        
    def add(self,s,d,w):
        if s not in self.graph:
            self.graph[s] =[]
        if d not in self.graph:
            self.graph[d] = []
        self.graph[s].append(Node(s,d,w))
        
    def prims(self):                                 
        visit = set()
        pq = []
        cost = 0
        
        # weight and destination
        heapq.heappush(pq,(0,0)) 

        while pq:
            w , curr = heapq.heappop(pq)
            if curr not in visit:
                visit.add(curr)
                cost += w
                for node in self.graph[curr]:
                    if node.d not in visit:
                        heapq.heappush(pq,(node.w,node.d))
                        
        print(f'Minimum Cost: {cost}')   
        
g  = Graph()

g.add(0,1,10)                 
g.add(0,3,30)                 
g.add(0,2,15) 

g.add(1,0,10)                
g.add(1,3,40)

g.add(2,0,15)                
g.add(2,3,50)

g.add(3,1,40)                
g.add(3,0,30)                
g.add(3,2,50)

g.prims()                
               
       
       
        