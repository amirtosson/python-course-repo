# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 10:31:48 2022

@author: HP
"""
  

import math


#the basic calculator class
class Basic:
    number1 = 0
    number2 = 0
    operation = 'x'

    def __init__(self,num1,num2,oper):
        self.number1 = num1
        self.number2 = num2
        self.operation = oper
    
    def printresult(self):
        result = 0
        if self.operation == '+':
            result = self.number1 + self.number2
        elif self.operation == '-':
            result = self.number1 - self.number2
        elif self.operation == '*':
            result = self.number1 * self.number2
        elif self.operation == '/':
            if self.number2 == 0: #Condition for dividing by zero
                print ('Cannot divide by zero!')
                return 0
            else:    
                result = self.number1 / self.number2
        print('\nThe result = ', result)   
 
        
#the Scientific Calculator class 
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

#the Advanced Calculator class             
class Advanced:
    numbers = []
    operators = []
    
    def __init__(self,nums,ops):
        self.numbers = nums
        self.operators = ops
    
    def printresult(self):
        result = numbers[0]
        j = 1
        for i in self.operators:
            if i == '+':
                 result = result + self.numbers[j]  
                 j = j+1
            elif i == '-':
                 result = result - self.numbers[j]  
                 j = j+1       
            elif i == '*':
                 result = result * self.numbers[j]  
                 j = j+1   
            elif i == '/':
                if self.numbers[j] == 0:
                    print('Cannot divid by zero')
                    return 0
                else:
                    result = result / self.numbers[j]  
                    j = j+1   
        print('\nThe result = ', result)   
    
        
def basic_calc(input_operation):
       
    if input_operation in ('+','-','*','/'):

        input_number1 = float(input('Enter the first number  '))
        input_number2 = float(input('Enter the second number  '))
        calc_basic = Basic(input_number1,input_number2,input_operation)  
        calc_basic.printresult()   
    else:
        print('Invalid Operation')
def sci_calc(input_operation):
   
    if input_operation in ('R', 'P','Sin','Cos'):
        input_number = float(input('Enter the number  '))
        calc_sci = Scientific(input_number,input_operation)  
        calc_sci.printresult()
    else:
        print('Invalid Operation')

while True:   
     
    input_calc = str(input('Enter the calculator type:\n Basic(B)\n Scientific(S)\n Advanced(A)\n To Exit enter E\n '))
    if input_calc in ('B','A','S','E'):
        if input_calc == 'E':
            print(' See you soon!')
            break; 
            
        elif input_calc == 'B': 
            input_operation = str(input('Enter the operation: \n Plus(+)\n Minus(-)\n Multiply(*) \n Divide(/)\n '))
            basic_calc(input_operation) 
       
        elif input_calc == 'S': 
            input_operation = str(input('Enter the operation: \n Plus(+)\n Minus(-)\n Multiply(*) \n Divide(/)\n Root(R)\n Power(P)\n Sin(Sin)\n Cos(Cos)\n'))
           
            if input_operation in ( '+', '-', '*', '/'):
                basic_calc(input_operation)
            else:
                sci_calc(input_operation)
                
        elif input_calc == 'A':
            numbers = []
            num_of_numbers = int(input('How many number?\n '))
            print('Enter the numbers (one after the other): ')
            for i in range (0,num_of_numbers):
                input_numbers = float(input())
                numbers.append(input_numbers)
                    
            operations = []
            print('Enter the',len(numbers)-1,'operations: ')        
            for i in range(0,len(numbers)-1):
                m = input()
                operations.append(m)
            
            calc_advanced = Advanced(numbers,operations)  
            calc_advanced.printresult() 
        
    else:
           print('Invalid Option')


