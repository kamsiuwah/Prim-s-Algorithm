import heapq  # Import the heapq library to use the heap queue (priority queue) for efficient minimum element extraction.

def prim_mst(graph):
    # The graph is represented as a dictionary where keys are node labels and values are lists of (weight, node) tuples.
    # This adjacency list structure provides easy access to connected nodes and the corresponding weights.

    # Start the MST from an arbitrary node. Here, the first node from the dictionary is used.
    start_node = next(iter(graph))

    # Initialize the MST edges list, a set to track visited nodes, and a min heap for edges to be processed.
    mst = []  # Stores the edges in the MST.
    visited = set()  # Tracks the nodes that have been added to the MST to avoid cycles.
    min_edges = [(0, start_node, None)]  # Min-heap initialized with the first node and a weight of 0.

    # Process the edges in the priority queue until it's empty.
    while min_edges:
        weight, current_node, from_node = heapq.heappop(min_edges)  # Extract the edge with the smallest weight.
        if current_node not in visited:
            visited.add(current_node)  # Mark the node as visited.
            if from_node is not None:
                mst.append((from_node, current_node, weight))  # Add the edge to the MST, except for the first node.

            # Iterate through the connected nodes of the current node.
            for next_weight, next_node in graph[current_node]:
                # Only add edges connected to unvisited nodes to prevent cycles.
                if next_node not in visited:
                    heapq.heappush(min_edges, (next_weight, next_node, current_node))

    # Return the list of edges in the MST.
    return mst

def print_mst_results(graph, graph_type):
    print(f"\nResults for {graph_type} graph using Prim's algorithm:")
    mst_prim = prim_mst(graph)  # Compute the MST using Prim's algorithm.
    # Calculate the total weight of the MST.
    total_weight_prim = sum(weight for _, _, weight in mst_prim)
    print("MST includes the following edges:")
    for from_node, to_node, weight in mst_prim:
        print(f"{from_node} - {to_node} with weight {weight}")
    print("Total Weight of the MST:", total_weight_prim)

# Define graphs with different characteristics using adjacency lists.
sparse_graph_adj = {
    'A': [(1, 'B')],
    'B': [(1, 'A'), (3, 'C')],
    'C': [(3, 'B')]
}

dense_graph_adj = {
    'A': [(2, 'B'), (4, 'C'), (1, 'D')],
    'B': [(2, 'A'), (3, 'C'), (5, 'D')],
    'C': [(4, 'A'), (3, 'B'), (1, 'D')],
    'D': [(1, 'A'), (5, 'B'), (1, 'C')]
}

varied_weights_graph_adj = {
    'A': [(10, 'B'), (20, 'C')],
    'B': [(10, 'A'), (15, 'C')],
    'C': [(20, 'A'), (15, 'B'), (5, 'D')],
    'D': [(5, 'C')]
}

# Run the function for different graph types and print the results.
print_mst_results(sparse_graph_adj, "Sparse")
print_mst_results(dense_graph_adj, "Dense")
print_mst_results(varied_weights_graph_adj, "Varied Weights")
