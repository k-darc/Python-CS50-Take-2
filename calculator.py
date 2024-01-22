# def main():
#     x = int(input("What's x? "))
#     print("x squared is", square(x))

# def square(n):
#     return n * n

# if __name__ == "__main__":
#     main()

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Not an integer")

def main():
    x = get_int("x: ")
    y = get_int("y: ")

    print( x + y)

main()