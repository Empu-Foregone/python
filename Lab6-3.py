def аналіз_тексту(текст):
    """Аналізує текст та визначає, чи більше голосних чи приголосних."""
    голосні = {'a', 'e', 'i', 'o', 'u', 'y'}  # Множина голосних літер
    приголосні = set('bcdfghjklmnpqrstvwxyz')  # Множина приголосних літер

    # Вибір літер із тексту
    літери = {символ.lower() for символ in текст if символ.isalpha()}  # Унікальні літери у тексті

    if not літери:  # Якщо літер немає
        print("У тексті немає літер.")
        return

    # Підрахунок голосних та приголосних
    кількість_голосних = sum(1 for літера in літери if літера in голосні)
    кількість_приголосних = sum(1 for літера in літери if літера in приголосні)

    # Виведення результатів
    if кількість_голосних > кількість_приголосних:
        print(f"Голосних більше ({кількість_голосних}), ніж приголосних ({кількість_приголосних}).")
    elif кількість_приголосних > кількість_голосних:
        print(f"Приголосних більше ({кількість_приголосних}), ніж голосних ({кількість_голосних}).")
    else:
        print(f"Голосних і приголосних однакова кількість ({кількість_голосних}).")

    # Перетворення множини у список для додаткової обробки
    літери_список = list(літери)
    print("Літери у вигляді множини:", літери)
    print("Літери у вигляді списку:", літери_список)


# Ввід тексту користувачем
текст = input("Введіть текст із цифр та літер латинського алфавіту: ")
аналіз_тексту(текст)
