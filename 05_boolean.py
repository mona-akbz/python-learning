age = int(input("Enter your age: "))

is_member = bool(input("Are you a member? "))

if age >= 18 and is_member:
    print("Access granted")
else:
    print("Access denied")