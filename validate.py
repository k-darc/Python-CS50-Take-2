# Lecture 7 - Regular Expressions
email = input("What's your email? ").strip()

if "@"  in email:
    print("Valid")
else:
    print("Invalid")