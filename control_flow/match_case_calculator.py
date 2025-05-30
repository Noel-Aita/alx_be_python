

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation(+, -, *, /): ")

if operation == "+":
            addition = num1 + num2
            print("The result is ",+ addition)

elif operation == "-":
            subtraction = num1 - num2
            print("The result is ",+ subtraction)

elif operation == "*":
            multiplication = num1 * num2
            print("The result is ",+ multiplication)

elif operation == "/": 
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        division = num1 / num2 
        print("The result is ",+ division)
    
    

 # else:
  #  print("The result is ",+ result)
  
