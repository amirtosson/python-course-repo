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
  
#%%%%%%%%%%%%%%%%%%%%%%%%%%%
# my array from 10 to 60
my_arr = range(10,61)

# using for loop
for x in my_arr:
    if x % 2 == 0:
        print('from for loop: ' + str(x))
    else:
        print("from for loop: ODD")
        

u = 10
# using while loop
while u < 61:  
    if u % 2 == 0:
        print('from while loop: ' + str(u))
    else:
        print("from while loop: ODD")
        
    u = u + 1
    
#%%%%%%%%%%%%%%%%%%%

u=10
while u<61:
    if u%2==0:
        print(u)
    
    else:
        print("odd")
        
    u=u+1
    
#%%%    

x= int("Hi")

print(type(x))




































    
        
    
