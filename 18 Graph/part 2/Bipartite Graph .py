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

    def biPartiteGraph(self):
        visit = set()
        yellow = set()
        blue = set()
        for vertex in self.graph:
            if vertex not in visit:
                if not self.biPartiteGraphUtil(vertex, visit, yellow, blue, True):
                    return False
        return True

    def biPartiteGraphUtil(self, curr, visit, yellow, blue, color):
        visit.add(curr)
        if color:
            yellow.add(curr)
        else:
            blue.add(curr)

        for node in self.graph[curr]:
            if node.d not in visit:
                if not self.biPartiteGraphUtil(node.d, visit, yellow, blue, not color):
                    return False
            else:
                if color and node.d in yellow:
                    return False
                if not color and node.d in blue:
                    return False
        return True

# Example usage:
g = Graph()

g.add(0, 1)
g.add(0, 2)
g.add(1, 0)
g.add(1, 3)
g.add(2, 0)
g.add(2, 3)
g.add(3, 1)
g.add(3, 2)
g.add(4, 3)
g.add(4, 2)

print(g.biPartiteGraph())  # Output: False
