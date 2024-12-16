import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt

# Завантаження необхідних ресурсів NLTK
nltk.download('gutenberg')
nltk.download('punkt')
nltk.download('stopwords')

# Завантаження тексту "Sense and Sensibility" Джейн Остін
text = gutenberg.raw('austen-sense.txt')

# Токенізація тексту на слова
words = word_tokenize(text.lower())

# Визначення кількості слів у тексті
word_count = len(words)
print(f'Кількість слів у тексті: {word_count}')

# Визначення 10 найбільш вживаних слів у тексті
word_freq = Counter(words)
most_common_words = word_freq.most_common(10)
print('10 найбільш вживаних слів у тексті:')
for word, freq in most_common_words:
    print(f'{word}: {freq}')

# Побудова стовпчастої діаграми для 10 найбільш вживаних слів
words, frequencies = zip(*most_common_words)
plt.bar(words, frequencies, color='blue')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.title('10 найбільш вживаних слів у тексті (без фільтрації)')
plt.show()

# Видалення стоп-слів та пунктуації
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.isalpha() and word not in stop_words]

# Визначення 10 найбільш вживаних слів у тексті після фільтрації
filtered_word_freq = Counter(filtered_words)
filtered_most_common_words = filtered_word_freq.most_common(10)
print('10 найбільш вживаних слів у тексті (після фільтрації):')
for word, freq in filtered_most_common_words:
    print(f'{word}: {freq}')

# Побудова стовпчастої діаграми для 10 найбільш вживаних слів після фільтрації
filtered_words, filtered_frequencies = zip(*filtered_most_common_words)
plt.bar(filtered_words, filtered_frequencies, color='green')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.title('10 найбільш вживаних слів у тексті (після фільтрації)')
plt.show()
