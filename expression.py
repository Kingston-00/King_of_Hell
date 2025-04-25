x = 5

# Convert to string to build 'xx' and 'xxx'
a = int(str(x))         # '5'
b = int(str(x)*2)       # '55'
c = int(str(x)*3)       # '555'

# Add them
result = a + b + c

print("x + xx + xxx =", result)
