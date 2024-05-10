# Function to find the minimum spanning tree (MST) using Prim's algorithm
def prim_mst(graph):
    # Initialize an empty list to store the MST
    mst = []
    
    # Initialize a set to keep track of vertices included in the MST
    visited = set()
    
    # Choose an arbitrary starting vertex
    start_vertex = list(graph.keys())[0]  # Select the first vertex as the starting point
    
    # Add the starting vertex to the MST and the visited set
    mst.append(start_vertex)  # Add the starting vertex to the MST
    visited.add(start_vertex)  # Mark the starting vertex as visited
    
    # Repeat until all vertices are included in the MST
    while len(visited) < len(graph):  # Loop until all vertices are visited
        # Initialize variables to store the minimum edge weight and its corresponding vertices
        min_weight = float('inf')  # Set initial minimum weight to infinity
        min_edge = None  # Set initial minimum edge to None
        
        # Iterate over each vertex in the MST
        for vertex in mst:
            # Iterate over each neighbor of the current vertex
            for neighbor, weight in graph[vertex].items():
                # If the neighbor is not already in the MST and the weight of the edge is less than the minimum weight
                if neighbor not in visited and weight < min_weight:
                    # Update the minimum weight and the corresponding edge
                    min_weight = weight
                    min_edge = (vertex, neighbor)  # Store the current minimum edge
        
        # Add the vertex with the minimum weight edge to the MST and mark it as visited
        mst.append(min_edge[1])  # Add the vertex connected to the minimum weight edge to the MST
        visited.add(min_edge[1])  # Mark the added vertex as visited
    
    return mst  # Return the minimum spanning tree

# Example usage:
# Define a weighted undirected graph as an adjacency dictionary
# Each key represents a vertex, and the corresponding value is a dictionary where keys are neighbors and values are edge weights
example_graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 4, 'D': 1},
    'C': {'A': 3, 'B': 4, 'D': 5},
    'D': {'B': 1, 'C': 5}
}

# Find the minimum spanning tree of the example graph using Prim's algorithm
minimum_spanning_tree = prim_mst(example_graph)
print("Minimum Spanning Tree:", minimum_spanning_tree)
