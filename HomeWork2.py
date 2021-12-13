
########## Task 1 (even with while loop) ###############
num = 10     
while num < 60 or num == 60:
     
    if num % 2 == 0:
        print(num)
    num = num +1 
    
########## Task 2 (even with for loop) ###############
for i in range (10,61):
    if i % 2 == 0:
        print(i)
        
############ Task 3 ################
print('enter a number, if you enter zero the program will close in your face')
 
while True:
    x = float(input())
    if x == 0:
        print('Told u, GoodBye')
        break
