import string

def Open(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print("File", file_name, "wasn't opened!")
        return None
    else:
        print("File", file_name, "was opened!")
        return file

file1_name = "TF4_1.txt"
file2_name = "TF4_2.txt"

# a) Create TF4_1 file
file_1_w = Open(file1_name, "w")

if file_1_w is not None:
    text = [
        "Hello, how are you?",
        "This is an example of a test text.",
        "We will count words of different lengths.",
        "Words should not exceed 16 characters!"
    ]
    
    for line in text:
        file_1_w.write(line + '\n')
    
    print("Information was successfully added to TF4_1.txt!")
    file_1_w.close()
    print("File TF4_1.txt was closed!")

# b) Read and count words from TF4_1 file
file_2_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")

if file_2_r is not None and file_2_w is not None:
    word_count = {}

    text = file_2_r.read()
    # Remove punctuation and split text into words
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).split()

    for word in words:
        word_length = len(word)
        if word_length <= 16:
            word_count[word_length] = word_count.get(word_length, 0) + 1

    # Write the word count to TF4_2.txt
    for length in range(1, 17):
        count = word_count.get(length, 0)
        file_2_w.write(f"{length} characters: {count} words\n")

    file_2_r.close()
    file_2_w.close()

    print("Files were closed!")

# c) Read TF4_2 file and print the contents
file_3_r = Open(file2_name, "r")

if file_3_r is not None:
    for line in file_3_r:
        print(line.strip())

    print("File TF4_2.txt was closed!")
    file_3_r.close()
