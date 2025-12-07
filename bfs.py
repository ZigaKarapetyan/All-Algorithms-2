graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def BFS(graph, start):
    visited=set()
    queue =[start]
    visited.add(start)
    while queue:
        node=queue.pop(0)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


visited_nodes = BFS(graph, 'A')
print(visited_nodes)


