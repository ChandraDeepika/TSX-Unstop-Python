#-----------------------------------------------Topic-1----------------------------------------------
# This is a simple Python script that prints your name and a greeting

# Print your name
print("My name is Chandra Deepika")  # This line displays your name

# Print a greeting message
print("Hello! Nice to meet you.")  # This line displays a friendly greeting


#------------------------------------------Topic-2---------------------------------------------------------
#--> 1. Area and Perimeter of a Rectangle

# Variables for length and width
length = 10
width = 5
# Calculating area and perimeter
area = length * width
perimeter = 2 * (length + width)
# Display the results
print(f"Length: {length}, Width: {width}")
print(f"Area of the rectangle: {area}")
print(f"Perimeter of the rectangle: {perimeter}")

#--> 2. Compare Two Numbers

# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Compare the numbers
if num1 > num2:
    print("The first number is greater than the second.")
elif num1 < num2:
    print("The first number is less than the second.")
else:
    print("Both numbers are equal.")
    
#--> 3. Leap Year Checker

# Input year
year = int(input("Enter a year: "))
# Leap year condition
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    
#--> 4. Experimenting in the Interpreter
#Run the following lines one at a time in the Python interpreter:
# Arithmetic Operators
5 + 3
10 - 2
4 * 3
9 / 2
9 // 2
5 ** 2
10 % 3
# Logical Operators
True and False
True or False
not True
# Comparison
7 > 5
10 == 10
4 != 3

#--> 5. Concatenate Two Strings

# Define two strings
first_name = "Chandra"
last_name = "Deepika"
# Concatenate with space in between
full_name = first_name + " " + last_name

# Print the result
print("Full Name:", full_name)
