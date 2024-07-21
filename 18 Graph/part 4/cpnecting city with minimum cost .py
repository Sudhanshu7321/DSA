import heapq
class Node:
    def __init__(self,s,d,w):
        self.s = s
        self.d = d
        self.w = w
        
class Graph:
    
    def __init__(self):
        self.graph = {}
        
    def add(self,s,d,w):
        if s not in self.graph:
            self.graph[s] = []
        if d not in self.graph:
            self.graph[d] = []
            
        self.graph[s].append(Node(s,d,w))
        
    def display(self):
        for vertex in self.graph:
            for node in self.graph[vertex]:
                print(f'S:{node.s}, D:{node.d}, W:{node.w}')    

    def primss(self):
        pq = []
        visit = set()
        cost = 0
        
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
                
                
g = Graph()
n = [[0,1,2,3,4],[1,0,5,0,7],[2,5,0,6,0],[3,0,6,0,0],[4,7,0,0,0]]        
for i in range(len(n)):
    for j in range(len(n[0])):
        if n[i][j] != 0:
            g.add(i,j,n[i][j])
            
g.display()   

g.primss()         
            
                            
                        