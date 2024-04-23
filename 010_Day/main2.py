
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


operations={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

import os
from art import logo

def calculator():
    os.system("Clear")
    print(logo)

    num1=float(input("What's the first number?"))
    keep_going=True
    while keep_going:
        for item in operations:
            print(item)
        op=input("Which operation would you like to perform?")

        num2=float(input("What's the 2nd number?"))

        result=operations[op](num1,num2)
        print(f"{num1} {op} {num2} = {result}")
        
        user_input=input(f"Type 'y' to keep calculating with {result}, or type 'n' to start a new calculation. (type 'q' to quit)")
        
        if user_input=='y':
            num1=result
        elif user_input=='n':
            calculator()
        else:
            keep_going=False
            
calculator()