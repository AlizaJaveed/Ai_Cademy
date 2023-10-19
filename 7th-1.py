import random 
mark = 0
optr = ['+','-','*','//','%','/']
for i in range(3):
    n1 = random.randrange(0,500)
    n2 = random.randrange(0,500)
    op = random.choice(optr)
    actual_answer = n1+n2
    if op == '+':
        ans = n1 + n2
    elif op == '-':
        ans = n1 - n2
    elif op == '*':
        ans = n1 * n2
    elif op == '//':
        ans = n1 // n2
    elif op == '%':
        ans = n1 % n2 
    else:
        ans = n1 / n2
    option = ['a','b','c','d']
    print("Result ", n1, op ,n2 , "Enter your choice? ")
    listOfAns = [ans,random.randrange(0,1000),random.randrange(0,1000),random.randrange(0,1000)]
    random.shuffle(listOfAns)
    for i in range(4):
    
        print(option[i],")",listOfAns[i])
        if ans == listOfAns[i]:
            rightChoice =option[i]
        
    us_ans = input("Enter Answers  ")
    if us_ans == rightChoice:
        mark += 4
        print("Correct Answer""\n")
    else:
        print("Wrong Ans, Actual Ans: ", ans,"\n")
        mark += -1
print("mark "  , mark)  
print("Quiz solve")  


