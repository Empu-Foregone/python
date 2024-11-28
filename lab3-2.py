def find_duplicate_letters(word):
    """Find and print duplicate letters in the given word."""
    word = word.lower() 
    letter_count = {}  

   
    for letter in word:
        if letter.isalpha():  
            letter_count[letter] = letter_count.get(letter, 0) + 1

   
    duplicates = [letter for letter, count in letter_count.items() if count > 1]
    if duplicates:
        print("Duplicate letters in the word:")
        print(", ".join(duplicates))
    else:
        print("No duplicate letters found in the word.")


word = input("Enter a word: ")
find_duplicate_letters(word)
