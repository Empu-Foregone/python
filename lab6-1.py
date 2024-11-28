def insert_element(lst, index, element):
  """Вставляє елемент в список на вказану позицію.

  Args:
    lst: Вхідний список.
    index: Індекс, на який потрібно вставити елемент.
    element: Елемент для вставки.

  Returns:
    Модифікований список.
  """

  result = []
  for i, item in enumerate(lst):
    if i == index:
      result.append(element)
    result.append(item)

  return result

# Отримання списку від користувача
my_list = list(map(int, input("Введіть елементи списку через пробіл: ").split()))

# Отримання індексу та елемента для вставки
index = int(input("Введіть індекс для вставки: "))
element = int(input("Введіть елемент для вставки: "))

# Виклик функції та друк результату
result_list = insert_element(my_list, index, element)
print("Результат:", result_list)