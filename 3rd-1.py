# choice = "y"
# while(choice == "y"):
#     num=int(input("Enter a number:"))
#     if num>1:
#         for i in range(2,num):
#             if(num%i)==0:
#                 print(i,"is a prime number")
#         else:
#             print(num,"is not a prime number")
#     else:
#         print(num,"is neither prime nor composite")
#     choice = input("Enter y/n: ")
num=int(input("Enter a number:"))
if num>1:
    for i in range(2,num):
        if(num%i)==0:
           print( num ,"is not a prime number")
           break
          
    else:
       print(num,"is a prime number")
else:
   print(num,"is neither prime nor composite")
# num = 13
# isprime = True
# if num == 1:
#     isprime = False
# for i in range(2,num):
#     if(num%i)==0:
#         isprime = False
#         break
# if isprime  == True:
#     print(num,"is a prime number")
# else:
#     print(num,"is not a prime number")
    