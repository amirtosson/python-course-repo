#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 13:10:06 2022

@author: marialompe
"""

def adding(): 
    num1 = float(input("First number: ")) 
    num2 = float(input("Second number: ")) 
    print(float(num1) + float(num2))
    return None 
def substraction():
    num1 = float(input("First number: ")) 
    num2 = float(input("Second number: ")) 
    print(float(num1) - float(num2)) 
    return None 
def multiplication():
    num1 = float(input("First number: ")) 
    num2 = float(input("Second number: ")) 
    print(float(num1) * float(num2))
    return None 
def division(): 
    num1 = float(input("First number: ")) 
    num2 = float(input("Second number: "))
    while num2 == 0:
        num2 = float(input("Second number (you can't divide by 0): "))
    print(float(num1) / float(num2))
    return None 
def sqrt():
    import math 
    num1 = float(input("Enter the number: ")) 
    result = math.sqrt(num1)
    print("Square root of",num1, "is: ", result)
    return None 
def sin():
    import math 
    a = eval(input("What is the angle measure?"))
    result = math.sin(math.radians(a))
    print(str(round(result,3)))
    return None 
def cos():
    import math
    a = eval(input("What is the angle measure?"))
    result = math.sin(math.radians(a))
    print(str(round(result,3)))
    return None 
def no_operation():
    print("You did not choose any operation") 
    return None
    
def calculator_msg(calc):
    if calc == "B":
        return "Select operation to perform:\n1. +, 2. -, 3. x 4. /"
    elif calc == "S":
        return "Select operation to perform:\n1. +, 2. -, 3. x 4. /, 5. sqrt, 6. sin, 7. cos"
    elif calc == "A":
        return "Type calculation"
        
def call_operation(operation_type):
    if operation_type == "1":
        adding() 
    elif operation_type == "2":
        substraction() 
    elif operation_type == "3": 
        multiplication()
    elif operation_type == "4":
        division()
    elif operation_type == "5": 
        sqrt()
    elif operation_type == "6":
        sin()
    elif operation_type == "7":
        cos()
    else: 
        no_operation()


calculate_again = True
while calculate_again == True:
    print("Welcome to calculator")
    print("Which calculator you would like to use? B - basic, S - scientific, A - advanced")
    calculator_type = input().upper()
    print(calculator_msg(calculator_type))
    if calculator_type == "A":
        calc = input()
        print("Answer: " + str(eval(calc)))
    elif calculator_type == "B" or calculator_type == "S":
        operation_type = input()
        call_operation(operation_type)
    else:
        no_operation()
    calculator = True
    while calculator == True:
            calculate_again = input("Do you want to calculate again? y = yes, n = no ")       
            if calculate_again == "y": 
                print("Ok. You can use calculator again")
                calculator = False
                calculate_again = True
            elif calculate_again == "n":
                print("Ok. Sayonnara")
                play_again_user = False
                calculator = False
            else:
                no_operation()
