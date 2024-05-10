def prim_mst(graph):
    mst = []
    visited = set()
    start_vertex = list(graph.keys())[0]
    mst.append(start_vertex)
    visited.add(start_vertex)
    while len(visited) < len(graph):
        min_weight = float('inf')
        min_edge = None
        for vertex in mst:
            for neighbor, weight in graph[vertex].items():
                if neighbor not in visited and weight < min_weight:
                    min_weight = weight
                    min_edge = (vertex, neighbor)
        mst.append(min_edge[1])
        visited.add(min_edge[1])
    return mst

example_graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 4, 'D': 1},
    'C': {'A': 3, 'B': 4, 'D': 5},
    'D': {'B': 1, 'C': 5}
}

minimum_spanning_tree = prim_mst(example_graph)
print("Minimum Spanning Tree:", minimum_spanning_tree)
