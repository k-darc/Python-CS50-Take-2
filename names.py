# Lecture 6 - File i/o
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()