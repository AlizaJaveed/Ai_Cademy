# Problem 5:
# You want to create an app that keeps track of your friends’ and family’s holiday wish list throughout
# the year. Write a simple program that does the following:
# 1. Contains a single dictionary of your family members’ names (key) and their wish lists (value).
# 2. Allows you to look up each list using their name and add items to it (hint: you can call
# relevant methods on any objects in your dictionary ex. my_dictionary['some_name'].add('fire
# truck')
# Example output:
# Enter name of wish list to update: John
# John’s current wish list: teddy bear, cookies, scarf
# Enter item to add to list: G.I.Joe
# John’s new wish list: teddy bear, cookies, scarf, G.I.Joe
dictionary = {
"John" : ["teddy bear", "cookies", "scarf"],
"Parwaz" : ["book", "bag", "pizza"],
"Aliza" : ["tea", "Apple", "kulfi"]
  }
name = input("Enter name of wish list: ")
if name in dictionary:
    print(f"{name}'s current wish list: ",dictionary[name])
    item = input("Enter item to add to list: ")
    dictionary[name].append(item)
    print(f"{name}'s new wish list: " ,dictionary[name])
    