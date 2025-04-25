file = open("devil.txt", "r")
text = file.read()
file.close()

words = text.split()
print("Number of words:", len(words))

alphabets = 0
digits = 0
spaces = 0

for ch in text:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch == ' ':
        spaces += 1

print("Number of alphabets:", alphabets)
print("Number of digits:", digits)
print("Number of spaces:", spaces)
