

def Dijkstra(graph, source):
    for vertex in graph:
        vertex.distance = float('inf')
        vertex.previous = None

    q = []                      
    for vertex in graph:
        q.append(vertex)

    source.distance = 0

    while q:
        u = min(q, key=lambda v: v.distance)
        q.remove(u)

        for neighbor in u.neighbors:
            alt = u.distance + u.get_edge_weight(neighbor)
            if alt < neighbor.distance:
                neighbor.distance = alt
                neighbor.previous = u

    return {v: v.distance for v in graph}

class vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        self.distance = None
        self.previous = None

    def add_neighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight  

    def get_edge_weight(self, neighbor):
        return self.neighbors[neighbor] 

    def __repr__(self):
        return self.name    
    

A = vertex('A')
B = vertex('B')
C = vertex('C')
D = vertex('D')

A.add_neighbor(B, 1)
A.add_neighbor(C, 4)
B.add_neighbor(D, 2)
C.add_neighbor(D, 1)


graph = [A, B, C, D]
source = A
 
distances = Dijkstra(graph, source)
print(distances) 

