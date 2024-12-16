# Описуємо структуру даних для країн
class Country:
    def __init__(self, name, area, population, continent):
        self.name = name
        self.area = area
        self.population = population
        self.continent = continent

def find_countries_in_asia_or_africa(countries):
    result = [country.name for country in countries if country.continent in ['Азія', 'Африка']]
    return result

# Список країн із загальною інформацією про них
countries = [
    Country("Україна", 603628, 41723998, "Європа"),
    Country("Канада", 9984670, 38005238, "Північна Америка"),
    Country("Єгипет", 1002450, 104124440, "Африка"),
    Country("Китай", 9596960, 1444216107, "Азія"),
    Country("Бразилія", 8515767, 213993437, "Південна Америка"),
    Country("Австралія", 7692024, 25687041, "Австралія"),
    Country("Індія", 3287263, 1393409038, "Азія"),
    Country("Південна Африка", 1221037, 59308690, "Африка"),
    Country("Франція", 551695, 65273511, "Європа"),
    Country("Японія", 377975, 125960000, "Азія")
]

# Знаходимо країни в Африці або Азії
countries_in_asia_or_africa = find_countries_in_asia_or_africa(countries)

# Друкуємо результати
if countries_in_asia_or_africa:
    print("Країни, що знаходяться в Африці або в Азії:")
    for country in countries_in_asia_or_africa:
        print(country)
else:
    print("Серед заданих країн немає тих, що знаходяться в Африці або в Азії.")
