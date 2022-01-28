#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 15:07:59 2022

@author: marialompe
"""

from class_basic import basic
cal = basic()
from class_scientific import scientific
sc = scientific()
from class_msg import msg
ms = msg()

def call_operation_2arg(operation_type, num1, num2):
        if operation_type == "1":
         cal.adding(num1, num2)
        elif operation_type == "2":
         cal.subtraction(num1, num2) 
        elif operation_type == "3": 
         cal.multiplication(num1, num2)
        elif operation_type == "4":
         cal.division(num1, num2)
         
def call_operation_1arg(operation_type, num1):
    if operation_type == "5": 
         sc.sqrt(num1)
    elif operation_type == "6":
         sc.sin(num1)
    elif operation_type == "7":
         sc.cos(num1)
            
         

calculate_again = True
while calculate_again == True:
    print("Welcome to calculator")
    print("Which calculator you would like to use? B - basic, S - scientific, A - advanced")
    calculator_type = input().upper()
    print(ms.calculator_msg(calculator_type))
    if calculator_type == "A":
        calc = input()
        print("Answer: " + str(eval(calc)))
    elif calculator_type == "B" or calculator_type == "S":
        operation_type = input()
        if int(operation_type) <= 4:
            num1 = float(input("First number: ")) 
            num2 = float(input("Second number: "))
            call_operation_2arg(operation_type, num1, num2)
        else:
            num1 = float(input("Number: "))
            call_operation_1arg(operation_type, num1)
    else:
        cal.no_operation()
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
