import random
f = open("QUESTION.txt")
#print(f.read())
listOfQuestion= []
for i in f :
    splitOption = i.split("?")
    listOfQuestion.append(splitOption)
print(listOfQuestion)
f = open("ANSWER.txt")
listOfAnswer= []
for i in f :
    splitOption = i.split(" ")
    listOfAnswer.append(splitOption)
print(listOfAnswer)
f = open("WRONG.txt")
listOfWrong= []
for i in f :
    splitOption = i.split(",")
    listOfWrong.append(splitOption)
print(listOfWrong)
