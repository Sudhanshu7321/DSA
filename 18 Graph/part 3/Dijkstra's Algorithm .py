import heapq

class Node:
    def __init__(self, s, d, w):
        self.s = s
        self.d = d
        self.w = w

class Graph:
    def __init__(self):
        self.graph = {}
        
    def add(self, s, d, w):
        if s not in self.graph:
            self.graph[s] = []
        if d not in self.graph:
            self.graph[d] = []
        self.graph[s].append(Node(s, d, w))
        
    def dijkstra(self, src):
        # Initialize distances with infinity and set distance of source to 0
        dist = {node: float('inf') for node in self.graph}
        dist[src] = 0

        # Priority queue to store (distance, node)
        pq = [(0, src)]

        while pq:
            current_distance, current_node = heapq.heappop(pq)
            
            # If we find a shorter path to current_node, we skip processing it
            if current_distance > dist[current_node]:
                continue
            
            # Explore neighbors
            for edge in self.graph[current_node]:
                distance = current_distance + edge.w
                
                # Only consider this new path if it's better
                if distance < dist[edge.d]:
                    dist[edge.d] = distance
                    heapq.heappush(pq, (distance, edge.d))
        
        return dist

    def dijkstra1(self, src):
        
        dis = {node: float('inf') for node in self.graph}
        dis[src] = 0
        
        pq = [(0,src)]
        
        while pq:
            currDis , currNode = heapq.heappop(pq)
            
            if currDis > dis[currNode]:
                continue
            for edge in self.graph[currNode]:
                distance = currDis+edge.w

                if distance < dis[edge.d]:
                    dis[edge.d] = distance
                    heapq.heappush(pq,(distance,edge.d))
        return dis            
                    
# Create graph
g = Graph()
g.add(0, 1, 2)
g.add(0, 2, 4)
g.add(1, 3, 7)
g.add(1, 2, 1)
g.add(2, 4, 3)
g.add(3, 5, 1)
g.add(4, 3, 2)
g.add(4, 5, 5)

# Run Dijkstra's algorithm from source node 0
src = 0
distances = g.dijkstra1(src)
print(distances)
