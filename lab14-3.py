import json
import matplotlib.pyplot as plt

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

# Function to create and display a pie chart
def create_pie_chart():
    countries = load_from_json()
    if not countries:
        print("No data available to create a pie chart.")
        return

    # Count countries by continent
    continent_counts = {}
    for country in countries:
        continent = country["continent"]
        continent_counts[continent] = continent_counts.get(continent, 0) + 1

    # Prepare data for the pie chart
    labels = list(continent_counts.keys())
    sizes = list(continent_counts.values())
    colors = plt.cm.tab20.colors[:len(labels)]  # Generate colors dynamically

    # Plot the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, textprops={'fontsize': 12})
    plt.title("Розподіл країн за континентами", fontsize=16)
    plt.axis('equal')  # Ensure the pie chart is circular
    plt.show()

# Main function to interact with the user
def main():
    while True:
        print("\nMenu:")
        print("1. Display the contents of the JSON file")
        print("2. Add a new country")
        print("3. Remove a country")
        print("4. Search for countries")
        print("5. Check for countries in Africa or Asia")
        print("6. Show pie chart of countries by continent")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

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
            create_pie_chart()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Initially saving the sample countries data to the JSON file
    save_to_json(countries_data)
    main()
