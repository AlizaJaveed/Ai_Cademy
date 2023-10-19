import random
listofQuestion = ["What is AI", "What is DSA", "What is ML", "What is DL"]
listofAns = ["ai", "dsa", "ml", "dl"]
listofWrongans = [["dsa", "ml", "dl"], ["ai", "ml", "dl"], ["dsa", "ai", "dl"], ["dsa", "ml", "ai"]]
repeart = []
#for i in range(3):
#    sltdIndex = random.randint(0, 3)
 #   print(listofQuestion[sltdIndex])
#    answers = [listofAns[sltdIndex]] + listofWrongans[sltdIndex]
#    random.shuffle(answers)
#    for ans in answers:
#        print(ans)
#   user_ans = input("\nYour answer: ")
#    if user_ans == listofAns[sltdIndex]:
#       print("Your answer is correct!\n")
#    else:
#        print("Your answer is wrong.\n")
while len(repeart) < len(listofQuestion):
    sltdIndex = random.randint(0, 3)
    if sltdIndex in repeat:
        continue
    repeat.append(sltdIndex)
    print(listofQuestion[sltdIndex])
    