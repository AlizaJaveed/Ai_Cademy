import random
listofQuestion = ["What is AI", "What is DSA", "What is ML", "What is DL"]
listofAns = ["ai", "dsa", "ml", "dl"]
listofWrongans = [["dsa", "ml", "dl"], ["ai", "ml", "dl"], ["dsa", "ai", "dl"], ["dsa", "ml", "ai"]]
repeat = []
mark = 0
while len(repeat) < len(listofQuestion):
    sltdIndex = random.randint(0, 3)
    if sltdIndex in repeat:
        continue
    repeat.append(sltdIndex)
    print(listofQuestion[sltdIndex])
    answers = [listofAns[sltdIndex]] + listofWrongans[sltdIndex]
    random.shuffle(answers)
    for i in range(len(answers)):
        print(f"{i + 1}. {answers[i]}")
    user_ans = input("\nYour answer: ")
    if user_ans == listofAns[sltdIndex]:
        print("Your answer is correct!\n")
        mark += 4
    else:
        print("Your answer is wrong. The correct answer is:", listofAns[sltdIndex], "\n")
        mark -= 1
print(mark)        
print("Quiz complete.")