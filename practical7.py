# Function to compute in-degrees and out-degrees given an adjacency matrix
def compute_degrees(adj_matrix):
    num_vertices = len(adj_matrix)  # Number of vertices in the graph
    in_degrees = [0] * num_vertices  # Initialize in-degrees array with zeros
    out_degrees = [0] * num_vertices  # Initialize out-degrees array with zeros
# Compute out-degrees
    for i in range(num_vertices):
        out_degrees[i] = sum(adj_matrix[i])  # Out-degree is the sum of the row
# Compute in-degrees
    for i in range(num_vertices):
        for j in range(num_vertices):
            if adj_matrix[j][i]:  # If there's an edge from vertex j to vertex i
                in_degrees[i] += 1  # Increment the in-degree for vertex i
    return in_degrees, out_degrees
# Define a directed graph using an adjacency matrix
# Example graph with 5 vertices (A, B, C, D, E)
adj_matrix = [
    # A  B  C  D  E
    [0, 1, 1, 0, 0],  # A points to B and C
    [0, 0, 0, 1, 0],  # B points to D
    [0, 0, 0, 1, 1],  # C points to D and E
    [0, 0, 0, 0, 0],  # D points to no one
    [1, 0, 0, 1, 0],  # E points to A and D
]
# Compute the in-degrees and out-degrees for each vertex
in_degrees, out_degrees = compute_degrees(adj_matrix)
print("In-degrees:")
for i in range(len(in_degrees)):
    print(f"Vertex {i}: {in_degrees[i]}")
print("\nOut-degrees:")
for i in range(len(out_degrees)):
    print(f"Vertex {i}: {out_degrees[i]}")
