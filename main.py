name = input("What's your name?")

with open('example.txt', 'w') as file:
    file.write(f"{name} created this file")