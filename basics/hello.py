# Get user name
name = input("Enter your name: ")
name = name.strip().title()
first, last = name.split(" ")
print("Hello", first, last)