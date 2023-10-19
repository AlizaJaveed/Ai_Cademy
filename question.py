# x = 87
# result = {x > 190: "First condition satisfied!",
#           x == 87: "Second condition satisfied!"}.get(
#     True, "Third condition satisfied")
# 
# print(result)
num = int(input("Enter number"))
res = {(num==121) :" pagal" , (num>12):"masoom" }.get(True , "parwaz")
print(res)