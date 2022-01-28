#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 15:14:55 2022

@author: marialompe
"""

class scientific(object):
    def adding(self, num1, num2): 
        answer = num1 + num2
        print(answer)
    def subtraction(self, num1, num2):
        answer = num1 - num2
        print(answer)
    def multiplication(self, num1, num2):
        answer = num1*num2
        print(answer)
    def division(self, num1, num2): 
        answer = num1/num2
        print(answer)
    def sqrt(self, num): 
       import math
       answer = math.sqrt(num)
       print("Square root of is: ", answer)
    def sin(self, num):
       import math 
       answer = math.sin(math.radians(num))
       print("Sine (%f) =%f" %(num,answer)) 
    def cos(self, num):
       import math
       answer = math.cos(math.radians(num))
       print("Cos (%f) =%f" %(num,answer))