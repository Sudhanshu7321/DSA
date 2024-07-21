class Node:
    def __init__(self, s, d):
        self.s = s
        self.d = d

class Graph:
    def __init__(self):
        self.graph = {}

    def add(self, s, d):
        if s not in self.graph:
            self.graph[s] = []
        if d not in self.graph:
            self.graph[d] = []
        self.graph[s].append(Node(s, d))
        
    def allPath(self, s, d, path, visited):
        
        visited.add(s)
        path += str(s)
        
        if s == d:
            print(path)
        else:
            for node in self.graph[s]:
                if node.d not in visited:
                    self.allPath(node.d, d, path, visited)
        
        # Backtrack
        path = path[:-1]
        visited.remove(s)

# Example usage
g = Graph()
g.add(0, 3)
g.add(2, 3)
g.add(3, 1)
g.add(4, 0)
g.add(4, 1)
g.add(5, 0)
g.add(5, 2)

# Find all paths from 5 to 1
g.allPath(5, 1, '', set())
