# Get input from user
day = int(input("Enter day of birth (1-31): "))
month = int(input("Enter month of birth (1-12): "))
year = int(input("Enter year of birth: "))

# Store in a tuple
my_bday = (day, month, year)

# Display the birthday
print(f"Your birthday is on {day:02d}/{month:02d}/{year}")
