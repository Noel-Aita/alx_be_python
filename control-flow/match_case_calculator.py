
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation :
        case "*":
            if operation == "*":
                multiplication = num1 * num2
            print("The result is ",+ multiplication)

        case "-":
          if operation == "-":
            subtraction = num1 - num2
            print("The result is ",+ subtraction)
        case "+":
         if operation == "+":
            addition = num1 + num2
            print("The result is ",+ addition)
        
if operation == "/": 
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        division = num1 / num2 
        print("The result is ",+ division)
    
    

 # else:
  #  print("The result is ",+ result)
  

