size = int(input("Enter the size of t5he pattern: ")) #asks the user to put the positive number

while size <= 0:
    print("Please enter a positive integer.")
    size = int(input("Enter the size of the pattern: "))

row = 0 # initiate row counter
# use a while loop to iterate through each row
while row <size:
    for col in range(size):
        print("*",end="")  #prints asterick without newline
    print() # moves to the next line after each row

    row += 1
