def compute_degrees(adj_matrix):
    n = len(adj_matrix)
    in_degrees = [0] * n
    out_degrees = [0] * n

    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 1:
                out_degrees[i] += 1
                in_degrees[j] += 1
    
    return in_degrees, out_degrees

# Example usage
adj_matrix = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 0, 0]
]
in_degrees, out_degrees = compute_degrees(adj_matrix)
print("In-degrees:", in_degrees)
print("Out-degrees:", out_degrees)
