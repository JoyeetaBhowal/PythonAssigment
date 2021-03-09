# 1. Create three variables in a single line and assign values to them in such a manner that each one ofthem belongs
# to a different data type.

a, b, c = 1, 2.01, 'string'
print(a, b, c)

# 2. Create a variable of type complex and swap it with another variable of type integer.

a = (3 + 6j)
b = 1

print("Before swapping: ")
print(a, b)

# code to swap 'a' and 'b'
a, b = b, a

print("After swapping: ")
print(a, b)

# 3. Swap two numbers using a third variable and do the same task without using any third variable.
a = 2
b = 10

# create a temporary variable and swap the values
temp = a
a = b
b = temp

print('value of a after swapping: {}'.format(a))
print('value of b after swapping: {}'.format(b))
# Swap value without using any third variable.
a = 3
b = 1

print("Before swapping: ")
print(a, b)

# code to swap 'a' and 'b'
a, b = b, a

print("After swapping: ")
print(a, b)

# 4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.xVersion.

value = input("Enter your value: ")
print("You have entered " + value)

# 5. Write a program to complete the task given below:Ask users to enter any 2 numbers in between 1-10 , add the two
# numbers and keep the sum in another variable called z. Add 30 to z and store the output in variable result and print
# result as the final output.

print("Select two number between 1-10")
val1 = input("Enter First number: ")
val2 = input("Enter second number: ")

z = int(val1) + int(val2)

result = z + 30

print(result)

# 6. Write a program to check the data type of the entered values.HINT: Printed output should say -The data type of
# the input value is : int/float/string/etc.

print("Enter a value")
val = input("Enter Value: ")

print("The data type of variable a is", type(val))

# 7.Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase andUPPERCASE

st = input("Enter a Word: ")

print("entered value in lower", st.lower())

print("entered value in Upper", st.upper())

# 8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’again.
# Will it change the value? If Yes then Why?
variable = 5
variable = "Python"
# Ans. Yes, variables in Python can be reassigned to a new value that is a different data type from its current value.
# Because variables are like an empty box, that can contain something like a string, number, or other value.
