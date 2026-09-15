numbers = []

for i in range(5):
    number = float(input("Enter a score: "))
    numbers.append(number)

 
def average(numbers):
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)


print("Average:", average(numbers))

print("Passing scores:")

for number in numbers:
    if number >= 10:
        print(number)   