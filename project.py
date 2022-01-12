# First project 

import math
import random 
#import turtle

#then a code for running the Scientific Calculator

def askForNumInput(textPrompt):
    # Devine local variable
    convertedNum = math.nan

    # Wait for valid numerical input 
    while True:
        num = input(textPrompt)
        try:
            # Try to typecast the input to a float
            float(num)
        except ValueError:
            # Catch the exception if it is not a number
            print("Sorry ERROR: Syn: it is Invalid Num")
        else:
            # Typecasting
            convertedNum = float(num)
            break
    return convertedNum


# the point here is to give a hints for the code user for how to use all the operators, in case he is not fimilar with it. 

def Ideas ():
    print("+...Addition")
    print("-...Subtraction")
    print("*...Multiplication")
    print("/...Division")
    print("^...Powers")
    print("asin...Arc Sine")
    print("acos...Arc Cosine")
    print("atan...Arc Tangent")
    print("log10...Log(10) of Input")
    print("log...Returns The Apropriate Log of the Input (input1 is the log power)")
    print("rand...Returns A Random Number Between 0 and 1")
    print("d/r...Degrees To Radians")
    print("/-...Square Roots ")
    print("!...Factorials (Input Cannot Be Negetave)")
    print("Abs...Absolute Value")
    print("cos...Cosine")
    print("tan...Tangent")
    print("r/d...Radians To Degrees")
    print("pi...Returns PI")
    print("e...Returs 'e'")
    print("tau...Returns TAU (2xPI)")
    print("M+...Save input to memory")
    print("MR...Recall Memory")
    print("M-...Clear Memory")
    print("sin...Sine")

#while loop to define the operators out side the mentioned list above, incase the user wants to do something unusual with the calculator  
    
while True:
    operator = input("What do you like to do more wild .. i mean operators  ? ")
    # Is operator == to any of out constants or predefines?
        
    if operator == "help":
        Ideas()
    #extra list for showing the code user the build in operators to be used. 
    elif operator == "pi":
    #pi operator 
        print(math.pi)
    elif operator == "rand":
        print(random.random())
    elif operator == "e":
    #exponential operator
        print(math.e)
    elif operator == "M-":
    #for memory evacuation
        memStore = "Empty"
        print("Memory Cleared")
    elif operator == "tau":
    #tau operator 
        print(math.pi*2)
    #when the user enter a defined valid operator which is listed below. 
    #all the mentioned operators in the defined function (Idea)
    elif operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "^" or operator == "/-" or operator == "!" or operator == "Abs" or operator == "d/r" or operator == "r/d" or operator == "M+" or operator == "M-" or operator == "MR" or operator == "sin" or operator == "cos" or operator == "tan" or operator == "asin" or operator == "acos" or operator == "atan" or operator == "log10" or operator == "log" :
        break
    else:
        #when the code user write anything outside the given list
        print("Invalid Operator, try again please")
         
#while loop for looping the inputs form the user depending on the permitted limit for each function 
while True:
    num1 = askForNumInput("First Number? ")
    # Catch asin and acos out of bounds error case
    if (operator == "asin" or operator == "acos") and (num1 > 1 or num1 < -1):
        print("ERROR: Math: 'asin' and 'acos' commands only accept inputs in range -1 to +1, try again please!")
    elif operator == "!" and num1 < 0:
        print("ERROR: Math: Factorials only accept inputs > 0, try again please!")
    else:
        break

if not (operator=="/-" or operator=="!" or operator=="Abs" or operator=="d/r" or operator=="r/d" or operator=="M+" or operator=="sin" or operator=="cos" or operator=="tan" or operator=="asin" or operator=="acos" or operator=="atan" or operator=="log10"):
    # Loop for 2nd number input
    while True:
        num2 = askForNumInput("Second Number? ")
        # Catch x/0 mathmatical error case
        if  operator == "/" and num2 == "0":
            print("ERROR: Math: Canot divide by 0!")
        else:
            break
            
# normal if conditional cases for all the operators, 
if operator == "+":
    output = num1 + num2
    print("Your Answer: "+str(output))
elif operator == "-":
    output = num1 - num2
    print("Your Answer: "+str(output))
elif operator == "*":
    output = num1 * num2
    print("Your Answer: "+str(output))
elif operator == "/":
    output = num1 / num2
    print("Your Answer: "+str(output))
elif operator == "^":
    output = math.pow(num1,num2)
    print("Your Answer: "+str(output))
elif operator == "/-":
    output = math.sqrt(num1)
    print("Your Answer: "+str(output))
elif operator == "!":
    output = math.factorial(num1)
    print("Your Answer: "+str(output))
elif operator == "Abs":
    output = math.fabs(num1)
    print("Your Answer: "+str(output))
elif operator == "d/r":
    output = math.radians(num1)
    print("Your Answer: "+str(output))
elif operator == "r/d":
    output = math.degrees(num1)
    print("Your Answer: "+str(output))
elif operator == "M+":
    memStore = num1
    print("Number Stored")
elif operator == "sin":
    output = math.sin(num1)
    print("Your Answer: "+str(output))
elif operator == "cos":
    output = math.cos(num1)
    print("Your Answer: "+str(output))
elif operator == "tan":
    output = math.tan(num1)
    print("Your Answer: "+str(output))
elif operator == "asin":
    output = math.asin(num1)
    print("Your Answer: "+str(output))
elif operator == "acos":
    output = math.acos(num1)
    print("Your Answer: "+str(output))
elif operator == "atan":
    output = math.atan(num1)
    print("Your Answer: "+str(output))
elif operator == "log10":
    output = math.log10(num1)
    print("Your Answer: "+str(output))
elif operator == "log":
    output = math.log(num2, num1)
    print("Your Answer: "+str(output))
elif operator == "randint":
    output = random.randint(num1, num2)
    print("Your Answer: "+str(output))

#Thank you Dr. Amir 