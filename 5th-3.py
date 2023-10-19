print("""AI stand for : 
a = Artificsl intelligent
b = Artifical intelligent
c = Artifl intelligent
d = Artifical intelligence """)
ans1 = input("Enter correct answer : ")
if  ans1 == "d" :
   mark1 = 4
else:
    mark1 = 1
print("""pip stand for : 
a = pip install python 
b = pip index python
c = pip install project
d = pip project """)
ans2 = input("Enter correct answer : ")
if  ans2 == "c" :
   mark2 = 4
else:
    mark2 = -1
print("""CS stand for : 
a = computer sciences
b =  computer 
c = computer intelligent
d = Artifical intelligence """)
ans3 = input("Enter correct answer : ")    
if  ans3 == "a" :
   mark3 = 4
else:
    mark3 = -1
total_marks = mark1 + mark2 + mark3
print("total marks : ", total_marks)
