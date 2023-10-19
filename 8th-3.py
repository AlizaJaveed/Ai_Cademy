import random

# Read questions from "QUESTION.txt"
with open("QUESTION.txt", "r") as f:
    listOfQuestion = [line.strip() for line in f]

# Read correct answers from "ANSWER.txt"
with open("ANSWER.txt", "r") as f:
    listOfAnswer = [line.strip() for line in f]

# Read wrong answers from "WRONG.txt"
with open("WRONG.txt", "r") as f:
    listOfWrong = [line.strip() for line in f]

repeat = []
mark = 0

while len(repeat) < len(listOfQuestion):
    sltdIndex = random.randint(0, len(listOfQuestion) - 1)
    if sltdIndex in repeat:
        continue

    repeat.append(sltdIndex)
    print(listOfQuestion[sltdIndex])

    answers = [listOfAnswer[sltdIndex]] + random.sample(listOfWrong, 3)
    random.shuffle(answers)

    for i, answer in enumerate(answers, start=1):
        print(f"{i}. {answer}")

    user_ans = int(input("\nYour answer (enter the number): "))
    if user_ans == answers.index(listOfAnswer[sltdIndex]) + 1:
        print("Your answer is correct!\n")
        mark += 4
    else:
        print("Your answer is wrong. The correct answer is:", listOfAnswer[sltdIndex], "\n")
        mark -= 1

print("Total marks:", mark)
print("Quiz complete.")
