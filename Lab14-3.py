import matplotlib.pyplot as plt

# Створюємо словник даних
data = [
    {"name": "Nigeria", "area": 923768, "population": 206700000, "continent": "Africa"},
    {"name": "China", "area": 9596961, "population": 1393409038, "continent": "Asia"},
    {"name": "USA", "area": 9833517, "population": 331893745, "continent": "North America"},
    {"name": "India", "area": 3287263, "population": 1366417754, "continent": "Asia"},
    {"name": "Belgium", "area": 30688, "population": 11820000, "continent": "Europe"},
    {"name": "Canada", "area": 9984670, "population": 38005238, "continent": "North America"},
    {"name": "Brazil", "area": 8515767, "population": 212559417, "continent": "South America"},
    {"name": "Egypt", "area": 1002450, "population": 91250000, "continent": "Africa"},
    {"name": "Australia", "area": 7692024, "population": 25687041, "continent": "Oceania"},
    {"name": "South Korea", "area": 100210, "population": 51329899, "continent": "Asia"}
]

# Підраховуємо кількість країн в кожному континенті
continent_counts = {"Africa": 0, "Asia": 0, "North America": 0, "Europe": 0, "South America": 0, "Oceania": 0, "Other": 0}

for entry in data:
    continent = entry["continent"]
    if continent in continent_counts:
        continent_counts[continent] += 1
    else:
        continent_counts["Other"] += 1

# Дані для кругової діаграми
labels = continent_counts.keys()
sizes = continent_counts.values()
colors = ['gold', 'yellowgreen', 'lightcoral', 'blue', 'orange', 'purple', 'red']

# Побудова кругової діаграми
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Відсоток країн за континентами')
plt.axis('equal')  # Забезпечуємо круглу форму діаграми

# Виведення діаграми на екран
plt.show()
