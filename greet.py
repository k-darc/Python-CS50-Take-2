from sys import argv

if len(argv) == 2:
    print(f"Hello, {argv[1]}")
else:
    print("hello, world")

#Run as: python greet.py Kevin