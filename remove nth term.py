s = "hello"      # This is the original string
n = 2            # We want to remove the character at index 2 (which is 'l')

# This line slices the string to remove the character at index 2
new_s = s[:n] + s[n+1:]
print("After removing index", n, ":", new_s)
