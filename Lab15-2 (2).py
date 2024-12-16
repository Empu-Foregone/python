import pandas as pd
import matplotlib.pyplot as plt

# Налаштування стилю графіків
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

# Завантаження даних з CSV файлу
fixed_df = pd.read_csv('comptage_velo_2018.csv', 
                       sep=',', encoding='utf-8', 
                       parse_dates=['Date'], dayfirst=True, 
                       index_col='Date')

# Переглядаємо перші 3 рядки датафрейму
fixed_df.head(3)

# Додавання стовпця "Month" для групування за місяцем
fixed_df['Month'] = fixed_df.index.month

# Агрегація даних за місяцямиi
monthly_counts = fixed_df.groupby('Month').sum()

# Визначення місяця з найбільшою кількістю велосипедистів
most_popular_month = monthly_counts['Berri1'].idxmax()
print(f'Найбільш популярний місяць у велосипедистів: {most_popular_month}')

# Візуалізація даних
monthly_counts['Berri1'].plot(kind='bar', color='skyblue')
plt.xlabel('Місяць')
plt.ylabel('Кількість велосипедистів')
plt.title('Кількість велосипедистів за місяцями у 2018 році')
plt.show()
