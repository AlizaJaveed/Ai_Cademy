#Problem 3:
#Write a program that does the following:
#1. Asks the user to enter a number greater than 2
#2. Pass this number to a function that generates a list of random numbers (values ranging
#between -100 and 100) with a length matching the user’s input
#3. Prints the resulting list, as well as the minimum and maximum values in the list
#Example output:
#Please enter a number: 5
#Your list = [-2, 89, -24, 40, 28]
#Maximum = 89, Minimum = -24
import random
def function():
    num2 =[]
    num = int(input("Please enter a number: "))
    for i in range(num):
        num1 = random.randrange(-100 , 100)
        num2.append(num1)
    print("Your list = ",num2)
    maximum = num2[0]
    minimum = num2[0]
    for i in range(1 ,len(num2)):
        
        if num2[i]>minimum:
            maximum = num2[i]
        else:
            minimum = num2[i]
    print("Maximum = ",maximum )
    print("Minimum =",minimum )
function()