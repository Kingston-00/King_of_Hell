text = input("Enter text: ")

letters = 0
numbers = 0

for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        numbers += 1

print(f"letter:{letters} number:{numbers}")