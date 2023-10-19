import random
listofQuestion = ["What is AI", "What is DSA", "What is ML", "What is DL"]
listofAns = ["ai", "dsa", "ml", "dl"]
listofWrongans = [["dsa", "ml", "dl"], ["ai", "ml", "dl"], ["dsa", "ai", "dl"], ["dsa", "ml", "ai"]]
for i in range(3):
    sltdIndex = random.randint(0, 3)
    print(listofQuestion[sltdIndex])
    print(listofAns[sltdIndex])
    answers = [listofAns[sltdIndex]] + listofWrongans[sltdIndex]
    random.shuffle(answers)
    for idx, ans in enumerate(answers):
        print(f"{idx + 1}. {ans}")
    user_ans = input("\nYour answer: ")
    if user_ans == listofAns[sltdIndex]:
        print("Your answer is correct!\n")
    else:
        print("Your answer is wrong.\n")
        while True:
            shuffle_option = input("Do you want to shuffle the options? (yes/no): ").lower()
            if shuffle_option == "yes":
                random.shuffle(answers)
                for idx, ans in ranfge(len(answers)):
                    print(f"{idx + 1}. {ans}")
                user_ans = input("\nYour answer: ")
                if user_ans == listofAns[sltdIndex]:
                    print("Your answer is correct!\n")
                    break
                else:
                    print("Your answer is still wrong.\n")
            elif shuffle_option == "no":
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
