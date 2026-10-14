def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2

def main():
    print("--- Modular Calculator v2.0 ---")
    
    while True:
        # 1. Ask for inputs and prevent crashes if letters are typed
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.\n")
            continue

        # 2. Display the menu
        print("\nChoose operation:")
        print("1 - Addition")
        print("2 - Subtraction")
        print("3 - Multiplication")
        print("4 - Division")
        
        choice = input("Enter choice (1/2/3/4): ").strip()

        # 3. Check choices and calculate
        if choice == '1':
            result = add(num1, num2)
            print(f"Result: {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"Result: {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"Result: {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Result: {result}")
        else:
            print("Invalid choice.")

        # 4. Ask to continue or quit
        print("-" * 30)
        again = input("Do you want to try again? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break
        print("-" * 30 + "\n")

if __name__ == "__main__":
    main()