numbers = [8, 12, 15, 7, 19, 20]


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