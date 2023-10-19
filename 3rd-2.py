import time
startTime = time.time()
num = 10
#num = int(input("Enter factorial number : "))

for j in range( num):
    fact = 1
    for i in range(2,num+1):
        fact *= i
    print("factorial of ",i,":",fact)
endTime = time.time()
print((endTime-startTime) * 10**3)