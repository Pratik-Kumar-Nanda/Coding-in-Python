"""
Python String Methods Playground
Author: Pratik Kumar Nanda

This project demonstrates commonly used Python string methods
with examples and user input.
"""


text = "Hello everyone, today I am learning Python"

# basic_methods

print("--Basic methods--")
print(f"Original String: {text}")
print(f"Length of string: {len(text)}")
print(f"Capitalize: {text.capitalize()}")
print(f"Upper case: {text.upper()}")
print(f"Lower case: {text.lower()}")
print(f"Title case: {text.title()}")

# search_methods 

print("--Search methods --")
print(f"Ends with 'Python': {text.endswith('Python')}")
print(f"Starts with 'Hello': {text.startswith('Hello')}")
print(f"Frequency of 'o': {text.count('o')}")
print(f"First occurrence of 'o': {text.find('o')}")


# replace_methods

print("--Replace methods--")
replaced_text = text.replace("everyone", "world")

print(f"Original text: {text}")
print(f"Replaced text: {replaced_text}")


# split_and_strip

print("--Split and Strip--")
messy_text = "   Python is fun to learn   "

print(f"Original text: '{messy_text}'")
print(f"After strip(): '{messy_text.strip()}'")

words = messy_text.strip().split()

print(f"After split(): {words}")


# user_input_demo

print("--User input demo--")
user_text = input("Enter a sentence: ")

print(f"You entered: {user_text}")
print(f"Upper case: {user_text.upper()}")
print(f"Word count: {len(user_text.split())}")
print(f"Reversed string: {user_text[::-1]}")


