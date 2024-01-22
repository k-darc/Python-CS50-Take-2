people = [
    {"name": "Carter", "number": "+1-732-555-5555"},
    {"name": "David", "number": "+1-752-555-5555"},
    {"name": "John", "number": "+1-908-555-5555"},
]

name = input("Name: ")

for person in people:
    if person["name"] == name:
        number = person["number"]
        print(f"Found {number}")
        break

else:
    print("Not found")