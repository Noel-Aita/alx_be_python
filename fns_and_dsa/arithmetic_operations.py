def perform_operation():
    print("Arithmetic Operations")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = str(input("Enter Operation (add, subtract, multiply, divide): "))
    if operation == "add":
        add = num1 + num2
        print(f"Result: {add}")
        return add
    elif operation == "subtract":
        subtract = num1 - num2
        print(f"Result: {subtract}")
        return subtract
    elif operation == "multiply":
        multiply = num1 * num2
        print(f"Result: {multiply}")
        return multiply
    elif operation == "divide":
        divide = num1 / num2
        print(f"Result: {divide}")
        return divide
  
    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")
    

perform_operation()

''' 
    if operation == "add":
        add = num1 + num2
        return add
    elif operation == "subtract":
        subtract = num1 - num2
        return subtract
    elif operation == "multiply":
        multiply = num1 - num2
        return multiply
        '''