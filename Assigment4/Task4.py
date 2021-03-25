# 1. Write a program to reverse a string.
val = input("Enter string to reverse value:")


def reverse(val):
    return val[::-1]


print(reverse(val))

# 2. Write a function that accepts a string and prints the number of uppercase letters  and lowercase letters.

val = input("Enter string in upper and lowercase:")

a = {"lower": 0, "upper": 0}

for i in val:
    if i.islower():
        a["lower"] += 1
    elif i.isupper():
        a["upper"] += 1
    else:
        pass

print("Total number of uppercase", a["upper"], "\n", "Total number of lower", a["lower"])

# 3. Create a function that takes a list and returns a new list with unique elements of the first list.

input_string = input("Enter a list element separated by space ")
List = input_string.split()


def unique(List):
    new_list = list(set(List))
    return new_list


newList = unique(List)
print(newList)

# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a
# hyphen-separated sequence after sorting them alphabetically.

input_string = input("Enter a sentence use '-' instead of space")
string = input_string.split("-")
string.sort()
string1 = " ".join(string)
print(string1)

# 5. Write a program that accepts a sequence of lines as input and prints the lines after making allcharacters in the
# sentence capitalized.

input_string = input("Enter a sentence:")
newString = input_string.upper()
print(newString)

# 6.Define a function that can receive two integral numbers in string form and compute their sum and print it in the
# console.

input_string = input("Enter first number to add: ")
input_string1 = input("Enter second number to add: ")


def function(i, j):
    a = int(i)
    b = int(j)
    total = a + b
    print(total)


function(input_string, input_string1)


# 7. Define a function that can accept two strings as input and print the string with the maximum length in the
# console. If two strings have the same length, then the function #  should print both the strings line by line


def function(a, b):
    i = len(a)
    j = len(b)
    if i == j:
        print(a)
        print(b)
    elif i > j:
        print(a)
    elif j > i:
        print(b)


a1 = input("Enter first string: ")
a2 = input("Enter second string: ")
function(a1, a2)


# 8. Define a function which can generate and print a tuple where the values are square of numbers between 1 and 20 (
# both 1 and 20 included).

def squares():
    return tuple([i ** 2 for i in range(1, 21)])


print(squares())


