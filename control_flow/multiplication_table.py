number = int(input("Enter a number to see its multiplication table: "))

# Show the multiplication table
#print(f"Multiplication Table for {number}:")
for i in range(0,  11): # Starts counting from 0 up to 10 excluding number 11 itself
    print(f"{number} x {i} = {number * i}")