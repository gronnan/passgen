import random
from string import ascii_letters
passlenght = int(input("Write lenght of your password: "))
password = ""
for i in range(0,passlenght):
    password += random.choice(ascii_letters)

print("your password is ", password)

