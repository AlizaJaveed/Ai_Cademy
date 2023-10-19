import random 
listofQuestion = ["What is AI","What is DSA","What is ML","What is DL"]
listofAns=["ai","dsa","ml","dl"]
listofWrongans=[["dsa","ml","dl"],["ai","ml","dl"],["dsa","ai","dl"],["dsa","ml","ai"]]
for i in range(3):
    sltdIndex = random.randint(0,3)
    print(listofQuestion[sltdIndex])
    print(listofAns[sltdIndex])
    for j in range(3):
        print(listofWrongans[sltdIndex][j])

    user_ans = input("\nYour answer: ")
    if user_ans == listofAns[sltdIndex]:
        print("Your answer is correct!\n")
    else:
        print("Your answer is wrong.\n")
        