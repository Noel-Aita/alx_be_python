

FAHRENHEIT_TO_CELCIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    return(fahrenheit - 32) * FAHRENHEIT_TO_CELCIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return(celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp_value =float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit == "F":
            result = convert_to_celsius(temp_value)
            print(f"{temp_value}\u00B0F is {result}\u00B0C")
        elif unit == "C":
            result = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}\u00B0C is {result}\u00B0F")
        #else:
            #print("Invalid unit: Please enter 'F' for Fahrenheit or 'C' for Celsius")
    except ValueError:
        raise ValueError("Invalid temperature: Please enter a numeric value.")
    
if __name__=="__main__":
    main()