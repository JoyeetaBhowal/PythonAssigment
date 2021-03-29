# 1. Write a program in Python to allow the error of syntax to be handled using exception handling.

while True:
    try:
        a = int(input("Please enter a number: "))
        print(" root of %s is %s" % (a, a ** 0.5))
        break
    except SyntaxError:
        print("Please enter a valid number!")

# 2. Write a program in Python to allow the user to open a file by using the argv module. If the entered name is
# incorrect throw an exception and ask them to enter the name again.

import sys
file = sys.argv[1]
try:
    f = open(file, 'r')
    s = f.readline()
    i = int(s.strip())
    print("File opened. Ready to write.")
    f.close()
except IndexError:
    print("Enter filename after program filename.")
except IOError:
    print("File not found")

# 3. Write a program to handle an error if the user entered a number more than four digits it should return “The
# length is too short/long !!! Please provide only four digits.

val = int(input("Enter a four digit number: "))
try:

    if val < 1000 or val > 9999:
        raise Exception('The length is too short/long !!! Please provide only four digits.')
    else:
        print("You have entered", val)
except Exception as i:
    print(i)

# 4. Create a login page backend to ask users to enter the username and password. Make sure to
# ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
# should not be more than 3 times.

count = 0
while True:
    userName = input("Hello! Welcome to Chat Nap! \n\n Please enter your Username: ")
    password = input("Enter your Password: ")
    count += 1
    if count == 3:
        print("You have entered maximum number of retry Account has been blocked")
        break
    else:
        if userName == 'joy' and password == 'python':
            print("Welcome to Chat Nap!!")
            break
        else:
            print("You have entered wrong password or username")

# 6. Read doc.txt file using Python File handling concept and return only the even length string from the file.

file = open("python.txt", 'r')
val = file.read()
for i in val.split():
    if len(i) % 2 == 0:
        print(i)
file.close()
