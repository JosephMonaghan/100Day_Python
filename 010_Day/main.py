import os
from art import logo

def add(n1,n2):
    """Adds two number (n1) and (n2) together"""
    result=n1+n2
    return result

def subtract(n1,n2):
    """Substracts two numbers"""
    result=n1-n2
    return result

def multiply(n1,n2):
    """Multiplies two numbers"""
    result=n1*n2
    return result

def divide(n1,n2):
    """Divides two numbers"""
    result=n1/n2
    return result

os.system('Clear')
print(logo)

first_num=float(input("What's the first number?"))

keep_calculating=True
while keep_calculating:
    print("+\n-\n*\n/")
    operation=input("Pick an Operation:\n")
    second_num=float(input("What's the 2nd number?"))

    if operation=="+":
        output=add(first_num,second_num)
    elif operation=="-":
        output=subtract(first_num,second_num)
    elif operation=="*":
        output=multiply(first_num,second_num)
    elif operation=="/":
        output=divide(first_num,second_num)

    print(f"{first_num} {operation} {second_num} = {output}")
    
    user_input=input(f"Type 'y' to keep calculating with {output}, or type 'n' to start a new calculation. (type 'q' to quit)")
    
    if user_input=='y':
        first_num=output
    elif user_input=='n':
        os.system('Clear')
        print(logo)
        first_num=first_num=float(input("What's the first number?"))
    else:
        keep_calculating=False
        