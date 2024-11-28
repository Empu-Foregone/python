def count_words_starting_with_n(sentence):
  """Підраховує кількість слів у реченні, які починаються з літери "н".

  Args:
    sentence: Вхідне речення.

  Returns:
    Кількість слів, що починаються з "н".
  """

  words = sentence.split()  # Розділити речення на слова
  count = 0
  for word in words:
    if word.lower().startswith('н'):  # Перевіряємо першу літеру в нижньому регістрі
      count += 1
  return count

if __name__ == "__main__":
  sentence = input("Введіть речення: ")
  result = count_words_starting_with_n(sentence)
  print("Кількість слів, що починаються з 'н':", result)