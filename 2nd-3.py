num = 10
for i in range(5, num+1 , 2):
    base = int(input("Enter base for triangle : "))
    height = i
    tri = 0.5 * height * base
    print("if base is ", base,"and height is " , height , "then \nArea of triangle is :" , tri)
    i += 1