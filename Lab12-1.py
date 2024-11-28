import json

# Sample countries data
countries_data = [
    {"name": "Nigeria", "area": 923768, "population": 206700000, "continent": "Africa"},
    {"name": "China", "area": 9596961, "population": 1393409038, "continent": "Asia"},
    {"name": "USA", "area": 9833517, "population": 331893745, "continent": "North America"},
    {"name": "India", "area": 3287263, "population": 1366417754, "continent": "Asia"},
    {"name": "Russia", "area": 17098242, "population": 145912025, "continent": "Europe"},
    {"name": "Canada", "area": 9984670, "population": 38005238, "continent": "North America"},
    {"name": "Brazil", "area": 8515767, "population": 212559417, "continent": "South America"},
    {"name": "Egypt", "area": 1002450, "population": 91250000, "continent": "Africa"},
    {"name": "Australia", "area": 7692024, "population": 25687041, "continent": "Oceania"},
    {"name": "South Korea", "area": 100210, "population": 51329899, "continent": "Asia"}
]

# Function to save the data into a JSON file
def save_to_json(data, filename="countries.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Function to load data from the JSON file
def load_from_json(filename="countries.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to display the contents of the JSON file
def display_json():
    countries = load_from_json()
    if countries:
        print("Countries Data:")
        for country in countries:
            print(country)
    else:
        print("No data available.")

# Function to add a new country to the JSON file
def add_country():
    name = input("Enter country name: ")
    area = int(input("Enter country area (in square km): "))
    population = int(input("Enter country population: "))
    continent = input("Enter continent (Africa, Asia, etc.): ")

    new_country = {"name": name, "area": area, "population": population, "continent": continent}

    countries = load_from_json()
    countries.append(new_country)
    save_to_json(countries)

    print(f"Country {name} added successfully.")

# Function to remove a country from the JSON file
def remove_country():
    name = input("Enter the name of the country to remove: ")

    countries = load_from_json()
    countries = [country for country in countries if country['name'] != name]

    save_to_json(countries)
    print(f"Country {name} removed successfully.")

# Function to search for countries by a specific field
def search_country():
    field = input("Enter the field to search by (name, area, population, continent): ").lower()
    value = input("Enter the value to search for: ")

    countries = load_from_json()
    result = []

    for country in countries:
        if str(country.get(field, "")).lower() == value.lower():
            result.append(country)

    if result:
        print(f"Found {len(result)} countries:")
        for country in result:
            print(country)
    else:
        print("No countries found with that search criteria.")

# Function to check and print countries located in Africa or Asia
def check_africa_asia():
    countries = load_from_json()
    found = False
    for country in countries:
        if country['continent'] in ['Africa', 'Asia']:
            print(f"Country: {country['name']} is located in {country['continent']}.")
            found = True
    if not found:
        print("No countries are located in Africa or Asia.")

# Main function to interact with the user
def main():
    while True:
        print("\nMenu:")
        print("1. Display the contents of the JSON file")
        print("2. Add a new country")
        print("3. Remove a country")
        print("4. Search for countries")
        print("5. Check for countries in Africa or Asia")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            display_json()
        elif choice == '2':
            add_country()
        elif choice == '3':
            remove_country()
        elif choice == '4':
            search_country()
        elif choice == '5':
            check_africa_asia()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Initially saving the sample countries data to the JSON file
    save_to_json(countries_data)
    main()
