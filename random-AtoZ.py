# Import string and random module
import string
import random

# Randomly choose a letter from all the ascii_letters
randomLetter = chr(random.randint(ord('a'), ord('d')))
print(randomLetter)

a = random.random()  # Generates a random float between 0 and 1 (excluding 1)
b = random.randint(1, 100)  # Generates a random integer between 1 and 100 (including both endpoints)
c = random.choice(string.ascii_lowercase)  # Generates a random lowercase letter
d = random.choice(string.ascii_uppercase)  # Generates a random uppercase letter

print("Random a:", a)
print("Random b:", b)
print("Random c:", c)
print("Random d:", d)
print("\n")
# Generate random values for a, b, c, and d
a = random.choice(range(1, 101))  # Random integer between 1 and 100 (including 1 but excluding 101)
b = random.choice(range(1, 101))  # Random integer between 1 and 100 (including 1 but excluding 101)
c = random.choice(range(1, 101))  # Random integer between 1 and 100 (including 1 but excluding 101)
d = random.choice(range(1, 101))  # Random integer between 1 and 100 (including 1 but excluding 101)

# Create a list containing a, b, c, and d
options = [a, b, c, d]

# Shuffle the options
random.shuffle(options)

# Present the multiple-choice options to the user
print("Choose the correct option for each variable:")
print("a) ", options[0])
print("b) ", options[1])
print("c) ", options[2])
print("d) ", options[3])

# You can use input() to get the user's response and check if it's correct.
# For this example, I'll just print the correct values.
print("\nCorrect values:")
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
