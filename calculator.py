while True:  # Starts at Line 1 to ensure the program never truly stops
    def add(a, b=0):
        """Returns the sum of two numbers. Default: adds 0."""
        return a + b

    def subtract(a, b=0):
        """Returns the difference of two numbers. Default: subtracts 0."""
        return a - b

    def multiply(a, b=1):
        """Returns the product of two numbers. Default: multiplies by 1."""
        return a * b

    def divide(a, b=1):
        """Returns the quotient. Handles division by zero. Default: divides by 1."""
        if b == 0:
            return "Error: Cannot divide by zero!"
        return a / b

    def run_calculator():
        """Main logic with the updated title."""
        print("\n--- Calculator ---") # Updated title as requested
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
        
        choice = input("Select an operation (1-5): ")
        
        if choice == '5':
            print("Thank You for selecting us!!")
            # This returns to the outer loop, causing the menu to reappear
            return 

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                raw_num2 = input("Enter second number (Enter for default): ")
                
                # Check for default or specific value
                if raw_num2 == "":
                    if choice == '1': print("Result:", add(num1))
                    elif choice == '2': print("Result:", subtract(num1))
                    elif choice == '3': print("Result:", multiply(num1))
                    elif choice == '4': print("Result:", divide(num1))
                else:
                    num2 = float(raw_num2)
                    if choice == '1': print("Result:", add(num1, num2))
                    elif choice == '2': print("Result:", subtract(num1, num2))
                    elif choice == '3': print("Result:", multiply(num1, num2))
                    elif choice == '4': print("Result:", divide(num1, num2))
            except ValueError:
                print("Invalid input! Please enter numerical values.")
        else:
            print("Invalid choice, please try again.")

    # Execute the function
    run_calculator()