def bellman_ford(edges, n, start):
    INF = 10**9
    dist = [INF] * n
    dist[start] = 0  

    
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            print("Graph contains a negative weight cycle")
            break

    return dist


edges = [(0,1,5), (1,2,3), (0,2,10)]
distances = bellman_ford(edges, 3, 0)

for vertex in range(len(distances)):
    print(f"Shortest path from 0 to {vertex} = {distances[vertex]}")
