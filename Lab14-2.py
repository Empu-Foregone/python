import matplotlib.pyplot as plt
import pandas as pd

# Дані для аналізу
data = {
    "Year": [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    "Ukraine": [5.2, 5.1, 5.0, 4.9, 4.8, 4.7, 4.6, 4.5, 4.4, 4.3, 4.2, 4.1, 4.0, 3.9, 3.8, 3.7, 3.6, 3.5, 3.4, 3.3, 3.2, 3.1],
    "USA": [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1]
}

# Перетворення даних у DataFrame
df = pd.DataFrame(data)

# Лінійний графік динаміки показника для України та США
plt.figure(figsize=(10, 5))
plt.plot(df["Year"], df["Ukraine"], label="Україна", marker='o', color='blue')
plt.plot(df["Year"], df["USA"], label="США", marker='o', color='orange')
plt.xlabel("Рік")
plt.ylabel("Children out of school, primary (%)")
plt.title("Динаміка показника 'Children out of school, primary' для України та США")
plt.legend()
plt.grid(True)
plt.show()

# Стовпчаста діаграма значень показника для кожної країни
plt.figure(figsize=(12, 6))
df.set_index("Year")[["Ukraine", "USA"]].plot(kind='bar', color=['blue', 'orange'], width=0.8)
plt.xlabel("Рік")
plt.ylabel("Children out of school, primary (%)")
plt.title("Значення показника 'Children out of school, primary' для України та США")
plt.legend(["Україна", "США"])
plt.grid(axis='y')
plt.tight_layout()
plt.show()