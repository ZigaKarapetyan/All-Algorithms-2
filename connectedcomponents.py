def dfs_cc(graph, v, visited, comp):
    visited.add(v)
    comp.append(v)
    for nei in graph[v]:
        if nei not in visited:
            dfs_cc(graph, nei, visited, comp)

def connected_components(graph):
    visited = set()
    all_components = []
    for v in graph:
        if v not in visited:
            comp = []
            dfs_cc(graph, v, visited, comp)
            all_components.append(comp)
    return all_components


g = {0:[1], 1:[0], 2:[3], 3:[2], 4:[]}
print(connected_components(g))
