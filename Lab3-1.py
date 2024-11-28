# Assigning a string to a variable
text = "Fiction is the best album of Dark Tranquillity"

# Checking if the string is long enough for slicing
if len(text) >= 15:
    slice_text = text[11:15]  # Note: Indexing starts from 0, so 12th character has index 11
    print(f"The slice from the 12th to the 15th character (excluding the 15th): '{slice_text}'")
else:
    print("The string is too short to perform the requested slice.")
