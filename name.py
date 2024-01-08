import sys # Type "python name.py Kevin"

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("too many arguments")

print("hello, my name is", sys.argv[1])
