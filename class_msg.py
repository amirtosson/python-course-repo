#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 15:09:30 2022

@author: marialompe
"""


class msg:
    def calculator_msg(self, input):
         if input == "B":
              return "Select operation to perform:\n1. +, 2. -, 3. x 4. /"
         elif input == "S":
              return "Select operation to perform:\n1. +, 2. -, 3. x 4. /, 5. sqrt, 6. sin, 7. cos"
         elif input == "A":
              return "Type calculation"