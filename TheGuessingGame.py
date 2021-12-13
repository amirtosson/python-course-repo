import random
 

print('enter a range of integers')
a = int(input('from '))
b = int(input('to '))

randnum = random.randint(a, b) 
#print('the number = ', randnum)   #This line here is to test the code

print('now guess an integer inside your range')

iterations = 1   #the number of trials 
while True:
    guess = int(input())
    if guess > b or guess < a:
        print('the number is out of your range u dumbass!')
    else:
        if guess > randnum:
            print('it is high, guess again')
        elif guess < randnum:
            print('it is low, guess again')
        else:
            print('The number is correct, nice! u got it after number of trials = ', iterations)
            break        
    iterations = iterations + 1
