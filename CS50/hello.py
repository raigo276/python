# Ask user for their name
name = input("What is your name? ")

# Remove whitespace from str and capitalize
name = name.strip().title()

# Split user's name into first name and last name
first, last =  name.split(" ")
print(first)
print(last)
# Capitalize user's name
# name = name.capitalize()

print(f"hello, {name}")
print("hello, " + name)
# print("Hello, World!")