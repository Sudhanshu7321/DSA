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
        
    def bellmanFord(self,src):
        dis = {node : float('inf') for node in self.graph}
        dis[src] = 0
        v = len(self.graph)
        
        for vertex in self.graph:
            for node in self.graph[vertex]:
                if dis[node.s] != float('inf') and (dis[node.s] + node.w) < dis[node.d]:
                    dis[node.d] = (dis[node.s] + node.w)
            
        return dis 
    
    def bellmanFord(self, src):
        # Step 1: Initialize distances from src to all other vertices as INFINITE
        dis = {vertex: float('inf') for vertex in self.vertices}
        dis[src] = 0
        
        # Step 2: Relax all edges |V| - 1 times
        for _ in range(len(self.vertices) - 1):
            for node in self.graph:
                if dis[node.s] != float('inf') and dis[node.s] + node.w < dis[node.d]:
                    dis[node.d] = dis[node.s] + node.w
        
        # Step 3: Check for negative-weight cycles
        for node in self.graph:
            if dis[node.s] != float('inf') and dis[node.s] + node.w < dis[node.d]:
                print("Graph contains negative weight cycle")
                return None
        
        return dis
    
    
g = Graph()
g.add(0,1,2)                                        
g.add(0,2,4)                                        
g.add(1,2,-4)                                        
g.add(2,3,2)                                        
g.add(3,4,4)                                        
g.add(4,1,-1)  

print(g.bellmanFord(0))                                      