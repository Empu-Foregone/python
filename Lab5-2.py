def create_matrix(n):
  """Створює матрицю розміром n x n за заданим шаблоном.

  Args:
    n: Розмір матриці.

  Returns:
    Двовимірний масив, заповнений відповідно до шаблону.
  """

  matrix = [[0] * n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      matrix[i][j] = j - i if i >= j else i + j

  return matrix

# Виведення матриці на екран
def print_matrix(matrix):
  for row in matrix:
    print(*row)

# Приклад використання
n = 7
matrix = create_matrix(n)
print_matrix(matrix)