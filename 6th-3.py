while (i):
            print("""A Simple Math Quiz
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Integer Division
            5. Exit
           """)
            operator = int(input("Enter operator ? "))
            if operator == 1:
    mark = 0
    for i in range(3):
        n1 = random.randrange(0,500)
        n2 = random.randrange(0,500)
        actual_answer = n1+n2
        option = ['a','b','c','d']
        print("The Addition of", n1, "and",n2 , "Enter your choice? ")
        listOfAns = [n1+n2,random.randrange(0,1000),random.randrange(0,1000),random.randrange(0,1000)]
        random.shuffle(listOfAns)
        for i in range(4):
       
            print(option[i],")",listOfAns[i])
            if actual_answer == listOfAns[i]:
    rightChoice =option[i]
           
        ans = input("Enter Answers  ")
        if ans == rightChoice:
           mark += 4
           print("Correct Answer""\n")
        else:
           print("Wrong Ans, Actual Ans: ", actual_answer,"\n")
           mark += -1
    print("mark "  , mark)  
    print("Quiz solve") 
    break
            elif operator == 2:
    mark = 0
    for i in range(3):
        n1 = random.randrange(0,500)
        n2 = random.randrange(0,500)
        actual_answer = n1-n2
        option = ['a','b','c','d']
        print("The Subtraction of", n1, "and",n2 , "Enter your choice? ")
        listOfAns = [n1-n2,random.randrange(0,1000),random.randrange(0,1000),random.randrange(0,1000)]
        random.shuffle(listOfAns)
        for i in range(4):
       
            print(option[i],")",listOfAns[i])
            if actual_answer == listOfAns[i]:
    rightChoice =option[i]
           
        ans = input("Enter Answers  ")
        if ans == rightChoice:
            mark += 4
            print("Correct Answer""\n")
        else:
            print("Wrong Ans, Actual Ans: ", actual_answer,"\n")
            mark += -1
    print("mark "  , mark)  
    print("Quiz solve") 
    break
             elif operator == 3:
    mark = 0
    for i in range(3):
        n1 = random.randrange(0,500)
        n2 = random.randrange(0,500)
        actual_answer = n1*n2
        option = ['a','b','c','d']
        print("The Multiplication of", n1, "and",n2 , "Enter your choice? ")
        listOfAns = [n1*n2,random.randrange(0,1000),random.randrange(0,1000),random.randrange(0,1000)]
        random.shuffle(listOfAns)
        for i in range(4):
       
            print(option[i],")",listOfAns[i])
            if actual_answer == listOfAns[i]:
    rightChoice =option[i]
           
        ans = input("Enter Answers  ")
        if ans == rightChoice:
            mark += 4
            print("Correct Answer""\n")
        else:
            print("Wrong Ans, Actual Ans: ", actual_answer,"\n")
            mark += -1
    print("mark "  , mark)  
    print("Quiz solve") 
    break
             elif operator == 4:
    mark = 0
    for i in range(3):
        n1 = random.randrange(0,500)
        n2 = random.randrange(0,500)
        actual_answer = n1n2
        option = ['a','b','c','d']
        print("The Integer Division of", n1, "and",n2 , "Enter your choice? ")
        listOfAns = [n1//n2,random.randrange(0,1000),random.randrange(0,1000),random.randrange(0,1000)]
        random.shuffle(listOfAns)
        for i in range(4):
       
            print(option[i],")",listOfAns[i])
            if actual_answer == listOfAns[i]:
    rightChoice =option[i]
           
        ans = input("Enter Answers  ")
        if ans == rightChoice:
            mark += 4
            print("Correct Answer""\n")
        else:
            print("Wrong Ans, Actual Ans: ", actual_answer,"\n")
            mark += -1
    print("mark "  , mark)  
    print("Quiz solve") 
    break
        else : 
            break
    break
