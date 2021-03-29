# 1. Write a program in Python to find out the character in a string which is uppercase using listcomprehension.\
str = input("Enter a sentences:")
print([i for i in str if i.isupper()])

# 2. Write a program to construct a dictionary from the two lists containing the names of students andtheir
# corresponding subjects. The dictionary should map the students with their respective subjects.Let’s see how to do
# this using for loops and dictionary comprehension.

students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']
dictionary = dict(zip(students, subjects))
print("Resultant dictionary is : ", dictionary)


# 4.Write a program in Python using generators to reverse the string.Input String = “Consultadd Training”.

def reverseStr(myStr):
    length = len(myStr)
    for i in range(length - 1, -1, -1):
        yield myStr[i]


for char in reverseStr("ConsultAdd Training"):
    print(char)

# 5. Write an example on decorators.

a = input("Enter a number from 1 to 9")
b = input("Enter a number from 1 to 9")


def make_pretty(func):
    def inner():
        print("let's get decorated")
        func()
        print("I am decorated now, How do i look?")

    return inner()


@make_pretty
def ordinary():
    print("I am still ordinary")
