#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pass_letters=""
pass_symbols=""
pass_numbers=""

for iter in range(1, nr_letters+1):
    tmp=random.randint(0,len(letters))
    pass_letters+=letters[tmp-1]

for iter in range(1, nr_symbols+1):
    tmp=random.randint(0,len(symbols))
    pass_symbols+=symbols[tmp-1]

for iter in range(1, nr_numbers+1):
    tmp=random.randint(0,len(numbers))
    pass_letters+=numbers[tmp-1]


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
print("Easy password:")
password_easy=pass_letters+pass_symbols+pass_numbers
print(password_easy)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
print("Hard password:")
password_hard="".join(random.sample(password_easy,len(password_easy)))
print(password_hard)
