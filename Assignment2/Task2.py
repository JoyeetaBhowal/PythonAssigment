                            #TASK TWOOPERATORS AND DECISION MAKING STATEMENT
# 1. Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print “Consultadd” as a string
# If a number is divisible by 5 it should print “Python Training” as a string
# If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as astring.

val = int(input(" Enter any Positive Number : "))

if((val % 3 == 0) and (val % 5 == 0)):
    print("Consultadd - Python Training")
elif(val % 3 == 0):
    print("Consultadd")
elif(val % 5 == 0):
    print("Python Training")
else:
    print("Entered Number {0} is Not Divisible by 3 and 5".format(val))

# 2. Write a program in Python to perform the following operator based task:
# Ask user to choose the following option first:
# If User Enter 1 - Addition
# If User Enter 2 - Subtraction
# If User Enter 3 - Division
# If User Enter 4 - Multiplication
# If User Enter 5 - Average
# Ask user to enter two numbers and keep those numbers in variables num1 and num2
# respectively for the first 4 options mentioned above.
# Ask the user to enter two more numbers as first and second for calculating the average as soon as
# the user chooses an option 5.At the end if the answer of any operation is Negative print a
# statement saying “NEGATIVE” NOTE: At a time a user can only perform one action.

print("Enter any 2 Number")
num1= int(input("Enter the 1st number: "))
num2= int(input("Enter the 2st number: "))


print(" Enter 1 for Addition\n Enter 2 for Subtraction\n Enter 3 for Division\n Enter 4 for Multiplication\n Enter 5 for Average")

act = int(input("Enter a Action Number: "))

if act == 1:
    result = num1 + num2

elif act == 2:
    result = num1 - num2

elif act == 3:
    result = num1 * num2

elif act == 4:
    result = num1 / num2

elif act == 5:
    num3 = int(input("Enter 3rd number: "))
    num4 = int(input("Enter 4th number: "))
    result = (num1 + num2 + num3 + num4) / 4

else:
    print("You entered wrong number.")

if result < 0:
    print("NEGATIVE")
else:
    print(result)

 # 3. Write a program in Python to implement the given flowchart:
print("Enter 3 values")

a = int (input("Enter the 1st number: "))
b = int (input("Enter the 2nd number: "))
c = int (input("Enter the 3rd number: "))

avg = (a + b + c)/3
print("Average is: ", avg)

if ((avg>a) and (avg>b) and (avg>c)):
    print("Average value is higher than a, b and c.")
elif ((avg>a) and (avg>b)):
    print("Average value is higher than a and b.")
elif ((avg>a) and (avg>c)):
    print("Average value is higher than a and c.")
elif((avg>c) and (avg>b)):
    print("Average value is higher than b and c.")
elif (avg>a):
    print("Average value is just higher than a.")
elif (avg>b):
    print("Average value is just higher than b.")
else:
    print("Average value is just higher than c.")

# 4. Write a program in Python to break and continue if the following cases occurs:
# If user enters a negative number just break the loop and print “It’s Over”
# If user enters a positive number just continue in the loop and print “Good Going”

val = int(input("Enter a number: "))
while True:
    if val < 0:
        print("It's over")
        break
    else:
        print("Good Going")

# 5. Write a program in Python which will find all such numbers which are divisible by 7
#  but are not a multiple of 5, between 2000 and 3200.

for a in range(2000, 3200):
    if (a%7==0) and (a%5!=0):
        print(a)

#6. What is the output of the following code examples
#x=123
#for i in x:
#   print(i)
#Result:  Error: int object is not iterable

#
#i= 0
#while i < 5:
    #print(i)
    #i += 1
    #if i == 3:
    #    break
    #else:
    #    print('Error')
# Result:
# 0
# error
# 1
# error
# 2
# error

#count = 0
#while True:
#   print(count)
#   count += 1
#   if count >= 5:
#       break
#Result:
#0
#1
#2
#3
#4

# 7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.Expected output: 0 1 2 4 5
# Note: Use ‘continue’ statement

for x in range(7):
    if x == 3 or x == 6:
        continue
    print(x, end=' ')
