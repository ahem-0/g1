def is_complete_graph(adj_matrix):
    n = len(adj_matrix)
    for i in range(n):
        for j in range(n):
            if i != j and adj_matrix[i][j] == 0:
                return False
    return True

# Example usage
adj_matrix = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]
print(is_complete_graph(adj_matrix))  
