class Node:
    def __init__(self, s, d, w):
        self.s = s  # Source vertex
        self.d = d  # Destination vertex
        self.w = w  # Weight of the edge

class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_edge(self, s, d, w):
        if s not in self.graph:
            self.graph[s] = []
        if d not in self.graph:
            self.graph[d] = []
        self.graph[s].append(Node(s, d, w))     
           
    def display(self):
        for vertex in self.graph:
            print(f'Source: {vertex}')
            for node in self.graph[vertex]:
                print(f'Destination: {node.d}, Weight: {node.w}', end=", ")
            print("")    
            
    def bfsDisplay(self, start_vertex):
        q = []
        visit = set()
        q.append(start_vertex)
        visit.add(start_vertex)
        
        while q:
            curr = q.pop(0)
            print(curr)
           
            for node in self.graph[curr]:
                if node.d not in visit:
                    q.append(node.d)
                    visit.add(node.d)

    def dfsDisplay(self, curr, visited=None):
        if visited is None:
            visited = set()
            
        print(curr)
        visited.add(curr)
        
        for node in self.graph[curr]:
            if node.d not in visited:
                self.dfsDisplay(node.d, visited)

# Example usage:
g = Graph()
g.add_edge('A', 'B', 5)
g.add_edge('A', 'C', 10)
g.add_edge('B', 'C', 2)
g.add_edge('C', 'D', 3)
g.display()

print("BFS Display:")
g.bfsDisplay('B')
print("\nDFS Display:")
g.dfsDisplay('A')



