def average(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total / len(numbers)


numbers = [10, 15, 20, 18]

result = average(numbers)

print(result)

