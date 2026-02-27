'''
Rayaan Hassan 
CMSC 111
Spring 2026
Week 2 Assignment 4
'''
# Correct username and password
correct_username = "admin"
correct_password = "password123"

# Ask the user for their username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Verfi the username and password is correct
if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid credentials")  