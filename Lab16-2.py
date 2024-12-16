import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

# Завантаження необхідних ресурсів NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Зберегти у текстовому файлі довільний текст (до 100 слів)
text = """In the heart of a bustling city, there stood an old library that had seen better days. Despite its aged appearance, the library was a treasure trove of knowledge, filled with books that spanned centuries. The shelves were lined with leather-bound volumes, their pages yellowed with age and filled with stories waiting to be discovered. Among these books, there was a particular volume that captured the attention of every visitor - a large, dusty tome titled "Legends of the Ancient World." It was said that this book held secrets of lost civilizations and forgotten myths. Scholars and curious readers alike would spend hours poring over its pages, hoping to uncover some hidden truth. The librarian, an elderly woman with a kind smile, would always encourage visitors to explore the depths of the library's collection. "Knowledge is a treasure," she would say, "and this library is a gateway to endless adventures." Despite the world outside growing more digital, this quaint library remained a sanctuary for those seeking the magic of words and the wisdom of ages past."""

with open('original_text.txt', 'w') as file:
    file.write(text)

# Зчитування тексту з файлу
with open('original_text.txt', 'r') as file:
    text = file.read()

# Токенізація по словам
words = word_tokenize(text)

# Лемматизація та стеммінг
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
stemmed_words = [stemmer.stem(word) for word in words]

# Видалення стоп-слів та пунктуації
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.isalpha() and word not in stop_words]

# Записати оброблений текст у інший файл
with open('processed_text.txt', 'w') as file:
    file.write(' '.join(filtered_words))

# Виведення результатів
print("Токенізовані слова:", words)
print("Лемматизовані слова:", lemmatized_words)
print("Стеммовані слова:", stemmed_words)
print("Оброблений текст:", filtered_words)
