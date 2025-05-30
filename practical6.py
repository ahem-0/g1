def get_adjacency_matrix():
  """
  This function prompts the user to enter the dimensions
  and elements of the adjacency matrix.

  Returns:
A 2D list representing the adjacency matrix entered by the user.
  """
  n = int(input("Enter the number of vertices in the graph: "))
  adj_matrix = []
  for i in range(n):
    row = []
    for j in range(n):
      element = int(input(f"Enter element [{i}][{j}] of the adjacency matrix: "))
      row.append(element)
    adj_matrix.append(row)
  return adj_matrix
def is_complete(adj_matrix):
  """
  This function checks if a graph represented by an adjacency
  matrix is a complete graph
  Args:
adj_matrix: A 2D list representing the adjacency matrix of the graph.

  Returns:
      True if the graph is complete, False otherwise.
  """
  n = len(adj_matrix)  # Number of vertices in the graph
# Check if all elements in the diagonal are 0 (no self-loops in a complete graph)
  for i in range(n):
    if adj_matrix[i][i] != 0:
      return False
# Check if all pairs of vertices have an edge (adjacency of 1)
  for i in range(n):
    for j in range(i + 1, n):
      if adj_matrix[i][j] != 1:
        return False
  return True
# Main program
adj_matrix = get_adjacency_matrix()
if is_complete(adj_matrix):
  print("The graph is a complete graph.")
else:
  print("The graph is not a complete graph.")
