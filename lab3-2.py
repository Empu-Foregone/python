def find_duplicate_letters(word):
    """Find and print duplicate letters in the given word."""
    word = word.lower()  # Convert the word to lowercase for case-insensitive comparison
    letter_count = {}  # Dictionary to store the count of each letter

    # Count occurrences of each letter
    for letter in word:
        if letter.isalpha():  # Ensure it's a letter
            letter_count[letter] = letter_count.get(letter, 0) + 1

    # Find and print duplicate letters
    duplicates = [letter for letter, count in letter_count.items() if count > 1]
    if duplicates:
        print("Duplicate letters in the word:")
        print(", ".join(duplicates))
    else:
        print("No duplicate letters found in the word.")

# Input word
word = input("Enter a word: ")
find_duplicate_letters(word)
