# Function to calculate the value of X
def calculate_x(a, b):
    if a < b:
        return a / b + 5
    elif a == b:
        return -5
    else:  # a > b
        return (a * a - b) / b

# Input from user
try:
    a = float(input("Enter value for a: "))
    b = float(input("Enter value for b: "))

    # Check for division by zero
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        # Calculate and display the result
        x = calculate_x(a, b)
        print(f"The result is: X = {x}")

except ValueError:
    print("Invalid input! Please enter numeric values.")

