def find_subsequence(lst, subsequence):
  """Шукає послідовність елементів в списку.

  Args:
    lst: Вхідний список.
    subsequence: Послідовність для пошуку.

  Returns:
    Індекс початку знайденої послідовності або -1, якщо не знайдено.
  """

  n = len(lst)
  m = len(subsequence)

  for i in range(n - m + 1):
    j = 0
    while j < m and lst[i + j] == subsequence[j]:
      j += 1
    if j == m:
      return i
  return -1

# Отримання списку від користувача
my_list = list(map(int, input("Введіть елементи списку через пробіл: ").split()))

# Отримання послідовності для пошуку
subsequence = list(map(int, input("Введіть послідовність для пошуку через пробіл: ").split()))

# Виклик функції та друк результату
result = find_subsequence(my_list, subsequence)
if result != -1:
  print("Послідовність знайдена, починаючи з індексу:", result)
else:
  print("Послідовність не знайдена")