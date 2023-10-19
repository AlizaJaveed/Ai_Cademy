print("QUESTION 1")
# Python evaluation questions
# 1. Write a function which will take an integer as input and print each digit in a separate
# line. You are not allowed to use str or any other method will convert the integer into
# string.
# Input: 1011
# Output:
# 1
# 1
# 0
# 1
def separate(num):
    while(num != 0 ):
        num1 = num % 10
        num = num//10
        print(num1 , end = "")
num= int(input("Enter number : "))
separate(num)
print("\nQUESTION 3")
# QUESTION 3
# You are given a positive integer. You can only use one for loop and one print
# statement. Print a numerical triangle of height like the one below:
# Input:
# 5
# Output:
# 1
# 22
# 333
# 4444
num = int(input("Enter numerical triangle of height : "))
for i in range(1 ,num):
    print(i * ((10**i-1)//9))
    
def parwaz(number):
    sum = 0
    for num in range(len(number)):
        while number[num] > 0:
            sum += number[num]
            break
    print(sum)
num = [12,32,-12,3]
parwaz(num)
