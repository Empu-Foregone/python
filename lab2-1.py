import math

def calculate_function(m):
  """Calculates the value of the function according to the given formula.

  Args:
    m: Value of m.

  Returns:
    Value of Function.
  """

  result = 1 / math.sqrt(m**2 - 1)
  return result

def calculate_total_distance(n):
  """Calculates the total distance that the athlete will run in n days.

  Args:
    n: Number of Days.

  Returns:
    Full distance.
  """

  distance = 10  
  total_distance = 0
  for _ in range(n):
    total_distance += distance
    distance *= 1.1  
  return total_distance

if __name__ == "__main__":
  # Задача 1
  m = float(input("Enter value of m: "))
  result = calculate_function(m)
  print("The result of the calculation of the function:", result)

  # Задача 2
  n = int(input("enter the nemuber of days: "))
  total_distance = calculate_total_distance(n)
  print("The total distance that the athlete will run:", total_distance, "km")
