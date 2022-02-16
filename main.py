#Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# choosing random letters
chosen_letters = list()
for l in range(0, nr_letters):
  letter = random.choice(letters)
  chosen_letters.append(letter)
# print(chosen_letters)

# choosing random numbers
chosen_numbers = list()
for l in range(0, nr_numbers):
  number = random.choice(numbers)
  chosen_numbers.append(number)
# print(chosen_numbers)

# choosing random symbols
chosen_symbols = list()
for l in range(0, nr_symbols):
  symbol = random.choice(symbols)
  chosen_symbols.append(symbol)
# print(chosen_symbols)

# making one list containing all chosen elements
all_chosen_elements = chosen_letters + chosen_numbers + chosen_symbols
# print(all_chosen_elements)

# creating the password
password = ''
used_indexes = list()
random_element_index = int()
for num in range(0, len(all_chosen_elements)):
  # choosing elements from the list without repetition
  while random_element_index in used_indexes:
    random_element_index = random.randint(0, len(all_chosen_elements)-1)
  password += all_chosen_elements[random_element_index]
  used_indexes.append(random_element_index)

# printing the password
print(password)
