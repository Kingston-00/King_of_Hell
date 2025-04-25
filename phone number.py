# Write contacts to a file
file = open("contacts.txt", "w")
file.write("Alice:1234\nBob:2345\nCharlie:3456\nDavid:4567\nEva:5678\n")
file.write("Frank:6789\nGrace:7890\nHelen:8901\nIan:9012\nJack:0123\n")
file.close()

# Ask for name
name = input("Enter name to search: ")

# Read and search
file = open("contacts.txt", "r")
for line in file:
    if name in line:
        print("Phone number:", line.split(":")[1])
        break
else:
    print("Name not found.")
file.close()
