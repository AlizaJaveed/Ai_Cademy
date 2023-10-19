# Problem 2:
# Imagine you've just purchased an apple orchard and have set up an ordering system where
# customers can enter the number of baskets of apples they want delivered to their home or business.
# Each basket can hold 47 apples, but you've just realized that the shipping crates can only hold 20
# apples each and your shipping partner does not allow you to send partially packed crates.
# Write a program that does the following:
# ● prints the number of completely full crates you can pack based on the number of baskets
# entered
# ● prints the number apples that will be left out of the order
# Example Output:
# How many baskets of apples does the customer want? 78
# This order will require 183 crates.
# Due to shipping restrictions 6 apples will be left out of this order.
baskets_of_apples = 47
baskets_of_crates = 20
basket = int(input("How many baskets of apples does the customer want? "))
total_apple = basket * baskets_of_apples
require_crates = total_apple // baskets_of_crates
left_apple = total_apple % baskets_of_crates
print(f"This order will require {require_crates} crates.")
print(f"Due to shipping restrictions {left_apple} apples will be left out of this order.")