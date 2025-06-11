def safe_divide(numerator, denominator):
    # the numerator must be greater than the denominator
    # non of the numbers should be zero
    # non of the numbers should be nothing other than a string
    try:
        num = float(numerator)
        denom = float(denominator)

        result = num/denom
        return f"The result of the vision is {result}"

        
       
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."