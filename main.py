"""
@author:    Python Course
@license:   GNU General Public License v3 or higher
@copyright: Universität Siegen, Deutschland
@email:     tosson@physik.uni-siegen.de
"""

"""
summary:    A testing file  
name:       main
date:       16.12.2021
"""

is_not_zero = True
counter = 0

while is_not_zero == True and counter < 100:
    x = int(input("Enter any number. If you entered 0 I will close "))  
    if x == 0:
        print("Zero")
        is_not_zero = False
    
    else:
        print("other")
        
    counter = counter + 1
    
    
    
    
    