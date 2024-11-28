import math

def calculate_function(m):
  """Розраховує значення функції за заданою формулою.

  Args:
    m: Значення змінної m.

  Returns:
    Значення функції.
  """

  result = 1 / math.sqrt(m**2 - 1)
  return result

def calculate_total_distance(n):
  """Розраховує загальний шлях, який пробіжить спортсмен за n днів.

  Args:
    n: Кількість днів.

  Returns:
    Загальна відстань.
  """

  distance = 10  # Початкова відстань
  total_distance = 0
  for _ in range(n):
    total_distance += distance
    distance *= 1.1  # Збільшення відстані на 10%
  return total_distance

if __name__ == "__main__":
  # Задача 1
  m = float(input("Введіть значення m: "))
  result = calculate_function(m)
  print("Результат обчислення функції:", result)

  # Задача 2
  n = int(input("Введіть кількість днів: "))
  total_distance = calculate_total_distance(n)
  print("Загальна відстань, яку пробіжить спортсмен:", total_distance, "км")