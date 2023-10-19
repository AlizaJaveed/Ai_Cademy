import time
startTime = time.time()
num = 2005
for i in range(500):
    if (num % 4 == 0):
        if (num % 100 != 0) or (num % 400 == 0):
     
            print("leap year")
        else:
            print("Not leap year")
    else:
        print("Not leap year")
endTime = time.time()
print((endTime-startTime)* 10**3)
# import time
# startTime = time.time()
# num = 2004#int(input("Enter year:"))
# for i in range(50000):
#     if (num % 4 == 0)and( (num % 100 != 0) or (num % 400 == 0)):
#         print("leap year")
#     else:
#         print("Not leap year")
# endTime = time.time()
# print((endTime-startTime)* 10**3)