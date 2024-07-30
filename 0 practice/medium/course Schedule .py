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
        visit = set()
        
        for vertex in self.graph: 
            print(f'S : {vertex}',end=':')
            visit.add(vertex)
            
            for node in self.graph[vertex]:
                # if node.s not in visit:
                    # visit.add(node.s)
                    print(node.d,end=',')
            print('')    
    
    def topologicalSort(self):
        visit = set()
        stack =  []
        
        for vertex in self.graph:
            if vertex not in visit:
                self.util(vertex,visit,stack)    
        while stack:
            print(stack.pop(), end=' ')                 
                
    def util(self,curr, visit,staack):
        visit.add(curr)
        for node in self.graph[curr]:
            if node.d not in staack:
                self.util(node.d, visit, staack)
        staack.append(curr)                        
                            
    
    # def displayUtil(self,curr):   
        
    #     for node in self.graph[curr]:
    #         if node not in visit:
    #             visit.add(node.d)         
    
g = Graph()
c = [[1,0],[2,0],[3,1],[3,2]]
for i in range(len(c)):
    g.add(c[i][1],c[i][0])     
    
g.topologicalSort()                     