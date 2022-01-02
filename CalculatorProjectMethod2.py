# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 16:43:57 2022

@author: A.A.Mohamed
"""

import math 

#The Basic calculator class
class Basic:
    number1 = [3]

    def __init__(self,num1):
        self.number1 = num1
    
    def printresult(self):
        result = 0
        full_str = ''.join([str(elem) for elem in self.number1])
        result = eval(full_str)
        print('\nThe result of (',full_str,') = ', result) 

#The Scientific calculator class
class Scientific:
    
    number = 0
    operation = 'x'
    
    def __init__(self,num,oper):
        self.number = num
        self.operation = oper
    
    def printresult(self):
        result = 0
        if self.operation == 'R':
            result = math.sqrt(self.number)
        if self.operation == 'P':
            power = int(input('enter the power  '))
            result = self.number**power                                        
        if self.operation == 'Sin':
            result = math.sin(self.number)
        if self.operation == 'Cos':
            result = math.cos(self.number)
        print('\nThe result = ', result)  

#The Advanced calculator class
class Advanced:
    numbers = []    
    def __init__(self,nums):
        self.numbers = nums
    
    def printresult(self):
        result = 0
        full_str = ''.join([str(elem) for elem in self.numbers])
        try:
            result = eval(full_str)
            print('\nThe result of (',full_str,') = ', result) 
        except:
            print('Cannot divide by zero!')
 
#Function to manage the scientific inputs
def sci_calc(input_operation):
   
    if input_operation in ('R', 'P','Sin','Cos'):
        input_number = float(input('Enter the number  '))
        calc_sci = Scientific(input_number,input_operation)  
        calc_sci.printresult()
    else:
        print('Invalid Operation') 
    
 
while True:   
        
 
    input_calc = str(input('Enter the calculator type:\n Basic(B)\n Scientific(S)\n Advanced(A)\n To Exit enter E\n '))
    if input_calc  not in ('B','A','S','E'):
            print('Invalid input')
            continue
    if input_calc == 'E':
                print(' See you soon!')
                break
                
    elif input_calc == 'B': 
                numbers = [0,0,0] #arraay to store the numbers and the operator
                print('Enter the two numbers (one after the other):')
                i = 0
                while i < 3:
                    numbers[i] = input()
                    #The following block is to manage the error inputs
                    try:
                        input_check = float(numbers[i])
                    except:
                        print('Invalid input, please enter a number')
                        continue
                    i = i+2    
                
                print('Enter the operation (use only + , - , * , / )')       
                while True:
                    numbers[1] = input()
                    #The following block is to manage the error inputs
                    if numbers[1] in ('+' , '-' , '*' , '/' ):
                        calc_basic = Basic(numbers)  
                        calc_basic.printresult()
                        break
                    else:
                        print('Ivalid input, enter an allowed operation!')
                
    elif input_calc == 'S': 
            while True:
                input_operation = str(input('Enter the operation: \n Plus(+)\n Minus(-)\n Multiply(*) \n Divide(/)\n Root(R)\n Power(P)\n Sin(Sin)\n Cos(Cos)\n'))
                if input_operation in ( '+', '-', '*', '/'):
                    numbers = [0,0,0]
                    print('Enter the two numbers (one after the other):')
                    #The following block is to manage the error inputs
                    i = 0
                    while i < 3:
                        numbers[i] = input()
                        try:
                            input_check = float(numbers[i])
                        except:
                            print('Invalid input, please enter a number')
                            continue
                        i = i+2   
                    numbers[1] = input_operation
                    calc_basic = Basic(numbers)  
                    calc_basic.printresult()
                    break
                elif input_operation in ( 'R', 'P', 'Cos', 'Sin'):
                    sci_calc(input_operation) 
                    break
                else:
                    print('Ivalid input, enter an allowed operation!')

                
    elif input_calc == 'A':
                numbers = [] #This array will store the numbers and the operators
                while True:
                    try:
                        num_of_numbers = int(input('How many number?\n '))
                        break
                    except:
                        print('Ivalid input, enter a number!')
                    
                print('Enter the numbers (one after the other): ')
                #The following block is to manage the error inputs and fill the array with the numbers first
                i = 0
                while i < num_of_numbers:
                    input_numbers = input()
                    try:
                        float(input_numbers)
                        numbers.append(input_numbers)
                        if i != num_of_numbers-1:
                            numbers.append(0) 
                        i = i+1
                    except:
                       print('Ivalid input, enter a number!')
                       
                
                print('Enter the',num_of_numbers-1,'operations (only +, -, *, /)') 
                i = 1
                while i < len(numbers)-1:
                    m = input()
                    if m in ( '+', '-', '*', '/'):
                        numbers[i] = m #Fill the array with the operators

                        i=i+2                       
                    else: 
                        print('Ivalid input, enter an allowed operation!')
                calc_advanced = Advanced(numbers)  
                calc_advanced.printresult()        
   
        
        
