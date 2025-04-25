# Get user input
num = int(input("Enter a number: "))

# Initialize sum variable
sum_of_digits = 0

# Loop to extract and add digits
while num > 0:
    sum_of_digits += num % 10  # Add the last digit to the sum
    num = num // 10  # Remove the last digit

# Print the result
print("Sum of digits:", sum_of_digits)
