#Problem 4:
# Write a program that updates a list of strings by completing the following steps:
# 1. Create a list with at least 5 strings
# 2. Print the contents of the list
# 3. Pass the list to a function that uses a for loop to update each item in the list by adding any
# new character
# 4. Print the contents of the list again
# Example output:
# ['one', 'two', 'three‘,’four’,’five’]
# ['oneA', 'twoA', 'threeA‘,’fourA’,’fiveA’]
def function(string):
    listofStr = []
    for i in range(len(string)):
        a = string[i]
        b = a+"A"    
        listofStr.append(b)
    print(listofStr)
listOfString = ['one', 'two', 'three','four','five']
print(listOfString)
function(listOfString)

def function(string):
    listofStr = []
    for i in range(len(string)):
        a = string[i]
        b = a+"A"
        
        print(b, end = "")
        print()
listOfString = ['one', 'two', 'three','four','five']
print(listOfString)
function(listOfString)
