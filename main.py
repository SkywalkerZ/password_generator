import random as rd

#lists
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
u_letters = [l.upper() for l in letters]
final_letters = letters + u_letters
final_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
final_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#user inputs
print("Welcome to the SkywalkerZ's Password Generator!")
pw_letters= int(input("How many letters would you like in your password?\n")) 
pw_symbols = int(input(f"How many symbols would you like?\n"))
pw_numbers = int(input(f"How many numbers would you like?\n"))

#random selection from lists
string_letters=[]
for rand_letters in range(0,pw_letters):
  string_letters += rd.choice(final_letters)
string_symbols=[]
for rand_symbols in range(0,pw_symbols):
  string_symbols += rd.choice(final_symbols)
string_numbers=[]
for rand_numbers in range(0,pw_numbers):
  string_numbers += rd.choice(final_numbers)

#randomization of string
password=""
final_string=string_letters+string_symbols+string_numbers
rd.shuffle(final_string)

for chars in final_string:
  password += chars
print(f"Your newly generated password is: {password}")