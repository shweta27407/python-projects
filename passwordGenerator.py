import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['%', '&', '@', '*', '(', ')']
numbers = ['0', '1', '2', '3', '4', '5', '7', '8']

print("Welcome to Password Generator")
letters_no = int(input("How many letters in password? : "))
symbol_no = int(input("How many symbol in password? : "))
numbers_no = int(input("How many numbers in password? : "))

password = ""

letter_in_pswd = ""
symbol_in_pswd = ""
number_in_pswd = ""

for i in range(0, letters_no):
    letter_in_pswd += letters[random.randint(0, len(letters) - 1)]
print(letter_in_pswd)

for i in range(0, symbol_no):
    symbol_in_pswd += symbols[random.randint(0, len(symbols) - 1)]
print(symbol_in_pswd)

for i in range(0, numbers_no):
    number_in_pswd += numbers[random.randint(0, len(numbers) - 1)]
print(number_in_pswd)

#password = letter_in_pswd + symbol_in_pswd + number_in_pswd
temp_paswd = letter_in_pswd + symbol_in_pswd + number_in_pswd

print(temp_paswd, temp_paswd[1], temp_paswd[0])
paswd_len = letters_no + symbol_no + numbers_no
for i in range(0, paswd_len):
    password += temp_paswd[random.randint(0, len(temp_paswd) - 1)]
print(password)




