def count_words_starting_with_n(sentence):
  """Counts the number of words in a sentence that start with the letter "n".

  Args:
    sentence: Incoming sentence.

  Returns:
    Number of words starting with "n".
  """

  words = sentence.split()  
  count = 0
  for word in words:
    if word.lower().startswith('n'): 
      count += 1
  return count

if __name__ == "__main__":
  sentence = input("Enter a sentence: ")
  result = count_words_starting_with_n(sentence)
  print("Number of words starting with 'n':", result)
