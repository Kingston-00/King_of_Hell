numbers = [3, -2, 7, -5, 0, 9, -1]

positive = 0
negative = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)
