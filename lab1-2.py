# Function to generate the Fibonacci sequence and calculate the sum
def fibonacci_sequence(n):
    fib_numbers = [0, 1]  # Initial two numbers in the Fibonacci sequence
    while len(fib_numbers) < n:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    return fib_numbers, sum(fib_numbers)

# Main program
n = 8  # Number of Fibonacci numbers to generate
fib_numbers, total_sum = fibonacci_sequence(n)

# Display results
print("The first 8 numbers in the Fibonacci sequence are:")
print(fib_numbers)
print(f"The sum of these numbers is: {total_sum}")
