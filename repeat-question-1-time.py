import random
listofQuestion = ["What is AI", "What is DSA", "What is ML", "What is DL"]
listofAns = ["ai", "dsa", "ml", "dl"]
listofWrongans = [["dsa", "ml", "dl"], ["ai", "ml", "dl"], ["dsa", "ai", "dl"], ["dsa", "ml", "ai"]]
lenthOfquestion = len(listofQuestion)
asked_questions = []
while len(asked_questions) < lenthOfquestion:
    sltdIndex = random.randint(0, 3)
    if sltdIndex in asked_questions:
        continue
    asked_questions.append(sltdIndex)
    print(listofQuestion[sltdIndex])
    answers = [listofAns[sltdIndex]] + listofWrongans[sltdIndex]
    random.shuffle(answers)
    for i in range(len(answers)):
        print(f"{i + 1}. {answers[i]}")
    user_ans = input("\nYour answer: ")
    if user_ans == listofAns[sltdIndex]:
        print("Your answer is correct!\n")
    else:
        print("Your answer is wrong. The correct answer is:", listofAns[sltdIndex], "\n")
print("Quiz complete.")
