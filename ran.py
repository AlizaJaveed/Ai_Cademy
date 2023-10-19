input_list = [5, 2, 9, 10, 4, 1, 3]
print(input_list)
even = []
odd = []
sorted_list = []
even_index = 0
odd_index = 0
for i in input_list:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
odd.sort()
for i in input_list:
    if i % 2 == 0:
        sorted_list.append(even[even_index])
        even_index += 1
    else:
        sorted_list.append(odd[odd_index])
        odd_index += 1
print(sorted_list)
