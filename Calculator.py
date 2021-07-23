print("Welcome to my calculator!")

#Creating the inputs, so people can input their own values/integers
x = int(input("Please input your first integer: "))
y = int(input("Please input your second integer: "))

#Creating the operation input, so the people can tell the computer what they want to do.
operation = input("Please input what you want to do.\nAvailable actions are +, -, *, and /\n")

#Defining the functions, so the Addition, Subtraction, Multiplication and Division
def add(x, y):
    print(x + y)
#Defining the addition function.
'''Addition function,
performs addition problems'''


def sub(x, y):
    print(x - y)
#Defining the subtraction function.
'''Subtract function,
performs subtraction problems'''

def multiply(x, y):
    print(x * y)
#Defining the multiplication function.
'''Multiplication function,
performs multiplication problems'''

def divide(x, y):
    print(x / y)
#Defining the division function.
'''Division function,
performs division problems'''

#Here comes the if statement part, telling the computer what to do, you'll see.

if operation == '+':
    add(x, y)
#Telling the computer, if the user inputs '+' (in the operator input), then perform the add function.

elif operation == '-':
    sub(x, y)
#Telling the computer, if the user inputs '-', (in the operation input), then perform the subtraction function

elif operation == '*':
    multiply(x, y)
#Telling the computer, if the user inputs '*' (in the operation input), then perform the multiplication function

elif operation == '/':
    divide(x, y)
#Telling the computer, if the user inputs '/' (in the operation input), then perform the division function
