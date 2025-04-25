# List of words
words = ["apple", "banana", "grape", "orange", "cherry", "mango", "kiwi"]

# Get a letter from the user
letter = input("Enter a letter to search for: ").lower()

# Find and print words containing the letter
print("Words containing the letter", letter + ":")
for word in words:
    if letter in word.lower():
        print(word)