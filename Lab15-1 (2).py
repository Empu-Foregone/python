import pandas as pd

# Фраза
text = """They say the good die young?
No use in saying what is done is done 'cause it's not enough
And when the night gives way
It's like a brand new doomsday"""

# Розбиваємо фразу на слова
words = text.split()

# Створюємо словник з підрахунком кількості повторень кожного слова
word_count = {}
for word in words:
    word = word.lower().strip("?.',")
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Перетворюємо словник на датафрейм
df = pd.DataFrame(list(word_count.items()), columns=['Слово', 'Кількість'])

# Виводимо датафрейм на екран
print("Датафрейм:\n", df)

# Виконуємо агрегацію та групування даних
grouped = df.groupby("Слово").agg({
    "Кількість": "sum"
}).sort_values(by="Кількість", ascending=False)

# Виводимо результати агрегації на екран
print("\nАгреговані дані:\n", grouped)