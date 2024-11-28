def calculate_negative_mean(array):
    """Calculate the arithmetic mean of negative elements in the array."""
    negative_numbers = [num for num in array if num < 0]  # Filter negative elements
    if not negative_numbers:
        return 0  # Return 0 if there are no negative elements
    return sum(negative_numbers) / len(negative_numbers)

# Input from the user
try:
    n = int(input("Enter the number of elements in the array: "))
    if n <= 0:
        print("The array size must be greater than zero.")
    else:
        print("Enter the elements of the array:")
        array = [float(input(f"Element {i+1}: ")) for i in range(n)]  # Read N elements
        mean = calculate_negative_mean(array)
        if mean == 0:
            print("There are no negative elements in the array.")
        else:
            print(f"The arithmetic mean of the negative elements is: {mean:.2f}")
except ValueError:
    print("Invalid input! Please enter numeric values.")
