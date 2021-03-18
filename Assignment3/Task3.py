# Create a list of 10 elements of four different data types like int, string, complex and float.
List = [1, 2.2, (3 + 4j), "hello", "world", 6, 7.1, 8, 1.9]

# Create a list of size 5 and execute the slicing structure.

List = [1, 2, 3, 4, 5]
print(List[2:4])

# Write a program to get the sum and multiply of all the items in a given list.

List1 = [1, 3, 5, 10]

addition = sum(List1)

print("Added value of List:", addition)

multi = 1
for i in List1:
    multi = i * multi
print("Multiplied value of List:", multi)

# Find the largest and smallest number from a given list.

List2 = [6, 9, 6, 4, 12, 47, 3]

MaxVal = max(List2)
print("Maximum value in List: ", MaxVal)

MinVal = min(List2)
print("Minimum value in List: ", MinVal)

# Create a new list which contains the specified numbers after removing the even numbers from a predefined list.


List3 = [1, 3, 2, 5, 9, 12, 13, 14, 19]
OddVal = []
for i in range(len(List3)):
    if List3[i] % 2 != 0:
        OddVal.append(List3[i])
print(OddVal)

# Create a list of elements such that it contains the squares of the first and last 5 elements between 1 and30 (both
# included).

a = range(1, 31)[:5]
b = range(1, 31)[25:31]

square = []

for i in a:
    square.append(i * i)

for i in b:
    square.append(i * i)

print(square)

# Write a program to replace the last element in a list with another list.

List1 = [1, 3, 5, 7, 9, 10]
List2 = [2, 4, 6, 8]

List1[-1:] = List2
print(List1)

# Create a new dictionary by concatenating the following two dictionaries:
# Sample input: a={1:10,2:20} b={3:30,4:40}
# Expected output: {1:10,2:20,3:30,4:40}

x = {1: 10, 2: 20}
y = {3: 30, 4: 40}
x.update(y)
print(x)

# Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
# and n(both 1 and n included).

x = {}
for i in range(1, 6):
    x[i] = i * i
print(x)

# Write a program which accepts a sequence of comma-separated numbers from console and
# generates a list and a tuple which contains every number in the form of string.

val = input("Enter a sequence 5 numbers with comma: ").split(',')

List = list(val)
print(List)

List1 = tuple(val)
print(List1)
