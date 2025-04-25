import random

# Characters
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
special = "$@#"
all_chars = upper + lower + special + "0123456789"

# Generate password
password = random.choice(upper) + random.choice(special) + random.choice(lower)
password += ''.join(random.choices(all_chars, k=random.randint(5, 11)))

# Shuffle and print
password = ''.join(random.sample(password, len(password)))
print("Generated password:", password)
