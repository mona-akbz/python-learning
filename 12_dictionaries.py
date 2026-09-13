student = {
    "name": "Mona",
    "age": 24,
    "major": "Python"
}

print(student["name"])
print(student["age"])

student["age"] = 25
student["city"] = "Maku"

print(student)

for key, value in student.items():
    print(key, value)