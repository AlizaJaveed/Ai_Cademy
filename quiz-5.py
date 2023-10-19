import random
i=1
while(i):
    print("""
    a) ENGLISH
    b) computer
    c) MATH
    """)
    select = input("Select Options : ")
    if select == 'a':
        print("ENGLISH")
        print("""Question 1
        Select The Correct and Suitable English Grammar Letter: R----ad ?
        a) Ea
        b) A
        c) U
        d) E
        """)
        ans1 = input("Enter correct answer : ")
        if  ans1 == "d" :
            mark1 = 4
        else:
            mark1 = -1
        print("""Question 2
        CHOOSE THE ANONYMS(OPPOSITE WORDS): BOIL ?
        a) Steam
        b) Freeze
        c) Cold
        d) Hot
        """)
        ans2 = input("Enter correct answer : ")
        if  ans2 == "b" :
            mark2 = 4
        else:
            mark2 = -1
        print("""Question 3
        PUT THE Correct TENSE: The boys are------their home task ?
        a) None
        b) Doing
        c) Do
        d) Both a and b
        """)
        ans3 = input("Enter correct answer : ")    
        if  ans3 == "b" :
            mark3 = 4
        else:
            mark3 = -1
        total_marks = mark1 + mark2 + mark3
        print("total marks : ", total_marks)
            

        break
    elif select == 'b':
        print("computer")
        print("""Question 1
        Who is the father of Computers?
        a) James Gosling
        b) Charles Babbage
        c) Dennis Ritchie
        d) Bjarne Stroustrup """)
        ans1 = input("Enter correct answer : ")
        if  ans1 == "b" :
            mark1 = 4
        else:
            mark1 = -1
        print("""Question 2
        What is the full form of CPU?
        a) Computer Processing Unit
        b) Computer Principle Unit
        c) Central Processing Unit
        d) Control Processing Unit
         """)
        ans2 = input("Enter correct answer : ")
        if  ans2 == "c" :
            mark2 = 4
        else:
            mark2 = -1
        print("""Which of the following computer language
        is written in binary codes only?
        a) pascal
        b) machine language
        c) C
        d) C# 
        """)
        ans3 = input("Enter correct answer : ")    
        if  ans3 == "b" :
            mark3 = 4
        else:
            mark3 = -1
        total_marks = mark1 + mark2 + mark3
        print("total marks : ", total_marks)
        break
    elif select == 'c':
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
                    actual_answer = n1//n2
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

    else:
        print("invaild option")
        i += 1