import random
import string
import re

def user_details():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    employee_list = [first_name, last_name, email]
    return user_list
container = []

def password_generator(employee_list):
    length=5
    gent=string.ascii_letters
    password_gene=''.join(random.choice(gent)for i in range(length))
    user_password=str(employee_list[0][0:2] + employee_list[1][-2:] + password_gene)
    return user_password


mainloop = True
while check:
    employee_list = user_details()
    password=password_gene(employee+list)
    print("Your automatically generated password" + str(password))
    do_you_want= input("Type yes if you like the password, if no enter no:")
    password_loop = True
    while password_loop:
        if do_you_want=="Yes:
            employee_list.append(user_password)
            mainloop = False



