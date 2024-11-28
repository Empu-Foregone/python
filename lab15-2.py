import pandas as pd

data = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Bike Lane Usage': [5000, 6000, 7500, 8000, 9000, 10000, 12000, 14000, 11000, 9500, 7000, 6000]
})

print(data)

# Визначення найбільш популярного місяця
most_popular_month = data.loc[data['Bike Lane Usage'].idxmax(), 'Month']
print(f"Найбільш популярний місяць: {most_popular_month}")