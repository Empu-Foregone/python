import csv

input_file = "API_NY.GDP.PCAP.KD_DS2_en_csv_v2_45.csv"
output_file = "filtered_gdp_2016.csv"

try:
    # Вивести заголовки для перевірки
    with open(input_file, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        print("Заголовки у файлі:", reader.fieldnames)

    # Основний функціонал
    with open(input_file, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        print(f"{'Country Name':<30} {'2016 GDP (current US$)':>20}")
        print("-" * 50)

        for row in reader:
            country = row.get("Country Name", "Unknown")
            gdp_2016 = row.get("2016", "N/A")
            print(f"{country:<30} {gdp_2016:>20}")

    # Введення порогу
    threshold = float(input("\nВведіть порогове значення GDP per capita (current US$): "))

    # Фільтрація
    with open(input_file, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        filtered_data = [
            {"Country Name": row["Country Name"], "2016": row["2016"]}
            for row in reader
            if row.get("2016") and float(row["2016"]) > threshold
        ]

    # Запис результатів у файл
    with open(output_file, "w", newline="") as csvfile:
        fieldnames = ["Country Name", "2016"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered_data)

    print(f"\nРезультати фільтрації записані у файл: {output_file}")

except FileNotFoundError:
    print(f"Файл '{input_file}' не знайдено. Перевірте наявність файлу у директорії.")
except ValueError:
    print("Введено некоректне значення. Будь ласка, спробуйте ще раз.")
except Exception as e:
    print(f"Сталася помилка: {e}")
