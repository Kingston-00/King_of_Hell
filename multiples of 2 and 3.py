# Take 10 integers from the user
numbers = [int(input(f"Enter integer {i+1}: ")) for i in range(10)]

# Print multiples of 2 and 3
print("\nMultiples of 2 and 3:")
for num in numbers:
    if num % 2 == 0 and num % 3 == 0:
        print(num)
