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
        
    def cycleDetection(self):
        
        visit = set()
        for vertex in self.graph:
            if vertex not in visit:
                if Graph.cycleDetectionUtil(self,vertex,visit,-1):
                    return True
        return False    
        
    def cycleDetectionUtil(self,curr,visit,parent):
        visit.add(curr)
        
        for node in self.graph[curr]:
            if (node.d not in visit):
                if Graph.cycleDetectionUtil(self,node.d,visit,curr):
                    return True
            elif (node.d in visit) and (node.d != parent):
                return True
       

g = Graph()
g.add(0,1)
g.add(0,2)
g.add(0,3)

g.add(1,0)
g.add(1,2)

g.add(2,0)
g.add(2,1)

g.add(3,0)
g.add(3,4)

g.add(4,3)

print(g.cycleDetection())