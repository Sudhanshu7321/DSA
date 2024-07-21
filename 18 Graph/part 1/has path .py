class Node:
    def __init__(self, s, d):
        self.s = s  # Source vertex
        self.d = d  # Destination vertex
        
class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_edge(self, s, d):
        if s not in self.graph:
            self.graph[s] = []
        if d not in self.graph:
            self.graph[d] = []
        self.graph[s].append(Node(s, d))   
        
    def dfs_display(self, curr, visit=None):
        if visit is None:
            visit = set()
        visit.add(curr)
        print(curr,end='->')
        
        for node in self.graph[curr]:
            if node.d not in visit:
                self.dfs_display(node.d, visit)
                
    def hasPath(self,s,d,visit=None):
        
        if s == d :
            return True
        if visit is None:
            visit = set()
        visit.add(s)
        
        for node in self.graph[s]:
            if node.d not in visit and self.hasPath(node.d,d,visit):
                return True
        
        return False        
                        

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)
g.add_edge(5, 6)

g.dfs_display(0)
# 0->1->3->4->5->6->2->
print(g.hasPath(2,6))
print(len(g.graph))