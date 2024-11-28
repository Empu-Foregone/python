def print_pattern(n):
  """Enters the pyramid from 1 to N.

  Args:
    n: Number that means size of array.
  """

  if not 1 < n < 9:
    print("Uncorrect N. Enter numbers from 2 to 8.")
    return

  for i in range(1, n+1):
    row = ""
    for j in range(1, i+1):
      row += str(j)
    print(row)

if __name__ == "__main__":
  n = int(input("Enter N (1 < N < 9): "))
  print_pattern(n)
