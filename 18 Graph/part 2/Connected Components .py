class Node:
    def __init__(self,s,d):
        self.s = s
        self.d = d
        
class Graph:
    def __init__(self):
        self.graph = {}
        
    def add(self,s,d):
        
        if s not in self.graph:
            self.graph[s] = []
        if d not in self.graph:
            self.graph[d] = []
            
        self.graph[s].append(Node(s,d))
        
    def display(self):
        
        for vertex in self.graph:
            for node in self.graph[vertex]:
                print(f'Sorce: {node.s}, Dis: {node.d}')      
  
    def dfsDiaplay(self):
        visit = set()
        for vertex in self.graph:
            if vertex not in visit:
                Graph.dfsutil(self,vertex,visit)
                
    def dfsutil(self,curr,visit):
            visit.add(curr)
            print(curr,end=',')
            
            for node in self.graph[curr]:
                if node.d not in visit:
                    Graph.dfsutil(self,node.d,visit)   
                          
g = Graph()
g.add(1,2)                              
g.add(1,3)                              
g.add(2,3)                              
g.add(3,4)
g.add(10,11)
g.add(10,12)
g.add(12,13)
g.display()   
g.dfsDiaplay()                           