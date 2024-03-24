# Import Python library
import random

# Import local libraries
import numbers
import letters
import symbols

# Print welcome message and ask for number of letters, symbols and letters
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Create an empty list
password = []

# Iterate of input for letters
for i in range(0, nr_letters):
        
    # Pick a random letter from the list
    random_letter = random.randint(0, len(letters.letters) - 1)
    picked_letters = letters.letters[random_letter]
    password.append(picked_letters)
    
    
# Iterate of input for symbols
for i in range(0, nr_symbols):
    
    # Pick a random symbol from the list
    random_symbol = random.randint(0, len(symbols.symbols) - 1)
    picked_symbols = symbols.symbols[random_symbol]
    password.append(picked_symbols)


# # Iterate of input for numbers
for i in range(0, nr_numbers):
    
    # Pick a random number from the list
    random_number = random.randint(0, len(numbers.numbers) - 1)
    picked_numbers = numbers.numbers[random_number]
    password.append(picked_numbers)


# Shuffle the password
safe_password = random.sample(password, len(password))     

# Print the new password   
print(f"Your new password is: ", end="")

# Create new password   
for i in safe_password:
	print(i, end="")


