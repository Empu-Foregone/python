def create_matrix(n):
  """Creates an n x n matrix according to the given pattern.

  Args:
    n: sive of matrix.

  Returns:
    A two-dimensional array filled according to a pattern.
  """

  matrix = [[0] * n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      matrix[i][j] = j - i if i >= j else i + j

  return matrix

def print_matrix(matrix):
  for row in matrix:
    print(*row)

n = 7
matrix = create_matrix(n)
print_matrix(matrix)
