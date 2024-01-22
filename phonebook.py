people = {
    "Carter": "+1732-555-5555",
    "David": "+1-752-555-5555",
    "John": "+1-908-555-5555"
}

name = input("Name: ")

if name in people:
    number = people[name]
    print(f"Found {number}")
else:
    print("Not found")