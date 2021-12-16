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


        
    
"""
we need a function to gerante a random number (done) (new) 

input from the user (done)

checking:
    1) less than 
    2) greater than 
    3) equal 

count the trials

while loop 

break the condition: trials are more than ten or 
the user found the number  

"""    
    
import random

play_again_user = True

# to ask the user if he/she wants to play again 
# can be broken if the user wrote n
while play_again_user == True:
    print("starting again")
    my_random_number = random.randint(1,100)
    found = False
    counter = 0
    
    # the main loop to get an input from the user and check it 
    # can be broken if the user guessed the right number OR exceed the number 
    # of trials 
    while found == False and counter < 10:
        user_num = int(input("guess a number from 1 to 100 "))
        if user_num > 100 or  user_num < 1:
            print("Are you stupid. Out of range!! ")
        elif user_num == my_random_number:
            print("Bingoooo. ")
            print("You found the right number after " + str(counter+1) + " times")
            found = True
        elif user_num < my_random_number:
            print("It was too less. Please guess a higher num ")
        else:
            print("It was too high. Please guess a smaller num ")  
        counter = counter + 1 
        if counter == 10:
            print("You exceed the number of trials. ")
    
    wrong_choice = True
    # to be sure that the user answerd with the right input
    # can be broken if the user gave n or y 
    while wrong_choice == True:
        play_again = input("Do you want to play again? y = yes, n = no ")       
        if play_again == "y": 
            print("yes")
            wrong_choice = False
        elif play_again == "n":
            print("no")
            play_again_user = False
            wrong_choice = False
        else:
            print("wrong")
        





























