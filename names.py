# Lecture 6 - File i/o
name = input("What's your name? ")


with open("names.txt", "a") as file:
    file.write(f"{name}\n")