# main.py
import mod

def main():
    try:
        n = int(input("Enter the number of days for training: "))
        if n <= 0:
            print("Number of days must be positive.")
        else:
            total_distance = mod.calculate_total_distance(n)
            print(f"The athlete will run a total of {total_distance:.2f} km in {n} days.")
    except ValueError:
        print("Invalid input! Please enter a positive integer.")

# Run the main program
if __name__ == "__main__":
    main()
