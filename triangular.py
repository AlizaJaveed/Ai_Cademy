rows = 5
for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
print("\n")
print("\n")
print("\n")
print("\n")
for i in range(rows):
    
    for j in range(i):
        print("*", end = "")
    print()
print("\n")
print("\n")
print("\n")
print("\n")
num = 1
for i in range(rows):
        for j in range(rows - i - 1):
            print(" ", end=" ")
        for j in range(i + 1):
            print(num, end=" ")
            num += 2
        print()