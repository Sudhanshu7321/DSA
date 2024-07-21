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

    def dfsSort(self):
        visit = set()
        stack = []
        for vertex in self.graph:
            if vertex not in visit:
                self.dfsSortUtil(vertex, visit, stack)
        
        while stack:
            print(stack.pop(), end=' ')        

    def dfsSortUtil(self, curr, visit, stack):
        visit.add(curr)
        for node in self.graph[curr]:
            if node.d not in visit:
                self.dfsSortUtil(node.d, visit, stack)
        stack.append(curr)

# Example usage:
g = Graph()

g.add(6, 3)
g.add(6, 1)
g.add(5, 1)
g.add(5, 2)
g.add(3, 4)
g.add(4, 2)

g.dfsSort()  # Expected output: 5 6 1 3 4 2 

