def topo_sort(graph):
    visited = set()
    order = []

    def dfs(v):
        visited.add(v)
        for nei in graph[v]:
            if nei not in visited:
                dfs(nei)
        order.append(v)

    for v in graph:
        if v not in visited:
            dfs(v)

    return order[::-1]


g = {0:[1], 1:[2], 2:[]}
print(topo_sort(g))
